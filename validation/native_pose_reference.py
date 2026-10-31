#!/usr/bin/env python3
"""Independent CPU reference used for v44 validation. Our own emulator harness;
no game code/assets are embedded. Requires the exact user-owned source hashes,
NumPy and Unicorn2.1.4. Only authored pose evaluation is exercised: identity
placement, no floor IK, no actor gameplay. Handle resolution uses private mapped
buffers; event queries/cookie checks are excluded. Other unsupported imports fail.
See README_SOLVER.txt for commands and the limits of this reference.
"""
from pathlib import Path
import sys,struct,collections,json,math,hashlib
from unicorn import Uc,UC_ARCH_X86,UC_MODE_64,UC_HOOK_CODE,UC_HOOK_MEM_INVALID
from unicorn.x86_const import *
import numpy as np
BASE=0x140000000
def u32(b,p):return struct.unpack_from('<I',b,p)[0]
class NativePose:
 def __init__(self,exe,model,bank):
  self.source_model=Path(model).read_bytes();self.source_bank=Path(bank).read_bytes()
  assert hashlib.sha256(Path(exe).read_bytes()).hexdigest()=='d790746245d26159f3ee0e1060e33b2fa2de06941850a4ac724f598722884bac','Reference executable version not verified'
  assert hashlib.sha256(self.source_model).hexdigest()=='ef243b6ffe6d5234a1c4b795946f82db34cafb5f427ab816c8090b89379d91e3','Reference model differs from captured main1160'
  assert hashlib.sha256(self.source_bank).hexdigest()=='b50be471d376786a80caabbdaf08e861985d0d957e914552dc98180aa6c4d2a8','Reference motion bank differs from captured main1160' 
  b=Path(exe).read_bytes();pe=u32(b,0x3c);opt=pe+24;n=struct.unpack_from('<H',b,pe+6)[0];opts=struct.unpack_from('<H',b,pe+20)[0]
  self.uc=uc=Uc(UC_ARCH_X86,UC_MODE_64);size=u32(b,opt+56);uc.mem_map(BASE,(size+4095)&~4095);uc.mem_write(BASE,b[:u32(b,opt+60)])
  for i in range(n):
   a=opt+opts+40*i;va,size,off=u32(b,a+12),u32(b,a+16),u32(b,a+20)
   if size:uc.mem_write(BASE+va,b[off:off+size])
  uc.mem_map(0x10000000,0x2000000);uc.mem_map(0x70000000,0x400000)
  self.imports={};a=u32(b,opt+112+8)
  def read32(p):return struct.unpack('<I',uc.mem_read(BASE+p,4))[0]
  def string(p):return bytes(uc.mem_read(BASE+p,128)).split(b'\0')[0].decode()
  for desc in range(0,4096,20):
   orig,_,_,dll,iat=struct.unpack('<IIIII',uc.mem_read(BASE+a+desc,20))
   if not dll:break
   for i in range(4096):
    f=struct.unpack('<Q',uc.mem_read(BASE+(orig or iat)+i*8,8))[0]
    if not f:break
    name=string(f+2)if f<2**63 else '#'+str(f&65535);stub=0x11000000+len(self.imports)*16;self.imports[stub]=name;uc.mem_write(BASE+iat+i*8,struct.pack('<Q',stub));uc.mem_write(stub,b'\xc3')
  uc.hook_add(UC_HOOK_CODE,self.import_call,begin=0x11000000,end=0x11010000)
  self.ptr=0x10010000;self.trace=collections.deque(maxlen=12)
  uc.hook_add(UC_HOOK_CODE,self.translate,begin=BASE+0x38adc0,end=BASE+0x38adc0)
  for at in [0x394770,0x34b4f0]:uc.hook_add(UC_HOOK_CODE,self.empty,begin=BASE+at,end=BASE+at)
  uc.hook_add(UC_HOOK_MEM_INVALID,self.badmem)
 def alloc(self,size):
  p=self.ptr;self.ptr=(p+size+255)&~255;assert self.ptr<0x12000000;return p
 def write(self,p,data):self.uc.mem_write(p,bytes(data))
 def p32(self,p,n):self.write(p,struct.pack('<I',n&0xffffffff))
 def p64(self,p,n):self.write(p,struct.pack('<Q',n))
 def ret(self,value=0):
  u=self.uc;sp=u.reg_read(UC_X86_REG_RSP);u.reg_write(UC_X86_REG_RAX,value);u.reg_write(UC_X86_REG_RIP,struct.unpack('<Q',u.mem_read(sp,8))[0]);u.reg_write(UC_X86_REG_RSP,sp+8)
 def import_call(self,u,a,size,data):
  name=self.imports[a]
  def f32(reg):return struct.unpack('<f',u.reg_read(reg).to_bytes(16,'little')[:4])[0]
  def f64(reg):return struct.unpack('<d',u.reg_read(reg).to_bytes(16,'little')[:8])[0]
  ops={'sqrt':math.sqrt,'sqrtf':math.sqrt,'sinf':math.sin,'cosf':math.cos,'tanf':math.tan,'atan2f':math.atan2,'acosf':math.acos,'asinf':math.asin,'sin':math.sin,'cos':math.cos,'atan2':math.atan2,'acos':math.acos}
  if name in ops:
   single=name.endswith('f');x=(f32 if single else f64)(UC_X86_REG_XMM0);args=[x]
   if name.startswith('atan2'):args.append((f32 if single else f64)(UC_X86_REG_XMM1))
   v=ops[name](*args);u.reg_write(UC_X86_REG_XMM0,int.from_bytes(struct.pack('<f'if single else '<d',v),'little'));self.ret();return
  raise RuntimeError('unhandled import '+name)
 def translate(self,u,a,s,d):self.ret(u.reg_read(UC_X86_REG_RCX)&0xffffffff)
 def empty(self,u,a,s,d):self.ret()
 def badmem(self,u,access,a,size,value,d):
  print('bad memory',access,hex(a),size,'pc',hex(u.reg_read(UC_X86_REG_RIP)),{n:hex(u.reg_read(r))for n,r in [('rcx',UC_X86_REG_RCX),('rdx',UC_X86_REG_RDX),('r8',UC_X86_REG_R8),('r9',UC_X86_REG_R9),('rax',UC_X86_REG_RAX)]});return False
 def setup(self,slot):
  b=self.source_model;mobj=u32(b,4);h=mobj+u32(b,mobj+32);self.n=u32(b,h);table=h+u32(b,h+4);self.bones=b[table:table+self.n*48]
  self.instance=ins=self.alloc(0x200);header=self.alloc(0x40);wrapper=self.alloc(8);self.p64(ins,wrapper);self.p64(wrapper,header);self.p32(header,self.n)
  bonearr=self.alloc(len(self.bones));self.write(bonearr,self.bones);self.p32(header+4,bonearr)
  params=self.alloc(0x500);self.p32(params+0x20,0xffffffff);self.p32(params+0x10,1);self.p32(header+8,params)
  self.srt=srt=self.alloc(self.n*64);self.world=world=self.alloc(self.n*64);self.local=local=self.alloc(self.n*64)
  for i in range(self.n):
   bone=self.bones[i*48:(i+1)*48];v=bytearray(64);v[:12]=bone[:12];v[16:28]=bone[:12];v[32:44]=bone[16:28];v[48:60]=bone[32:44];v[60:64]=struct.pack('<f',1);self.write(srt+i*64,v)
   self.write(world+i*64,np.eye(4,dtype='<f4').tobytes());self.write(local+i*64,np.eye(4,dtype='<f4').tobytes())
  for a,p in [(0x1b0,srt),(0x1b4,world),(0x1b8,local)]:self.p32(ins+a,p)
  b=self.source_bank;s=u32(b,4);table=s+64;m=table+u32(b,table+slot*4);nexts=[table+u32(b,table+i*4) for i in range(31)if table+u32(b,table+i*4)>m];end=min(nexts)if nexts else len(b)
  raw=bytearray(b[m:end]);self.motion=motion=self.alloc(len(raw))
  for at in [0x14,0x1c,0x24,0x28,0x30,0x38,0x3c,0x44,0x4c]:
   off=u32(raw,at)
   if off:struct.pack_into('<I',raw,at,motion+off)
  self.write(motion,raw);self.p64(ins+8,0)
  self.matrix=self.alloc(64);self.write(self.matrix,np.eye(4,dtype='<f4').tobytes())
 def run(self,frame):
  u=self.uc;sp=0x703fff08;self.p64(sp,0x10000000);u.reg_write(UC_X86_REG_RSP,sp);u.reg_write(UC_X86_REG_RCX,self.matrix);u.reg_write(UC_X86_REG_RDX,self.instance);u.reg_write(UC_X86_REG_XMM2,int.from_bytes(struct.pack('<f',frame),'little'));u.reg_write(UC_X86_REG_R9,self.motion)
  u.emu_start(BASE+0x391c70,0x10000000,count=2000000)
  if u.reg_read(UC_X86_REG_RIP)!=0x10000000:raise RuntimeError('instruction limit at '+hex(u.reg_read(UC_X86_REG_RIP)))
  return np.frombuffer(u.mem_read(self.world,self.n*64),dtype='<f4').reshape(self.n,4,4).transpose(0,2,1).copy()

import argparse,time
parser=argparse.ArgumentParser(description='Offline CPU reference for the captured Steam KH1/Dark Riku main1160 source; no game process or game state is used.')
for name in ['exe','model','bank','poses','output']:parser.add_argument('--'+name,required=True)
args=parser.parse_args()
data=Path(args.poses).read_bytes()
assert data[:8]==b'KH1POSE1';count=struct.unpack_from('<I',data,8)[0];at=12
flip=np.diag([1.,-1.,-1.,1.]).astype(np.float32);current=None;worst=[];samples=0;components=0;start=time.time()
for index in range(count):
 slot,frame,n,h=struct.unpack_from('<IfII',data,at);at+=16
 active=np.frombuffer(data,dtype=np.uint8,count=n,offset=at).astype(bool);at+=n
 ours=np.frombuffer(data,dtype='<f4',count=(n+h)*16,offset=at).reshape(n+h,4,4).transpose(0,2,1);at+=(n+h)*64
 root_motion=np.frombuffer(data,dtype='<f4',count=3,offset=at);at+=12
 if slot!=current:
  if current is not None:print(json.dumps(worst[-1]),flush=True)
  native=NativePose(args.exe,args.model,args.bank);native.setup(slot);current=slot;worst.append({'slot':slot,'samples':0,'active_bones':int(active.sum()),'max_position_error':0.,'max_basis_error':0.,'max_helper_error':0.,'max_root_error':0.,'worst_frame':0.})
 ref=native.run(frame);native_helpers=np.frombuffer(native.uc.mem_read(BASE+0x2ef1f50,h*64),dtype='<f4').reshape(h,4,4).transpose(0,2,1)
 expected=flip@ours;position=float(np.max(np.linalg.norm(ref[active,:3,3]-expected[:n][active,:3,3],axis=1)));basis=float(np.max(np.abs(ref[active,:3,:3]-expected[:n][active,:3,:3])));helpers=float(np.max(np.abs(native_helpers-expected[n:])))
 ref_root=np.frombuffer(native.uc.mem_read(native.instance+0x100,12),dtype='<f4');root_error=float(np.max(np.abs(ref_root-np.array([root_motion[0],-root_motion[1],-root_motion[2]]))))
 assert np.isfinite(ours).all()and np.isfinite(ref).all()
 r=worst[-1];r['samples']+=1
 if position>r['max_position_error']:r['worst_frame']=frame
 for field,value in [('max_position_error',position),('max_basis_error',basis),('max_helper_error',helpers),('max_root_error',root_error)]:r[field]=max(r[field],value)
 samples+=1;components+=(int(active.sum())+h)*16
 if position>0.03 or basis>0.003 or helpers>0.003 or root_error>0.003:raise AssertionError((slot,frame,position,basis,helpers,root_error))
assert at==len(data);print(json.dumps(worst[-1]),flush=True)
report={'source':'Steam KH1 native authored skeleton evaluator in isolated CPU emulation; transforms, static/keyed/helper data and authored constraints; no game renderer/floor IK/AI','space_conversion':'native = exact diag(1,-1,-1,1) * source-model solver','pose_count':samples,'clip_count':len(worst),'compared_float_components':components,'max_position_error':max(r['max_position_error']for r in worst),'max_basis_error':max(r['max_basis_error']for r in worst),'max_helper_error':max(r['max_helper_error']for r in worst),'max_root_error':max(r['max_root_error']for r in worst),'passed':True,'original_game_or_gpu_test':False,'seconds':time.time()-start,'source_sha256':{Path(p).name:hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in [args.model,args.bank]},'slots':worst}
Path(args.output).write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if k!='slots'}),flush=True)
