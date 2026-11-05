//! Visual-only KH2 weapon effect gallery. IDs66..104 replace old animation tests.
//! Names identify traced attack families; unrendered particle details are not inferred.
use glam::Mat4;
use std::sync::atomic::{AtomicU32,Ordering};

pub const FIRST:u32=66;
pub const COUNT:usize=39;
pub const MASK:u64=(1u64<<COUNT)-1;
#[derive(Clone,Copy,Debug,PartialEq,Eq)]
#[repr(usize)]
pub enum Package{Weapon,Sora,Limit,Valor,Final}
pub const PACKAGES:[Package;5]=[Package::Weapon,Package::Sora,Package::Limit,Package::Valor,Package::Final];
impl Package{
    pub const fn path(self)->&'static str{match self{
        Self::Weapon=>"obj/W_EX010.a.us",Self::Sora=>"obj/P_EX100.a.us",Self::Limit=>"obj/P_EX100_KH1F.a.us",
        Self::Valor=>"obj/P_EX100_BTLF.a.us",Self::Final=>"obj/P_EX100_ULTF.a.us",
    }}
    pub const fn label(self)->&'static str{match self{Self::Weapon=>"Kingdom Key",Self::Sora=>"Sora",Self::Limit=>"Limit Form",Self::Valor=>"Valor Form",Self::Final=>"Final Form"}}
}
#[derive(Clone,Copy,Debug)]
pub struct Spec{pub package:Package,pub element:u16,pub name:&'static str,pub blade_host:bool}
macro_rules! fx{($p:ident,$id:literal,$name:literal)=>{Spec{package:Package::$p,element:$id,name:$name,blade_host:false}};($p:ident,$id:literal,$name:literal,blade)=>{Spec{package:Package::$p,element:$id,name:$name,blade_host:true}};}
pub const SPECS:[Spec;COUNT]=[
    fx!(Weapon,0,"Weapon appearance flash",blade),
    fx!(Limit,35,"Last Arcanum root glow"),fx!(Limit,36,"Last Arcanum tip glow"),
    fx!(Limit,32,"Strike Raid blade ribbon",blade),
    fx!(Valor,13,"Valor finisher burst 13"),fx!(Valor,14,"Valor finisher burst 14"),
    fx!(Final,20,"Final weapon burst 20"),
    fx!(Final,42,"Final weapon burst 42"),fx!(Final,43,"Final weapon burst 43"),
    fx!(Final,44,"Final weapon burst 44"),fx!(Final,45,"Final weapon burst 45"),
    fx!(Final,46,"Final weapon burst 46"),fx!(Final,47,"Final weapon burst 47"),
    fx!(Final,101,"Final weapon burst 101"),fx!(Final,102,"Final weapon burst 102"),
    fx!(Sora,30,"Guard Break effect 30"),fx!(Sora,31,"Guard Break effect 31"),fx!(Sora,32,"Guard Break effect 32"),
    fx!(Sora,33,"Finishing Leap effect 33"),fx!(Sora,34,"Finishing Leap effect 34"),
    fx!(Sora,35,"Aerial Finish effect 35"),fx!(Sora,36,"Aerial Finish effect 36"),
    fx!(Sora,37,"Aerial Finish effect 37"),fx!(Sora,38,"Aerial Finish effect 38"),
    fx!(Final,52,"Final first swing effect 52"),fx!(Final,53,"Final first swing effect 53"),
    fx!(Final,54,"Final first swing effect 54"),fx!(Final,55,"Final first swing effect 55"),
    fx!(Final,56,"Final first swing effect 56"),fx!(Final,57,"Final first swing effect 57"),
    fx!(Limit,26,"Sonic Rave effect 26"),fx!(Limit,27,"Sonic Rave effect 27"),fx!(Limit,28,"Sonic Rave effect 28"),
    fx!(Limit,29,"Sonic Rave Finish effect 29"),fx!(Limit,30,"Sonic Rave Finish effect 30"),fx!(Limit,31,"Sonic Rave Finish effect 31"),
    fx!(Limit,34,"Strike Raid catch flash",blade),fx!(Limit,20,"Infinity tip charge"),
    fx!(Sora,41,"Counterguard hand flash"),
];
pub fn get(id:u32)->Option<&'static Spec>{id.checked_sub(FIRST).and_then(|n|SPECS.get(n as usize))}
impl Spec{
    pub fn identifier(&self)->String{format!("KH2 {}: element {}",self.package.label(),self.element)}
    pub fn description(&self)->String{format!("{}. {}. Visual preview only.",self.name,self.identifier())}
}
//0 loading,1 ready,2 partial programs,3 missing package/element,4 no particle data,5 budget.
static STATUS:[AtomicU32;COUNT]=[const{AtomicU32::new(0)};COUNT];
pub fn status(id:u32)->u32{id.checked_sub(FIRST).and_then(|n|STATUS.get(n as usize)).map_or(3,|v|v.load(Ordering::Acquire))}
pub fn set_status(id:u32,value:u32){if let Some(v)=id.checked_sub(FIRST).and_then(|n|STATUS.get(n as usize)){v.store(value.min(5),Ordering::Release);}}
pub fn unavailable(){for v in &STATUS{v.store(3,Ordering::Release);}}

/// One selected element: show up to120 game frames, then60 clear frames.
/// Natural one-shot expiry is retained; no script/attack or sound is started.
#[derive(Clone,Copy,Default,Debug)]
pub struct Clock{frame:u16}
#[derive(Clone,Copy,Debug,PartialEq,Eq)]
pub enum Phase{Start,Hold,Stop}
impl Clock{
    pub fn reset(&mut self){self.frame=0;}
    pub fn advance(&mut self)->Phase{let action=match self.frame{0=>Phase::Start,120=>Phase::Stop,_=>Phase::Hold};self.frame=(self.frame+1)%180;action}
}
/// Keep the calibrated KH2 blade coordinates on the actual native grip, including
/// Type G's baked reverse grip; no native matrix is written.
pub fn blade_pose(grip:Mat4,bind_grip:Mat4,bind_blade:Mat4,world:Mat4)->Option<Mat4>{
    if ![grip,bind_grip,bind_blade,world].iter().all(|m|m.is_finite())||bind_grip.determinant().abs()<1e-6{return None;}
    let blade=world*grip*bind_grip.inverse()*bind_blade;
    (blade.is_finite()&&blade.w_axis.truncate().distance(world.w_axis.truncate())<300.).then_some(blade)
}
pub fn weapon_anchor(blade:Mat4,code:u16,blade_host:bool)->Option<Mat4>{
    let along=if blade_host{0.5}else{match code{0x4003|0x4004=>1.,0x4005|0x4006=>0.,0x4007|0x4008=>0.5,_=>return None,}};
    let point=blade*Mat4::from_translation(glam::Vec3::new(-78.*along,0.,0.));point.is_finite().then_some(point)
}

#[cfg(test)]mod tests{
    use super::*;
    #[test]fn all_repurposed_slots_have_distinct_named_package_element_pairs(){
        let pairs=SPECS.iter().map(|s|(s.package as usize,s.element)).collect::<std::collections::BTreeSet<_>>();assert_eq!(pairs.len(),COUNT);
        for id in FIRST..FIRST+COUNT as u32{let s=get(id).unwrap();assert!(s.name.len()<=34);assert!(s.identifier().len()<64);assert!(s.description().contains(&s.element.to_string()));assert!(s.package.path().ends_with(".a.us"));}
        assert!(get(65).is_none());assert!(get(105).is_none());assert_eq!(get(104).unwrap().element,41);
    }
    #[test]fn looping_and_one_shot_preview_budget_is_finite_and_restarts_without_overlap(){
        let mut c=Clock::default();let events=(0..540).filter_map(|f|{let p=c.advance();(p!=Phase::Hold).then_some((f,p))}).collect::<Vec<_>>();
        assert_eq!(events,[(0,Phase::Start),(120,Phase::Stop),(180,Phase::Start),(300,Phase::Stop),(360,Phase::Start),(480,Phase::Stop)]);
        c.reset();assert_eq!(c.advance(),Phase::Start);
    }
    #[test]fn grip_calibration_keeps_reverse_grip_and_weapon_root_tip_separate(){
        use glam::{Vec3,Quat};let world=Mat4::from_translation(Vec3::new(100.,20.,30.));let bind=Mat4::from_translation(Vec3::Y*10.);
        let blade=bind*Mat4::from_translation(Vec3::X*4.);let reverse=Mat4::from_rotation_translation(Quat::from_rotation_y(std::f32::consts::PI),Vec3::Y*10.);
        let b=blade_pose(reverse,bind,blade,world).unwrap();let root=weapon_anchor(b,0x4005,false).unwrap();let tip=weapon_anchor(b,0x4004,false).unwrap();
        assert!((root.w_axis.truncate()-Vec3::new(96.,30.,30.)).length()<0.001);assert!((tip.w_axis.truncate()-root.w_axis.truncate()-Vec3::X*78.).length()<0.001);
        assert!(weapon_anchor(b,101,false).is_none());assert!(blade_pose(reverse,Mat4::ZERO,blade,world).is_none());
    }
}
