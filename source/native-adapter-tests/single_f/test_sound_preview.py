"""Focused final-PE menu checks without private animation-regeneration fixtures.

Uses the real supplied Steam executable and C adapter. Rust dispatch, GPU and
audio availability/playback are mocked; no Windows/game session is claimed.
"""
from pathlib import Path
import ctypes as C, importlib.util,json,os,re,struct,unittest

HERE=Path(__file__).resolve().parent
os.environ.setdefault('TERRA_SOURCE',str(HERE))
spec=importlib.util.spec_from_file_location('styles_native_host',HERE/'test_runtime.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
b=m.bridge
CAT=[('Infinity Tip Charge sound','KH2 Limit Form / element 20'),('Counterguard Hand Flash sound','KH2 Sora / element 41')]+[(f'KH2 sound {999000+i}',f'KH2 se999 / SE {999000+i}')for i in range(43)]
assert len(CAT)==45

class PreviewHost(m.Host):
 def __init__(self):
  self.game=m.allocate(0x3000000);b.bridge_reset(self.game);b.bridge_range(self.game,0x3000000,0x40);b.bridge_modes(0,0);self.buffers=[]
  # Seed the exact native image before installing C adapters. No original game
  # function runs here; UI leaves are replaced by the existing Win64 ABI host.
  data=Path(os.environ['KH1_EXE']).read_bytes();pe=struct.unpack_from('<I',data,60)[0];op=pe+24;sh=op+struct.unpack_from('<H',data,pe+20)[0]
  m.put(self.game,data[:struct.unpack_from('<I',data,op+60)[0]])
  for i in range(struct.unpack_from('<H',data,pe+6)[0]):
   vs,va,rs,rp=struct.unpack_from('<4I',data,sh+i*40+8)
   if rs and va+rs<=0x3000000:m.put(self.game+va,data[rp:rp+rs])
  self.actor=self.buffer(bytes(0x800));m.w32(self.actor+0x374,1);m.w64(self.game+0x2537e48,self.actor)
  self.save=self.game+0x2de9360;m.put(self.save,bytes(0x1000));m.put(self.save+4,b'\x64\x05\x0a');m.w64(self.game+0x2868ba0,self.save)
  self.load_pe();self.want=0;self.epoch=0
  self.adapter_ready=b.adapter_init(self.symbols['SingleFInit'],self.game,1)
  assert self.adapter_ready, b.bridge_log().decode()
  self.descriptions=[]
  for name,identifier in CAT:
   for line in [name,identifier,'Plays once at ground combo start']:
    self.descriptions.append(self.buffer(line.encode()+b'\0'))
  self.text_table=self.buffer(struct.pack('<'+'Q'*len(self.descriptions),*self.descriptions))
  self.status_code=self.buffer(b'\xb8\x01\x00\x00\x00\xc3')
  self.identifier_code=self.buffer(b'\xb8\xff\xff\xff\xff\xc3')
  b.call_ptr3(self.symbols['SoundPreviewInit'],self.text_table,self.status_code,self.identifier_code)
 def status(self,value):m.w32(self.status_code+1,value)
 def help_lines(self):
  return [([b.bridge_menu_plain_word(i,j) for j in range(4)],C.string_at(b.bridge_menu_plain_text(i))) for i in range(b.bridge_menu_plain_count()) if b.bridge_menu_plain_word(i,0)==174]

class SoundPreviewTests(unittest.TestCase):
 def test_every_sound_has_exact_name_identifier_and_three_bounded_footer_lines(self):
  h=PreviewHost();_,page=h.passive_setup([6,117])
  for i,(name,identifier) in enumerate(CAT):
   text=h.ui_choose(page,1+i);self.assertIn(name,text);self.assertIn(identifier,text)
   rows=h.help_lines();self.assertEqual([v[1] for v,t in rows],[309,327,345]);self.assertEqual(len(rows),3)
   self.assertTrue(all(10<=v[2]<=16 and v[1]+v[2]<=361 for v,t in rows));self.assertIn('AP Used|3 / 30',text)
   for v,t in rows:
    encoded=C.create_string_buffer(t);self.assertLessEqual(b.call_ptr2(h.game+0x2d0e10,C.addressof(encoded),v[2]),226)
 def test_selection_is_exclusive_and_never_requests_old_body_profiles(self):
  h=PreviewHost();_,page=h.passive_setup([6,117]);before=C.string_at(h.save,0x1000);actor=C.string_at(h.actor,0x800)
  for i in range(45):
   h.ui_choose(page,1+i);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),66+i)
   self.assertEqual(m.r64(h.symbols['numbered_bits']),1<<i)
   self.assertEqual(b.call_int0(h.symbols['WeaponFxChoice']),0);self.assertEqual(b.call_int0(h.symbols['VentusTestChoice']),0);self.assertEqual(b.call_int0(h.symbols['DarkTestChoice']),0)
   self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(C.string_at(h.actor,0x800),actor)
  h.ui_choose(page,45);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),0)
 def test_preview_keeps_each_equipped_stance_and_native_ap(self):
  for stance in [124,123,120,119,117,116,115,126,125,121,118,122]:
   h=PreviewHost();_,page=h.passive_setup([6,0x87,stance]);before=C.string_at(h.save,0x1000)
   h.ui_choose(page,2);self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(h.ability_count(stance),1)
   self.assertEqual(b.call_ptr1(h.game+0x2e8660,0),27);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),66)
 def test_stance_changes_keep_preview_and_reserved_flags(self):
  for row in range(12):
   h=PreviewHost();_,page=h.passive_setup([6,117]);h.numbered_init((1<<50)|1)
   h.ui_page_frame(page,0x40);h.ui_page_frame(page,0x1000);h.ui_page_frame(page,0x20);h.ui_choose(page,row)
   self.assertEqual(m.r64(h.symbols['numbered_bits']),(1<<50)|1);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),66)
   h.intrinsic_frame();self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),66)
 def test_readiness_labels_follow_runtime_status_without_losing_identifier(self):
  h=PreviewHost();_,page=h.passive_setup([6]);h.ui_choose(page,1)
  for status,label in [(0,'Loading KH2 sound'),(1,'Plays once at ground combo start'),(2,'No playable sound assigned'),(3,'KH2 archive or sound bank missing'),(4,'Sound cannot be decoded'),(5,'Sound exceeds preview budget')]:
   h.status(status);text=h.ui_page_frame(page);self.assertIn(label,text);self.assertIn('KH2 Limit Form / element 20',text)
 def test_numbered_flags_and_passive_rows_retain_full_capacity(self):
  h=PreviewHost();_,page=h.passive_setup([6]*48);before=C.string_at(h.save,0x1000)
  for i in range(50):h.ui_choose(page,48+i)
  self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(m.r64(h.symbols['numbered_bits']),(m.ALL_NUMBERED&~m.TEST_MASK)|(1<<44))
  self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),110);self.assertEqual(C.c_ushort.from_address(page+0xf8).value,98)
 def test_unequip_and_removal_stop_active_preview_query(self):
  h=PreviewHost();_,page=h.passive_setup([6]);h.ui_choose(page,1);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),66)
  b.call_void1(h.symbols['SoundPreviewEnable'],0);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),0)
  b.call_void1(h.symbols['SoundPreviewEnable'],1);self.assertEqual(b.call_int0(h.symbols['SoundPreviewChoice']),66)
 def test_resolved_package_sound_identifier_is_bounded_and_disappears_when_unassigned(self):
  h=PreviewHost();_,page=h.passive_setup([6]);h.ui_choose(page,1)
  m.w32(h.identifier_code+1,999038);text=h.ui_page_frame(page);self.assertIn('element 20 / SE 999038',text)
  m.w32(h.identifier_code+1,0xffffffff);text=h.ui_page_frame(page);self.assertNotIn('/ SE 999038',text)
 def test_native_ability_help_and_ap_budget_are_unchanged(self):
  h=PreviewHost();_,page=h.passive_setup([0x86,0x87,117]);text=h.ui_page_frame(page);self.assertIn('Native help.',text);self.assertIn('AP Used|0 / 30',text)
  self.assertIn('AP Used|3 / 30',h.ui_choose(page,0));self.assertIn('AP Used|5 / 30',h.ui_choose(page,1))
 def test_original_overdrive_metadata_and_header_remain(self):
  h=PreviewHost();_,page=h.passive_setup([6,117]);h.ui_page_frame(page,0x40);text=h.ui_page_frame(page,0x4000)
  self.assertIn('Control|Drain|5',text);self.assertNotIn('AP Used',text)
  h.ui_page_frame(page,0x20);h.ui_choose(page,8);self.assertEqual(b.call_int0(h.symbols['OverdriveChoice']),5)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(SoundPreviewTests))
 report=dict(passed=result.wasSuccessful(),tests=result.testsRun,failures=len(result.failures),errors=len(result.errors),executed_final_integrated_pe_c_adapter=True,native_menu_references_checked_against_supplied_executable=True,private_animation_fixtures_required=False,rust_audio_dispatch_and_playback_mocked=True,windows_or_game_executed=False)
 Path(os.environ.get('VALIDATION_OUT',str(HERE/'sound_preview_validation.json'))).write_text(json.dumps(report,indent=2)+'\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)
