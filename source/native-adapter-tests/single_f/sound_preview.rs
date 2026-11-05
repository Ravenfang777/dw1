//! Numbered KH2 sound auditions. Audio selection never acquires a moveset or AP slot.
use crate::dual_wield::Binding;
use std::sync::atomic::{AtomicU32,Ordering};
pub const FIRST:u32=66;
pub const COUNT:usize=45;
pub const MASK:u64=(1u64<<COUNT)-1;
pub const UNKNOWN:u32=u32::MAX;
#[derive(Clone,Copy,Debug,PartialEq,Eq)]
pub enum Source{InfinityCharge,Counterguard,Sound(u32)}
#[derive(Clone,Copy,Debug)]
pub struct Spec{pub source:Source}
const fn specs()->[Spec;COUNT]{
    let mut out=[Spec{source:Source::InfinityCharge};COUNT];out[1]=Spec{source:Source::Counterguard};
    let mut i=2;while i<COUNT{out[i]=Spec{source:Source::Sound(999000+(i-2)as u32)};i+=1;}out
}
pub const SPECS:[Spec;COUNT]=specs();
pub fn get(id:u32)->Option<&'static Spec>{id.checked_sub(FIRST).and_then(|i|SPECS.get(i as usize))}
impl Spec{
    pub fn name(self)->String{match self.source{Source::InfinityCharge=>"Infinity Tip Charge sound".into(),Source::Counterguard=>"Counterguard Hand Flash sound".into(),Source::Sound(id)=>format!("KH2 sound {id}")}}
    pub fn identifier(self)->String{match self.source{Source::InfinityCharge=>"KH2 Limit Form / element 20".into(),Source::Counterguard=>"KH2 Sora / element 41".into(),Source::Sound(id)=>format!("KH2 se999 / SE {id}")}}
    pub fn package(self)->Option<(&'static str,u16)>{match self.source{Source::InfinityCharge=>Some(("obj/P_EX100_KH1F.a.us",20)),Source::Counterguard=>Some(("obj/P_EX100.a.us",41)),_=>None}}
}
//0 loading,1 decoded,2 no assigned/playable sound,3 missing archive/bank,
//4 unsupported/malformed audio,5 decoded audio exceeds preview budget.
static STATUS:[AtomicU32;COUNT]=[const{AtomicU32::new(0)};COUNT];
static IDS:[AtomicU32;COUNT]=[const{AtomicU32::new(UNKNOWN)};COUNT];
pub fn status(id:u32)->u32{id.checked_sub(FIRST).and_then(|i|STATUS.get(i as usize)).map_or(3,|v|v.load(Ordering::Acquire))}
pub fn resolved(id:u32)->u32{
    let Some(spec)=get(id)else{return UNKNOWN;};if let Source::Sound(n)=spec.source{return n;}
    IDS[(id-FIRST)as usize].load(Ordering::Acquire)
}
pub fn set(id:u32,sound:u32,status:u32){if let Some(i)=id.checked_sub(FIRST).filter(|i|(*i as usize)<COUNT){IDS[i as usize].store(sound,Ordering::Release);STATUS[i as usize].store(status.min(5),Ordering::Release);}}
pub fn unavailable(){for i in 0..COUNT{set(FIRST+i as u32,UNKNOWN,3);}}
pub fn audio_budget(rate:u32,channels:u16,samples:usize,already:usize)->bool{
    (4000..=96000).contains(&rate)&&(1..=2).contains(&channels)&&samples>=channels as usize*2
        &&samples<=rate as usize*channels as usize*15
        &&samples.checked_mul(2).and_then(|n|n.checked_add(already)).is_some_and(|n|n<=64*1024*1024)
}
/// One audition at ground-combo entry. Continuing hits do not restart the sound.
#[derive(Default,Debug)]
pub struct Trigger{binding:Option<Binding>,choice:u32,latched:bool,idle:f32,last_frame:Option<u64>}
impl Trigger{
    pub fn step(&mut self,binding:Option<Binding>,choice:u32,frame:u64,ground_combo:bool,paused:bool,delta:f32)->bool{
        if self.binding!=binding||self.choice!=choice{self.binding=binding;self.choice=choice;self.latched=false;self.idle=0.;self.last_frame=None;}
        if binding.is_none()||get(choice).is_none(){self.latched=false;return false;}
        if paused||self.last_frame==Some(frame){return false;}self.last_frame=Some(frame);
        if !ground_combo{self.idle+=if delta.is_finite(){delta.clamp(0.,4.)}else{0.};if self.idle>=3.{self.latched=false;}return false;}
        self.idle=0.;if self.latched{return false;}self.latched=true;true
    }
}
pub fn native_ground(state:i32,request:u32,current:bool)->bool{state==0&&current&&matches!(request&0xffff,0xc8..=0xcb)}

#[cfg(test)]mod tests{
    use super::*;
    fn b()->Binding{Binding{actor:1,instance:2,matrices:3,weapon:4,generation:1}}
    #[test]fn catalogue_covers_two_named_sources_and_every_se999_id_zero_through_42(){
        assert_eq!(get(66).unwrap().package(),Some(("obj/P_EX100_KH1F.a.us",20)));assert_eq!(get(67).unwrap().package(),Some(("obj/P_EX100.a.us",41)));
        for n in 0..43{let s=get(68+n).unwrap();assert_eq!(s.source,Source::Sound(999000+n));assert!(s.identifier().contains(&(999000+n).to_string()));assert!(s.name().len()<35);}
        assert!(get(65).is_none()&&get(111).is_none());assert_eq!(MASK.count_ones(),45);
    }
    #[test]fn a_combo_plays_once_including_chain_transitions_and_an_air_combo_never_starts_it(){
        let mut t=Trigger::default();assert!(t.step(Some(b()),68,1,true,false,1.));
        for f in 2..10{assert!(!t.step(Some(b()),68,f,true,false,1.));}
        assert!(!t.step(Some(b()),68,10,false,false,1.));assert!(!t.step(Some(b()),68,11,true,false,1.));
        for f in 12..15{assert!(!t.step(Some(b()),68,f,false,false,1.));}assert!(t.step(Some(b()),68,15,true,false,1.));
        for state in [1,2,21]{assert!(!native_ground(state,0xc8,true));}for req in [0,0x36,0xcc,0xd4,0xdc]{assert!(!native_ground(0,req,true));}
        for req in 0xc8..=0xcb{assert!(native_ground(0,req,true));assert!(!native_ground(0,req,false));}
    }
    #[test]fn selection_scope_pause_and_duplicate_physics_do_not_leak_an_audition(){
        let mut t=Trigger::default();assert!(!t.step(Some(b()),68,1,true,true,1.));assert!(t.step(Some(b()),68,1,true,false,1.));assert!(!t.step(Some(b()),68,1,true,false,1.));
        assert!(!t.step(None,68,2,true,false,1.));assert!(t.step(Some(b()),69,3,true,false,1.));assert!(!t.step(Some(b()),0,4,true,false,1.));
        assert!(!t.step(Some(b()),69,5,false,false,1.));assert!(t.step(Some(b()),69,6,true,false,1.));
    }
    #[test]fn preview_decode_budget_is_bounded_and_sound_ids_do_not_assume_stream_numbers(){
        assert!(audio_budget(48000,2,48000*2,0));for args in [(0,2,100,0),(48000,0,100,0),(48000,2,1,0),(48000,2,48000*2*16,0),(48000,2,100,64*1024*1024)]{assert!(!audio_budget(args.0,args.1,args.2,args.3));}
        assert_eq!(kh2_formats::scd::split_id(999038),(999,38));assert_eq!(kh2_formats::scd::bank_file(999),"se/se999.win32.scd");
    }
    #[test]fn upgrading_visual_flags_does_not_unexpectedly_play_a_sound_and_reserved_flags_persist(){
        let reserved=(1u64<<48)|(1u64<<50);let all=MASK|reserved;
        for marker in ["weapon_effects=kh2-v1","animation_tests=ventus-v1",""]{
            assert_eq!(crate::dual_wield::numbered_state(&format!("{marker}\nenabled={all}")),Some(reserved));
        }
        for bit in 0..COUNT{let bits=(1u64<<bit)|reserved;assert_eq!(crate::dual_wield::numbered_state(&crate::dual_wield::numbered_state_text(bits)),Some(bits));}
        assert_eq!(crate::dual_wield::numbered_state(&format!("sound_previews=kh2-v1\nenabled={all}")),Some(1|reserved));
    }
}
