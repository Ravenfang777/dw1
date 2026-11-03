"""Run the final combined PE's C adapter with Win64 ABI mocks on Linux.

Rust DllMain, shared Rust dispatch and rendering are not executed. Private
source fixtures are provided through the documented environment variables.
"""
from pathlib import Path
import ctypes as C,json,struct,subprocess,sys,unittest,os
ROOT=Path(os.environ['AQUA_SOURCE']).resolve()
TEST_ROOT=Path(__file__).resolve().parent
subprocess.run(['gcc','-std=c11','-O2','-shared','-fPIC',str(TEST_ROOT/'test_bridge.c'),'-o',str(TEST_ROOT/'test_bridge.so'),'-lm'],cwd=ROOT,check=True)
bridge=C.CDLL(str(TEST_ROOT/'test_bridge.so'))
for name,args,ret in [('bridge_reset',[C.c_size_t],None),('bridge_range',[C.c_size_t,C.c_size_t,C.c_uint],None),('bridge_modes',[C.c_int,C.c_int],None),('bridge_log',[],C.c_char_p),('bridge_queries',[],C.c_uint),('bridge_encode',[C.c_size_t],C.c_uint),('bridge_symbol',[C.c_char_p],C.c_size_t),('bridge_call0',[C.c_size_t],None),('bridge_init',[C.c_size_t],None)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
for name,args,ret in [('bridge_magic_modes',[C.c_int,C.c_int,C.c_int],None),('bridge_matrix',[C.c_size_t,C.c_size_t,C.c_uint,C.POINTER(C.c_float)],None),('bridge_point',[C.c_size_t,C.c_size_t,C.c_uint,C.c_float,C.POINTER(C.c_float)],None),('bridge_matrix_code',[],C.c_uint),('bridge_point_code',[],C.c_uint),('bridge_point_fraction',[],C.c_float)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
for name,args,ret in [('bridge_air_modes',[C.c_int,C.c_uint],None),('bridge_control',[C.c_size_t,C.c_size_t,C.c_size_t],None),('bridge_control_calls',[],C.c_uint),('bridge_control_word',[C.c_uint],C.c_uint),('bridge_queue_calls',[],C.c_uint),('bridge_commit',[C.c_size_t],None),('bridge_native_glide_calls',[],C.c_uint),('bridge_glide',[C.c_size_t,C.c_size_t],None),('bridge_event',[C.c_size_t,C.c_size_t,C.c_uint,C.c_float],C.c_size_t)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
bridge.bridge_move.argtypes=[C.c_size_t,C.c_size_t,C.POINTER(C.c_float)];bridge.bridge_move.restype=C.c_float
bridge.bridge_move_calls.argtypes=[];bridge.bridge_move_calls.restype=C.c_uint
bridge.bridge_guard_row.argtypes=[C.c_size_t,C.c_size_t,C.c_uint];bridge.bridge_guard_row.restype=C.c_size_t
bridge.bridge_motion_advance.argtypes=[C.c_size_t,C.c_size_t,C.c_float];bridge.bridge_motion_advance.restype=C.c_size_t
bridge.bridge_guard_angle.argtypes=[C.c_size_t,C.c_size_t,C.c_size_t];bridge.bridge_guard_angle.restype=C.c_int
bridge.bridge_guard_pool.argtypes=[C.c_size_t];bridge.bridge_guard_pool.restype=C.c_int
bridge.bridge_glide_eligible.argtypes=[C.c_int];bridge.bridge_glide_eligible.restype=None
bridge.bridge_motion_delta.argtypes=[];bridge.bridge_motion_delta.restype=C.c_float
libc=C.CDLL(None);libc.mmap.argtypes=[C.c_void_p,C.c_size_t,C.c_int,C.c_int,C.c_int,C.c_long];libc.mmap.restype=C.c_void_p

libc.munmap.argtypes=[C.c_void_p,C.c_size_t];libc.munmap.restype=C.c_int
allocation_sizes={}
def allocate(n):
    addr=libc.mmap(None,n,7,0x22,-1,0)
    if addr in [None,C.c_void_p(-1).value]:raise OSError('mmap failed')
    allocation_sizes[int(addr)]=n
    return int(addr)
def put(p,data):C.memmove(p,bytes(data),len(data))
def r32(p):return C.c_uint.from_address(p).value
def r64(p):return C.c_uint64.from_address(p).value
def w32(p,v):C.c_uint.from_address(p).value=v
def w64(p,v):C.c_uint64.from_address(p).value=v

class Host:
    def __del__(self):
        for address in getattr(self,'buffers',[])+[getattr(self,'game',0),getattr(self,'image',0)]:
            size=allocation_sizes.pop(address,0)
            if size:libc.munmap(address,size)
    def __init__(self,slot=98,encoded_fields=False,stamp=1721645006,remove=0,conflict=0,magic=False,hand_magic=1,fail_alloc=0,fail_protect=0,air=False,air_dodge=1,control_mode=0,guard=False,jump=False):
        self.game=allocate(0x3000000);bridge.bridge_reset(self.game);bridge.bridge_range(self.game,0x3000000,0x40);bridge.bridge_modes(remove,conflict)
        w32(self.game+60,0x80);w32(self.game+0x80,0x4550);w32(self.game+0x88,stamp);put(self.game+0x233fbdc,struct.pack('<f',1.))
        self.buffers=[]
        self.actor=self.buffer(bytes(0x800));w32(self.actor+0x374,1);w64(self.game+0x2537e48,self.actor)
        self.save=self.game+0x2de9360;put(self.save+4,b'\x64\x05\x0a');put(self.save+0x44,b'\x81\x82\x00')
        self.native_table=bytes((i*7)%256 for i in range(65*12));self.original_table=self.buffer(self.native_table);w64(self.game+0x2d36d48,self.original_table)
        put(self.game+0x394770,(ROOT/'fixtures/native_event_at.bin').read_bytes())
        put(self.game+0x38adc0,b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(b'NativeDecode'))+b'\xff\xe0')
        self.all_records=json.loads((ROOT/'curve_validation.json').read_text())['motions']
        self.activate_bank(slot==60,encoded_fields)
        # Native pointer-to-handle helper uses the ABI of the existing reference.
        put(self.game+0x38ad90,b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(b'NativeHandle'))+b'\xff\xe0')
        bridge.bridge_magic_modes(hand_magic,fail_alloc,fail_protect)
        if magic:
            self.matrix_prefix=bytes.fromhex('48895c24084889742410574883ec20')
            self.point_prefix=bytes.fromhex('405355574881ec800000000f29742460')
            call=lambda n:b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(n))+b'\xff\xd0'
            put(self.game+0x29ea00,self.matrix_prefix+call(b'NativeMatrix')+bytes.fromhex('4883c4205f488b5c2408488b742410c3'))
            put(self.game+0x29eb20,self.point_prefix+call(b'NativePoint')+bytes.fromhex('0f287424604881c4800000005f5d5bc3'))
        bridge.bridge_air_modes(air_dodge,control_mode)
        self.dir=self.buffer(bytes(16))
        if air:
            self.glide_work=self.buffer(bytes(0x200));w32(self.actor+0x148,bridge.bridge_encode(self.glide_work));w32(self.glide_work+0x104,1)
            self.control_prefix=bytes.fromhex('48895c2418574883ec40488b0557e82a00')
            self.queue_prefix=bytes.fromhex('48895c2408574883ec20488bf9')
            call=lambda n:b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(n))+b'\xff\xd0'
            put(self.game+0x2a6220,self.control_prefix+call(b'NativeControl')+bytes.fromhex('4883c4405f488b5c2418c3'))
            put(self.game+0x29f980,self.queue_prefix+call(b'NativeQueue')+bytes.fromhex('4883c4205f488b5c2408c3'))
            put(self.game+0x2b26c0,(ROOT/'fixtures/native_glide_constructor.bin').read_bytes())
            self.glide_common_prefix=bytes.fromhex('40534883ec20488bd98b8948010000')
            put(self.game+0x2b2d30,self.glide_common_prefix+bytes.fromhex('4889d9')+call(b'NativeGlideCommon')+bytes.fromhex('4883c4205bc3'))
            super_constructor=bytearray((ROOT/'fixtures/native_glide_constructor.bin').read_bytes())
            struct.pack_into('<i',super_constructor,10,0x2b2d30-(0x2b2750+14));struct.pack_into('<i',super_constructor,25,0x38adc0-(0x2b2750+29));super_constructor[0x1d:0x24]=bytes.fromhex('83880401000001')
            put(self.game+0x2b2750,bytes(super_constructor))
            put(self.game+0x29fa30,self.queue_prefix+call(b'NativeAppend')+bytes.fromhex('4883c4205f488b5c2408c3'))
            self.move_prefix=bytes.fromhex('48895c2410574883ec40f70100100000')
            put(self.game+0x2af6a0,self.move_prefix+call(b'NativeMove')+bytes.fromhex('4883c4405f488b5c2410c3'))
            self.state_prefix=bytes.fromhex('48895c2410574883ec2048634170')
            put(self.game+0x2b1960,self.state_prefix+call(b'NativeSetState')+bytes.fromhex('4883c4205f488b5c2410c3'))
            put(self.game+0x297870,bytes.fromhex('f601047518f6818800000020750ff68144040000017506b801000000c333c0c3'))
        if guard:
            call=lambda n:b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(n))+b'\xff\xd0'
            put(self.game+0x2a3980,bytes.fromhex('48895c240848896c24104889742418')+bytes.fromhex('574883ec20')+call(b'NativeGuardRow')+bytes.fromhex('4883c4205f488b5c2408488b6c2410488b742418c3'))
            put(self.game+0x29f0a0,bytes.fromhex('405557488d6c24e84881ec18010000')+call(b'NativeMotionAdvance')+bytes.fromhex('4881c4180100005f5dc3'))
            put(self.game+0x2b4640,bytes.fromhex('4c8bdc49895b20574881eca0000000')+call(b'NativeGuardAngle')+bytes.fromhex('4881c4a00000005f488b5c2420c3'))
            put(self.game+0x2b47a0,bytes.fromhex('48896c241048897424185741564157')+bytes.fromhex('4883ec20')+call(b'NativeGuardPool')+bytes.fromhex('4883c420415f415e5f488b6c2410488b742418c3'))
            put(self.game+0x2b3270,bytes.fromhex('48895c2408574883ec20488bf9')+call(b'NativeGuardCreate')+bytes.fromhex('4883c4205f488b5c2408c3'))
            put(self.game+0x2b3560,bytes.fromhex('4883ec2883b9b400000000')+call(b'NativeGuardFree')+bytes.fromhex('4883c428c3'))
            # Preserve native RIP-relative anchor; the following ABI mock returns the mask.
            put(self.game+0x2b3760,bytes.fromhex('8b15aa3fb00233c9')+b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(b'NativeGuardMask'))+b'\xff\xe0')
        if jump:
            assert air
            put(self.game+0x2afda0,(ROOT/'fixtures/native_jump_launch.bin').read_bytes())
            put(self.game+0x2af530,(ROOT/'fixtures/native_jump_curve.bin').read_bytes())
            for rva,raw in json.loads((ROOT/'fixtures/native_jump_constants.json').read_text()).items():put(self.game+int(rva,16),bytes.fromhex(raw))
            put(self.game+0x38503e,bytes.fromhex('f30f51c0c3')) # sqrtf SSE stub
            put(self.game+0x3850f2,b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(b'NativeSinf'))+b'\xff\xe0')
            put(self.game+0x386ad0,bytes.fromhex('0f10020f1101c3')) # exact native vector copy
            put(self.game+0x2af630,b'\xc3') # queue/animation handoff is outside this arc sample
            self.jump_stats=self.buffer(bytes(0xe4));w32(self.actor+0x6c,bridge.bridge_encode(self.jump_stats))
        self.load_pe()
    def activate_bank(self,olympus,encoded_fields=False):
        self.slot=60 if olympus else 98
        self.records=[r for r in self.all_records if not olympus or r['olympus_slot']!=0xffffffff]
        self.record_by_slot={r['normal_slot']:r for r in self.records}
        raw={r['normal_slot']:(ROOT/f"fixtures/original_{r['fixture_stem']}.bin").read_bytes() for r in self.records}
        packed=bytearray();offsets={}
        for record in self.records:
            key=record['normal_slot'];packed.extend(bytes((-len(packed))%16));offsets[key]=len(packed);packed.extend(raw[key])
        glide_raw={slot:(ROOT/f'fixtures/native_glide_s{slot:03}.bin').read_bytes() for slot in range(75,79)}
        glide_offsets={}
        for slot,data in glide_raw.items():
            packed.extend(bytes((-len(packed))%16));glide_offsets[slot]=len(packed);packed.extend(data)
        control=(ROOT/'fixtures/control_native_s105.bin').read_bytes();packed.extend(bytes((-len(packed))%16));control_offset=len(packed);packed.extend(control)
        region=self.buffer(bytes(packed));self.unmapped=region+control_offset;self.unmapped_original=control
        self.array=self.buffer(bytes(128*4));self.motions={};self.runtime_originals={}
        for record in self.records:
            key=record['normal_slot'];motion=region+offsets[key];data=raw[key]
            if encoded_fields:
                for off in [20,28,36,40,48,56,60,68,76]:
                    value=r32(motion+off)
                    if value and value<len(data):w32(motion+off,bridge.bridge_encode(motion+value))
            if encoded_fields:
                event_at=struct.unpack_from('<I',data,60)[0]
                while struct.unpack_from('<I',data,event_at)[0]!=0xffffffff:
                    offset=struct.unpack_from('<I',data,event_at+8)[0];w32(motion+event_at+8,bridge.bridge_encode(motion+offset));event_at+=12
            self.motions[key]=motion;self.runtime_originals[key]=C.string_at(motion,len(data))
            slot=record['olympus_slot'] if olympus else record['normal_slot'];w32(self.array+slot*4,bridge.bridge_encode(motion))
        self.native_glide_motions={};self.native_glide_originals={}
        for slot,data in glide_raw.items():
            motion=region+glide_offsets[slot]
            if encoded_fields:
                for off in [20,28,36,40,48,56,60,68,76]:
                    value=r32(motion+off)
                    if value and value<len(data):w32(motion+off,bridge.bridge_encode(motion+value))
                at=struct.unpack_from('<I',data,60)[0]
                while struct.unpack_from('<I',data,at)[0]!=0xffffffff:
                    value=struct.unpack_from('<I',data,at+8)[0];w32(motion+at+8,bridge.bridge_encode(motion+value));at+=12
            self.native_glide_motions[slot]=motion;self.native_glide_originals[slot]=C.string_at(motion,len(data))
            w32(self.array+(slot-38 if olympus else slot)*4,bridge.bridge_encode(motion))
        w32(self.array+(67 if olympus else 105)*4,bridge.bridge_encode(self.unmapped))
        self.motion=self.motions[98];self.original_motion=raw[98]
        self.native_reactions={}
        for row in json.loads((ROOT/'fixtures/native_reactions.json').read_text()):
            key=row['normal_slot'];data=(ROOT/f'fixtures/native_reaction_s{key:03}.bin').read_bytes();motion=self.buffer(data)
            if encoded_fields:
                for off in [20,28,36,40,48,56,60,68,76]:
                    value=r32(motion+off)
                    if value and value<len(data):w32(motion+off,bridge.bridge_encode(motion+value))
                at=struct.unpack_from('<I',data,60)[0]
                while struct.unpack_from('<I',data,at)[0]!=0xffffffff:
                    value=struct.unpack_from('<I',data,at+8)[0];w32(motion+at+8,bridge.bridge_encode(motion+value));at+=12
            self.native_reactions[key]=(motion,C.string_at(motion,len(data)))
            w32(self.array+(row['olympus_slot'] if olympus else key)*4,bridge.bridge_encode(motion))
        self.key_offset=struct.unpack_from('<I',raw[98],40)[0];self.runtime_original=self.runtime_originals[98]
        w32(self.actor+0x1d4,bridge.bridge_encode(self.array))
        self.request_original=(ROOT/f"fixtures/requests_{'he' if olympus else 'normal'}_original.bin").read_bytes()
        self.requests=self.buffer(self.request_original)
        self.original_request_handle=bridge.bridge_encode(self.requests)
        w32(self.actor+0x1d8,self.original_request_handle)
    def buffer(self,data):
        p=allocate((len(data)+4095)&~4095);put(p,data);bridge.bridge_range(p,len(data),4);self.buffers.append(p);return p
    def load_pe(self):
        dll=ROOT/'kh1-aqua.dll'
        if not dll.exists():dll=ROOT.parent/'dll/kh1-aqua.dll'
        data=dll.read_bytes();pe=struct.unpack_from('<I',data,60)[0];n=struct.unpack_from('<H',data,pe+6)[0];op=pe+24
        preferred=struct.unpack_from('<Q',data,op+24)[0];size=struct.unpack_from('<I',data,op+56)[0];headers=struct.unpack_from('<I',data,op+60)[0]
        p=allocate(size);self.image=p;bridge.bridge_range(p,size,0x40);put(p,data[:headers])
        sh=op+struct.unpack_from('<H',data,pe+20)[0]
        for i in range(n):
            s=sh+i*40;vs,va,rs,rp=struct.unpack_from('<4I',data,s+8)
            if rs:put(p+va,data[rp:rp+rs])
        directory=op+112
        reloc,size_reloc=struct.unpack_from('<II',data,directory+5*8);assert reloc and size_reloc
        offset=0
        while offset<size_reloc:
            page,span=struct.unpack('<II',C.string_at(p+reloc+offset,8))
            for at in range(8,span,2):
                item=C.c_ushort.from_address(p+reloc+offset+at).value
                if item>>12==10:
                    q=p+page+(item&4095);w64(q,(r64(q)+p-preferred)&0xffffffffffffffff)
                else:assert item>>12==0
            offset+=span
        imp=r32(p+directory+8)
        while r32(p+imp):
            ilt=r32(p+imp);iat=r32(p+imp+16);index=0
            while r64(p+ilt+index*8):
                name_rva=r64(p+ilt+index*8);name=C.string_at(p+name_rva+2);address=bridge.bridge_symbol(name);assert address,name
                w64(p+iat+index*8,address);index+=1
            imp+=20
        export=r32(p+directory);count=r32(p+export+24);functions=r32(p+export+28);names=r32(p+export+32);ordinals=r32(p+export+36)
        self.exports={}
        for i in range(count):
            name=C.string_at(p+r32(p+names+i*4)).decode();ordinal=C.c_ushort.from_address(p+ordinals+i*2).value
            self.exports[name]=p+r32(p+functions+ordinal*4)
        assert set(self.exports)=={'OnInit','OnFrame','DllMain'}
        bridge.bridge_init(self.exports['OnInit'])
    def frame(self):bridge.bridge_call0(self.exports['OnFrame'])
    def abilities(self):return C.string_at(self.save+0x44,48)
    def equip(self,on,profile=0):
        id_=117+profile;data=bytearray(self.abilities());i=next(i for i,v in enumerate(data) if v&127==id_);data[i]=id_ if on else id_|128;put(self.save+0x44,bytes(data))
    def decode(self,h):return r64(self.game+0x2ee3980+((h&0x7fffffff)>>25)*8)+(h&0x1ffffff)
    def body(self,slot=98):return C.string_at(self.motions[slot],len(self.runtime_originals[slot]))
    def expected(self,slot,on):
        r=self.record_by_slot[slot];folder=ROOT/'fixtures'
        if int(on)>1:
            candidate=ROOT/f'sets/p{int(on)-1}/fixtures'
            if (candidate/f"aqua_{r['fixture_stem']}.bin").exists():folder=candidate
        data=bytearray((folder/f"{'aqua' if on else 'original'}_{r['fixture_stem']}.bin").read_bytes())
        data[:80]=self.runtime_originals[slot][:80]
        event_at=struct.unpack_from('<I',(ROOT/f"fixtures/original_{r['fixture_stem']}.bin").read_bytes(),60)[0]
        while struct.unpack_from('<I',data,event_at)[0]!=0xffffffff:
            data[event_at+8:event_at+12]=self.runtime_originals[slot][event_at+8:event_at+12];event_at+=12
        return bytes(data)
    def assert_all(self,test,on):
        for r in self.records:test.assertEqual(self.body(r['normal_slot']),self.expected(r['normal_slot'],on),r['action'])
        active=self.decode(r32(self.actor+0x1d8))
        variant='main' if int(on)==1 else 'aqua' if on else 'original'
        wanted=(ROOT/f"fixtures/requests_{'he' if self.slot==60 else 'normal'}_{variant}.bin").read_bytes()
        test.assertEqual(C.string_at(active,len(wanted)),wanted)
        test.assertEqual(C.string_at(self.requests,len(self.request_original)),self.request_original)
        if not on:test.assertEqual(r32(self.actor+0x1d8),self.original_request_handle)
    def snapshot(self):return {r['normal_slot']:self.body(r['normal_slot']) for r in self.records}
    def matrix(self,actor=None,code=0x30):
        out=(C.c_float*16)();bridge.bridge_matrix(self.game+0x29ea00,self.actor if actor is None else actor,code,out);return list(out)
    def point(self,actor=None,code=0x30,fraction=.75):
        out=(C.c_float*4)();bridge.bridge_point(self.game+0x29eb20,self.actor if actor is None else actor,code,fraction,out);return list(out)

    def control(self,down=0,pressed=0,state=2,request=6,height=100,tilt=0,x=0,z=0,actor=None):
        a=self.actor if actor is None else actor
        w32(a+0x70,state);w32(a+0x164,request);put(a+0x3d4,struct.pack('<f',height))
        for field in [4,8,16,20]:w32(self.game+0x298ca90+field,(down if field in [4,16] else pressed))
        put(self.dir,struct.pack('<4f',x,0,z,tilt))
        bridge.bridge_control(self.game+0x2a6220,a,self.dir)
    def move(self,dt=1.):
        put(self.game+0x233fbdc,struct.pack('<f',dt));out=self.buffer(bytes(16))
        result=bridge.bridge_move(self.game+0x2af6a0,self.actor,C.cast(out,C.POINTER(C.c_float)))
        return list((C.c_float*4).from_address(out)),result
    def blizzard_body(self,slot):
        data=bytearray((ROOT/f'blizzard/fixtures/aqua_s{slot:03}.bin').read_bytes());data[:80]=self.runtime_originals[slot][:80]
        at=struct.unpack_from('<I',(ROOT/f'blizzard/fixtures/aqua_s{slot:03}.bin').read_bytes(),60)[0]
        while struct.unpack_from('<I',data,at)[0]!=0xffffffff:
            data[at+8:at+12]=self.runtime_originals[slot][at+8:at+12];at+=12
        return bytes(data)
    def dodge_body(self):
        data=bytearray((ROOT/'dodge/fixtures/aqua_s010.bin').read_bytes());data[:80]=self.runtime_originals[10][:80];return bytes(data)
    def event(self,slot,kind,frame,track=0):
        p=bridge.bridge_event(self.game+0x394770,self.motions[slot],(kind<<16)|track,frame)
        return None if not p else r32(p+4)
    def native_glide(self):bridge.bridge_glide(self.game+0x2b26c0,self.actor)
    def queue(self,request,frame=0):
        w32(self.actor+0x178,1);w32(self.actor+0x17c,request);put(self.actor+0x184,struct.pack('<f',frame))
    def clock(self,value):put(self.actor+0x16c,struct.pack('<f',value))
    def arm_air(self,profile=0):
        self.frame();self.equip(True,profile);self.frame();self.control(state=0,request=0,height=0)
        self.control(state=2,request=6)


BaseHost=Host
for name,args,ret in [
    ('single_e_init',[C.c_size_t,C.c_size_t,C.c_int],C.c_int),
    ('single_e_frame',[C.c_size_t,C.c_size_t,C.c_int,C.c_uint64],C.c_int),
    ('single_e_config',[C.c_size_t]*7,None),
    ('single_e_shared',[C.c_uint],C.c_size_t)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
DLL=Path(os.environ['STYLES_DLL']).resolve()
class Host(BaseHost):
    def __init__(self,*args,**kwargs):
        kwargs.update(air=True,guard=True,jump=True)
        self.want=0;self.epoch=0;self.clean=True
        super().__init__(*args,**kwargs)
    def load_pe(self):
        data=DLL.read_bytes();pe=struct.unpack_from('<I',data,60)[0];op=pe+24
        n=struct.unpack_from('<H',data,pe+6)[0];preferred=struct.unpack_from('<Q',data,op+24)[0]
        size=struct.unpack_from('<I',data,op+56)[0];headers=struct.unpack_from('<I',data,op+60)[0]
        p=allocate(size);self.image=p;bridge.bridge_range(p,size,0x40);put(p,data[:headers])
        sh=op+struct.unpack_from('<H',data,pe+20)[0];sections=[]
        for i in range(n):
            s=sh+i*40;vs,va,rs,rp=struct.unpack_from('<4I',data,s+8);sections.append(va)
            if rs:put(p+va,data[rp:rp+rs])
        directory=op+112;reloc,rs=struct.unpack_from('<II',data,directory+5*8);offset=0
        while offset<rs:
            page,span=struct.unpack('<II',C.string_at(p+reloc+offset,8))
            for at in range(8,span,2):
                v=C.c_ushort.from_address(p+reloc+offset+at).value
                if v>>12==10:
                    q=p+page+(v&4095);w64(q,(r64(q)+p-preferred)&0xffffffffffffffff)
                else:assert v>>12==0
            offset+=span
        # No Rust DllMain/OnInit is run in this Linux harness. C uses injected APIs.
        # Retain the uncalled IAT as data; native kernel operations are Win64 mocks.
        symoff,count=struct.unpack_from('<II',data,pe+12);strings=symoff+count*18;symbols={};i=0
        while i<count:
            at=symoff+i*18;name=data[at:at+8]
            if name[:4]==bytes(4):
                start=strings+struct.unpack_from('<I',name,4)[0];name=data[start:data.index(0,start)]
            else:name=name.rstrip(b'\0')
            value,section=struct.unpack_from('<Ih',data,at+8)
            if section>0:symbols[name.decode(errors='replace')]=p+sections[section-1]+value
            i+=1+data[at+17]
        self.ffi={k:symbols[k] for k in ['SingleEInit','SingleEFrame','SingleEControl','SingleEGuardRow','SingleESuppressGlide','SingleESuperglide','SingleEMove']}
        self.shared_before={r:C.string_at(self.game+r,l) for r,l in [(0x2a6220,17),(0x2a3980,15),(0x2b26c0,14),(0x2b2750,14)]}
        self.adapter_ready=bridge.single_e_init(self.ffi['SingleEInit'],self.game,1)
        self.shared_after={r:C.string_at(self.game+r,len(v)) for r,v in self.shared_before.items()}
        self.install_shared_mock()
    def install_shared_mock(self):
        originals=[]
        for rva in [0x2b26c0,0x2b2750]:
            raw=bytearray(C.string_at(self.game+rva,42));trampoline=self.buffer(bytes(64))
            for off in [9,24]:
                target=self.game+rva+off+5+struct.unpack_from('<i',raw,off+1)[0]
                struct.pack_into('<i',raw,off+1,target-(trampoline+off+5))
            put(trampoline,raw);originals.append(trampoline)
        bridge.single_e_config(self.ffi['SingleEControl'],self.ffi['SingleEGuardRow'],self.ffi['SingleESuppressGlide'],self.ffi['SingleESuperglide'],*originals,self.ffi['SingleEMove'])
        for index,rva in enumerate([0x2a6220,0x2a3980,0x2b26c0,0x2b2750,0x2af6a0]):
            put(self.game+rva,b'\x48\xb8'+struct.pack('<Q',bridge.single_e_shared(index))+b'\xff\xe0')
    def equip(self,on,profile=0):
        assert profile==0,'Single E imports main Aqua only'
        self.want=bool(on)
    def frame(self,epoch=None):
        self.epoch=self.epoch+1 if epoch is None else epoch
        self.clean=bool(bridge.single_e_frame(self.ffi['SingleEFrame'],self.actor,self.want,self.epoch))
        return self.clean

class RuntimeTests(unittest.TestCase):
    def test_main_guard_runs_the_complete_forward_reverse_at_thirty_source_fps(self):
        h=Host(guard=True,encoded_fields=True);h.frame();h.equip(True);h.frame()
        self.assertEqual(bridge.bridge_guard_row(h.game+0x2a3980,h.actor,0x3d),0x1234)
        self.assertEqual(bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.),0x5678)
        self.assertAlmostEqual(bridge.bridge_motion_delta(),53./156.,places=6)
        h.clock(40.);bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
        self.assertAlmostEqual(bridge.bridge_motion_delta(),53./156.,places=6)
        self.assertEqual(h.event(110,1,0.),1);self.assertEqual(h.event(110,1,53.9),1);self.assertEqual(h.event(110,1,54.),0)

    def test_main_guard_accepts_front_side_and_rear_angles_only_with_its_own_live_guard_object(self):
        for bank in [98,60]:
            h=Host(guard=True,slot=bank);h.frame();h.equip(True);h.frame();bridge.bridge_guard_row(h.game+0x2a3980,h.actor,0x3d)
            first=h.game+0x2db4710;second=h.buffer(bytes(0xc0));w32(first,0x80800);w32(first+0x34,bridge.bridge_encode(h.actor))
            for native_class in [0x20000,0x40000,0x60000,0x80000]:
                w32(first,native_class|0x800)
                for direction in [1.,0.,-1.]:
                    put(second+0x10,struct.pack('<f',direction));self.assertEqual(bridge.bridge_guard_angle(h.game+0x2b4640,first,second),1)
            put(second+0x10,struct.pack('<f',-1.));w32(first,0xa0800)
            self.assertEqual(bridge.bridge_guard_angle(h.game+0x2b4640,first,second),0)
            w32(first,0x80800);w32(first+0x34,bridge.bridge_encode(h.buffer(bytes(0x800))))
            self.assertEqual(bridge.bridge_guard_angle(h.game+0x2b4640,first,second),0)

    def test_foreign_event_descriptor_or_payload_blocks_every_initial_body_write(self):
        for change in ['descriptor','payload']:
            h=Host(encoded_fields=True);h.frame();h.equip(True)
            original=(ROOT/'fixtures/original_s099.bin').read_bytes();at=struct.unpack_from('<I',original,60)[0]
            if change=='descriptor':w32(h.motions[99]+at+4,99)
            else:
                keys=struct.unpack_from('<I',original,at+8)[0]
                C.c_ubyte.from_address(h.motions[99]+keys+5).value^=1
            before=h.snapshot();h.frame();self.assertEqual(h.snapshot(),before)

    def test_blizzard_keeps_original_lookup_events_and_queue_with_only_the_fire_body_changed(self):
        for bank in [98,60]:
            h=Host(slot=bank,air=True,encoded_fields=True);h.arm_air()
            table=h.decode(r32(h.actor+0x1d8))
            self.assertEqual([r32(table+q*4)&0xfff for q in [0x37,0x84]],[55,80] if bank==98 else [18,42])
            for spell,slot,terminal in [(0x37,55,0x40000000),(0x84,80,0x40000075)]:
                w32(h.actor+0x164,spell);h.queue(terminal);queue=C.string_at(h.actor+0x178,36)
                h.frame()
                self.assertEqual(C.string_at(h.actor+0x178,36),queue)
                self.assertEqual(h.body(slot),h.blizzard_body(slot))
                raw=h.runtime_originals[slot];at=struct.unpack_from('<I',raw,60)[0]
                self.assertEqual(h.body(slot)[at:],raw[at:])
                h.frame();self.assertEqual(C.string_at(h.actor+0x178,36),queue)
                w32(h.actor+0x164,0x38 if spell==0x37 else 0x85);w32(h.actor+0x178,0);h.frame()
                self.assertEqual(h.body(slot),h.expected(slot,1))

    def test_unknown_request_descriptor_blocks_all_body_writes_and_lookup_changes(self):
        h=Host();h.frame();h.equip(True)
        w32(h.requests+0x38*4,0x1001);before=h.snapshot();pointer=r32(h.actor+0x1d8)
        h.frame();self.assertEqual(h.snapshot(),before);self.assertEqual(r32(h.actor+0x1d8),pointer)
        self.assertIn('cast request table must verify',bridge.bridge_log().decode())

    def test_foreign_request_pointer_is_retained_and_native_reload_is_readmitted(self):
        h=Host();h.frame();h.equip(True);h.frame()
        foreign=h.buffer(bytes(1408));pointer=bridge.bridge_encode(foreign)
        w32(h.actor+0x1d8,pointer);h.equip(False);before=h.snapshot();h.frame()
        self.assertEqual(h.snapshot(),before);self.assertEqual(r32(h.actor+0x1d8),pointer)
        w32(h.actor+0x1d8,h.original_request_handle);[h.frame() for _ in range(8)];h.assert_all(self,False)

    def test_request_restore_waits_for_cast_completion_and_rejects_changed_original(self):
        h=Host();h.frame();h.equip(True);h.frame();pointer=r32(h.actor+0x1d8)
        w32(h.actor+0x164,0x38);h.equip(False);h.frame();self.assertEqual(r32(h.actor+0x1d8),pointer)
        w32(h.actor+0x164,0);w32(h.requests+0x39*4,0x1002);before=h.snapshot();h.frame()
        self.assertEqual(h.snapshot(),before);self.assertEqual(r32(h.actor+0x1d8),pointer)
        put(h.requests,h.request_original);[h.frame() for _ in range(8)];h.assert_all(self,False)

    def test_normal_all_37_exact_on_and_off_including_idle_and_normal_only_ledge_recovery(self):
        h=Host();self.assertEqual(len(h.records),37);h.frame();h.equip(True);h.frame();h.assert_all(self,True)
        self.assertIn('AQUA BANK: normal Sora',bridge.bridge_log().decode())
        h.equip(False);h.frame();h.assert_all(self,False)

    def test_olympus_36_exact_on_and_off_with_encoded_pointers_and_common_idle_prefix(self):
        h=Host(slot=60,encoded_fields=True);self.assertEqual(len(h.records),36);h.frame();h.equip(True);h.frame();h.assert_all(self,True)
        self.assertIn('AQUA BANK: Olympus',bridge.bridge_log().decode())
        h.equip(False);h.frame();h.assert_all(self,False)

    def test_foreign_change_in_last_record_blocks_every_other_write(self):
        h=Host();h.frame();h.equip(True);p=h.motions[117];w32(p+r32(p+40)+4,0x7f123456);before=h.snapshot();h.frame();self.assertEqual(h.snapshot(),before)
        log=bridge.bridge_log().decode();self.assertIn('AQUA rejected request=0xDC',log);self.assertIn('AQUA admission stage=0x38',log)

    def test_changed_early_locomotion_schema_blocks_later_attack_writes(self):
        h=Host();h.frame();h.equip(True);w32(h.motions[4]+44,70);before=h.snapshot();h.frame();self.assertEqual(h.snapshot(),before)

    def test_changed_late_attack_schema_blocks_earlier_idle_and_locomotion_writes(self):
        h=Host();h.frame();h.equip(True);w32(h.motions[104]+44,70);before=h.snapshot();h.frame();self.assertEqual(h.snapshot(),before)

    def test_switch_waits_for_attacks_casts_jumping_and_walking_to_finish(self):
        h=Host();h.frame();h.equip(True)
        for action in [1,2,4,5,6,0x36,0x3e,0x48,0x83,0xc8,0xc9,0xcc,0xd4,0xdc]:
            w32(h.actor+0x164,action);h.frame();h.assert_all(self,False)
        w32(h.actor+0x164,0);h.frame();h.assert_all(self,True)

    def test_unequip_during_guard_waits_until_idle_then_restores_every_record(self):
        h=Host();h.frame();h.equip(True);h.frame();h.equip(False);w32(h.actor+0x164,0xd4);h.frame();h.assert_all(self,True)
        w32(h.actor+0x164,0);h.frame();h.assert_all(self,False)

    def test_unknown_game_build_writes_no_abilities_table_or_animations(self):
        h=Host(stamp=1);before=h.abilities();h.frame();self.assertEqual(h.abilities(),before);h.assert_all(self,False);self.assertEqual(r64(h.game+0x2d36d48),h.original_table)

    def test_no_stale_writes_after_actor_unload(self):
        h=Host();h.frame();h.equip(True);h.frame();w64(h.game+0x2537e48,0);h.equip(False);h.frame();h.assert_all(self,True)
        w64(h.game+0x2537e48,h.actor);h.frame();h.assert_all(self,False)

    def test_unmapped_slapshot_record_is_not_replaced(self):
        h=Host();h.frame();h.equip(True);h.frame();h.assert_all(self,True)
        self.assertEqual(C.string_at(h.unmapped,len(h.unmapped_original)),h.unmapped_original)
        h.equip(False);h.frame();self.assertEqual(C.string_at(h.unmapped,len(h.unmapped_original)),h.unmapped_original)

    def test_noncontiguous_native_table_pointers_remain_supported(self):
        h=Host();h.frame();slot=1;p=h.motions[slot];original=h.runtime_originals[slot]
        offset=struct.unpack_from('<I',original,56)[0];size=r32(p+52)*8
        remote=h.buffer(original[offset:offset+size]);w32(p+56,bridge.bridge_encode(remote))
        h.runtime_originals[slot]=C.string_at(p,len(original));h.equip(True);h.frame()
        expected=bytearray(h.expected(slot,True));expected[offset:offset+size]=original[offset:offset+size]
        self.assertEqual(h.body(slot),bytes(expected))
        after=(ROOT/f"fixtures/aqua_{h.record_by_slot[slot]['fixture_stem']}.bin").read_bytes()
        self.assertEqual(C.string_at(remote,size),after[offset:offset+size])
        h.frame();h.equip(False);h.frame();h.assert_all(self,False)
        self.assertEqual(C.string_at(remote,size),original[offset:offset+size])

    def test_cached_scalar_corruption_is_rejected_before_toggle_writes(self):
        h=Host();h.frame();h.equip(True);h.frame();w32(h.motions[0]+24,999);h.equip(False);before=h.snapshot();h.frame();self.assertEqual(h.snapshot(),before)

    def test_foreign_nonsentinel_key_change_is_rejected_when_restoring(self):
        h=Host();h.frame();h.equip(True);h.frame();p=h.motions[104];offset=struct.unpack_from('<I',h.runtime_originals[104],40)[0]
        w32(p+offset+80,0x7f123456);h.equip(False);before=h.snapshot();h.frame();self.assertEqual(h.snapshot(),before)

    def guard_setup(self,bank=98):
        h=Host(slot=bank,guard=True);h.frame();h.equip(True);h.frame()
        bridge.bridge_guard_row(h.game+0x2a3980,h.actor,0x3d)
        native=h.game+0x2db4710;data=h.buffer(bytes(0x70))
        w32(native,0x80800);w32(native+0x34,bridge.bridge_encode(h.actor));w32(native+0x5c,bridge.bridge_encode(data))
        w32(native+0x54,1);w32(h.game+0x2db7710,1)
        put(h.actor+0x10,struct.pack('<3f',100.,200.,300.))
        self.assertEqual(bridge.bridge_guard_pool(h.game+0x2b47a0),19)
        return h,native,native+0xc0,data

    def test_other_native_row_callbacks_do_not_forget_the_witnessed_guard(self):
        h,native,p,data=self.guard_setup();bridge.bridge_guard_row(h.game+0x2a3980,h.actor,0x12)
        w32(h.actor+0x164,0x6e);h.clock(0.);bridge.bridge_guard_pool(h.game+0x2b47a0)
        self.assertTrue(r32(p)&0x800)
        h.queue(0xc8);bridge.bridge_guard_pool(h.game+0x2b47a0);self.assertFalse(r32(p)&0x800)

    def test_wider_guard_creates_one_native_body_capsule_covering_front_sides_and_rear(self):
        for bank in [98,60]:
            h,native,p,data=self.guard_setup(bank)
            self.assertEqual(r32(p)&0xe0000,0x80000);self.assertEqual(r32(p+0x2c),0)
            self.assertEqual(r32(p+0x68),100);self.assertEqual(h.decode(r32(p+0x34)),h.actor)
            self.assertNotEqual(h.decode(r32(p+0x5c)),data)
            self.assertEqual(struct.unpack('<f',C.string_at(data+0x64,4))[0],0.)
            self.assertLess(struct.unpack('<f',C.string_at(h.decode(r32(p+0x5c))+0x64,4))[0],-1.)
            a=list(struct.unpack('<4f',C.string_at(p+0x10,16)));b=list(struct.unpack('<4f',C.string_at(p+0x40,16)))
            self.assertEqual(a,[100.,165.,300.,1.]);self.assertEqual(b,[100.,115.,300.,1.])
            self.assertEqual(struct.unpack('<f',C.string_at(p+0xc,4))[0],50.)
            # Capsule geometry reaches equally to the front, rear and either side.
            for dx,dz in [(0,45),(0,-45),(45,0),(-45,0)]:self.assertLessEqual(dx*dx+dz*dz,50.*50.)
            for _ in range(20):bridge.bridge_guard_pool(h.game+0x2b47a0)
            self.assertEqual(sum(bool(r32(native+i*0xc0)&0x800) for i in range(64)),2)

    def test_guard_shield_follows_body_and_rearms_without_new_allocations(self):
        h,native,p,data=self.guard_setup();put(h.actor+0x10,struct.pack('<3f',-50.,100.,-80.))
        w32(p,r32(p)&~0x200);bridge.bridge_guard_pool(h.game+0x2b47a0)
        self.assertEqual(struct.unpack('<4f',C.string_at(p+0x10,16)),(-50.,65.,-80.,1.))
        self.assertEqual(C.string_at(p+0x10,16),C.string_at(p+0x70,16));self.assertTrue(r32(p)&0x200)

    def test_native_parry_6e_and_6f_keep_only_twelve_ticks_of_extra_guard(self):
        for request in [0x6e,0x6f]:
            h,native,p,data=self.guard_setup();w32(h.actor+0x164,request);h.clock(0.)
            for _ in range(11):
                bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
                bridge.bridge_guard_pool(h.game+0x2b47a0);self.assertTrue(r32(p)&0x800)
            bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.);bridge.bridge_guard_pool(h.game+0x2b47a0)
            self.assertFalse(r32(p)&0x800);self.assertTrue(r32(native)&0x800)

    def test_guard_release_grace_is_small_and_cannot_survive_new_actions(self):
        for request in [0,1,2,0x48,0x4c,0xc8,0xcc,0x36]:
            h,native,p,data=self.guard_setup()
            for _ in range(155):bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
            h.frame();w32(h.actor+0x164,request);h.clock(0.)
            bridge.bridge_guard_pool(h.game+0x2b47a0)
            if request==0:
                self.assertTrue(r32(p)&0x800)
                for _ in range(13):bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
                bridge.bridge_guard_pool(h.game+0x2b47a0)
            self.assertFalse(r32(p)&0x800);self.assertTrue(r32(native)&0x800)

    def test_guard_retirement_cannot_free_a_recycled_or_foreign_pool_object(self):
        for changed in ['owner','data','mask']:
            h,native,p,data=self.guard_setup();field={'owner':0x34,'data':0x5c,'mask':0x54}[changed]
            w32(p+field,0x12345678);before=C.string_at(p,0xc0)
            w32(h.actor+0x164,0x48);h.frame();self.assertEqual(C.string_at(p,0xc0),before)

    def test_guard_does_not_allocate_without_a_witness_template_or_free_native_slot(self):
        for reason in ['witness','template','full','mask']:
            h,native,p,data=self.guard_setup();w32(h.actor+0x164,0x48);h.frame()
            if reason!='witness':bridge.bridge_guard_row(h.game+0x2a3980,h.actor,0x3d)
            if reason=='template':w32(native+0x34,bridge.bridge_encode(h.buffer(bytes(0x800))))
            if reason=='full':
                for i in range(1,64):w32(native+i*0xc0,0x800)
            if reason=='mask':w32(h.game+0x2db7710,0x7fffffff)
            before=C.string_at(native,0x3000);bridge.bridge_guard_pool(h.game+0x2b47a0)
            self.assertEqual(C.string_at(native,0x3000),before)

    def test_unrelated_collision_pairs_do_not_query_or_validate_soras_guard(self):
        h,native,p,data=self.guard_setup();other=h.game+0x2db4710+10*0xc0
        w32(other,0x80800);w32(other+0x34,bridge.bridge_encode(h.buffer(bytes(0x800))))
        enemy=h.buffer(bytes(0xc0));q=bridge.bridge_queries()
        for _ in range(1000):bridge.bridge_guard_angle(h.game+0x2b4640,other,enemy)
        self.assertEqual(bridge.bridge_queries()-q,0)

    def test_air_combo_keeps_a_usable_followup_window_to_end_of_each_nonfinisher(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.frame();h.equip(True);h.frame()
            for slot,start,end in [(102,18.,40.),(103,22.,42.)]:
                self.assertEqual(h.event(slot,5,start),1);self.assertEqual(h.event(slot,5,end-.1),1)
                self.assertEqual(h.event(slot,5,end),0)
                for dt in [.5,1.,2.,4.]:self.assertGreaterEqual(sum(h.event(slot,5,f)==1 for f in __import__('numpy').arange(start+.1,end,dt)),4)
            self.assertEqual([h.record_by_slot[x]['donor'] for x in [102,103,104]],['305','407','353'])

    def test_both_second_ground_variants_have_identical_real_contact_and_chain_timing(self):
        h=Host(guard=True,encoded_fields=True);h.frame();h.equip(True);h.frame()
        hits=[];chains=[]
        for request,slot,finish in [(0xc9,99,24.),(0xca,100,33.6)]:
            w32(h.actor+0x164,request);h.clock(0.);bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
            rate=bridge.bridge_motion_delta();hits.append((finish*8./30.)/rate);chains.append(finish/rate)
        self.assertAlmostEqual(hits[0],hits[1],places=5);self.assertAlmostEqual(chains[0],chains[1],places=5)

    def test_main_fast_dodge_moves_same_distance_and_lift_in_two_thirds_time(self):
        for bank in [98,60]:
            for dt in [.5,1.,2.,4.]:
                for motion_first in [False,True]:
                    h=Host(slot=bank,air=True,guard=True);h.arm_air();h.control(down=6,pressed=6,x=1,tilt=1)
                    elapsed=0.;total=[0.,0.,0.]
                    while elapsed<26.:
                        if motion_first:bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,dt)
                        out,_=h.move(dt)
                        for k in range(3):total[k]+=out[k]
                        elapsed+=min(dt,26.-elapsed)
                        if not motion_first:bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,dt)
                    self.assertEqual(total,[546.,-29.25,0.]);self.assertEqual(h.body(10),h.expected(10,1))
                    self.assertEqual(C.c_float.from_address(h.actor+0x3c0).value,14.)

    def test_fast_dodge_advances_504_animation_by_one_and_a_half_per_native_tick(self):
        h=Host(air=True,guard=True);h.arm_air();h.control(down=6,pressed=6,x=1,tilt=1)
        bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
        self.assertEqual(bridge.bridge_motion_delta(),1.5);self.assertEqual(C.c_float.from_address(h.actor+0x16c).value,1.5)
        self.assertEqual(h.move()[0],[21.,-1.125,0.,21.])
        for slot,p in h.native_glide_motions.items():self.assertEqual(C.string_at(p,len(h.native_glide_originals[slot])),h.native_glide_originals[slot])

    def test_fast_dodge_retains_direction_and_same_diagonal_distance(self):
        import math
        for x,z in [(0,1),(0,-1),(-1,0),(.7,.7)]:
            h=Host(air=True,guard=True);h.arm_air();h.control(down=6,pressed=6,x=x,z=z,tilt=1)
            out,_=h.move();self.assertAlmostEqual(math.hypot(out[0],out[2]),21.,places=4)
            h.control(down=0,x=-x,z=-z,tilt=1)
            after,_=h.move();self.assertEqual(after,out)

    def test_main_dodge_budget_stays_spent_through_superglide_ability_switch_and_binding_reset(self):
        for reason in ['superglide','ability','binding']:
            h=Host(air=True,guard=True);h.arm_air();h.control(down=6,pressed=6,x=1,tilt=1)
            h.clock(39.);h.frame();h.control()
            if reason=='superglide':bridge.bridge_glide(h.game+0x2b2750,h.actor)
            elif reason=='ability':
                h.equip(False);h.frame();h.equip(True);h.frame()
            else:
                w32(h.motions[104]+24,999);h.frame()
                # Restore only the known scalar from its original header, then wait for bounded admission.
                w32(h.motions[104]+24,struct.unpack_from('<I',h.runtime_originals[104],24)[0]);[h.frame() for _ in range(9)]
            h.control(state=2,request=6);calls=bridge.bridge_queue_calls()
            h.control(down=6,pressed=6,x=1,tilt=1);self.assertEqual(bridge.bridge_queue_calls(),calls)
            self.assertEqual(h.body(10),h.expected(10,1))
            h.control(state=0,request=0,height=0);h.control(state=2,request=6)
            h.control(down=6,pressed=6,x=1,tilt=1);self.assertEqual(bridge.bridge_queue_calls(),calls+1)

    def test_grounded_while_aqua_is_off_rearms_exactly_the_next_airtime(self):
        h=Host(air=True,guard=True);h.arm_air();h.control(down=6,pressed=6);h.clock(39.);h.frame()
        h.equip(False);w32(h.actor+0x164,0);w32(h.actor+0x70,0);put(h.actor+0x3d4,struct.pack('<f',0.));h.frame()
        h.equip(True);h.frame();h.control(state=2,request=6);calls=bridge.bridge_queue_calls()
        h.control(down=6,pressed=6);self.assertEqual(bridge.bridge_queue_calls(),calls+1)

    def test_native_superglide_can_interrupt_a_dodge_without_resetting_its_budget(self):
        h=Host(air=True,guard=True);h.arm_air();h.control(down=6,pressed=6,x=1,tilt=1)
        h.move();bridge.bridge_glide(h.game+0x2b2750,h.actor)
        self.assertEqual(r32(h.actor+0x70),21);self.assertEqual(r32(h.glide_work+0x104)&1,1)
        self.assertEqual(h.body(10),h.expected(10,1));calls=bridge.bridge_queue_calls()
        h.control(state=2,request=6);h.control(down=6,pressed=6);self.assertEqual(bridge.bridge_queue_calls(),calls)

    def test_rejected_superglide_does_not_cancel_a_live_dodge(self):
        h=Host(air=True,guard=True);h.arm_air();h.control(down=6,pressed=6,x=1,tilt=1)
        bridge.bridge_glide_eligible(0);bridge.bridge_glide(h.game+0x2b2750,h.actor)
        self.assertEqual(h.body(10),h.dodge_body());self.assertEqual(h.move()[0][0],21.)

    def launch_native_jump(self,h,request=4,height=160.,elapsed=4.):
        w32(h.actor+0x70,1);w32(h.actor+0x164,request);put(h.actor+0x3b0,struct.pack('<f',elapsed))
        put(h.actor+0x14,struct.pack('<f',500.));put(h.jump_stats+0x10,struct.pack('<f',height))
        out=h.buffer(struct.pack('<4f',12.,4.,6.,7.))
        result=bridge.bridge_move(h.game+0x2afda0,h.actor,C.cast(out,C.POINTER(C.c_float)))
        return list((C.c_float*4).from_address(out)),result

    def test_real_native_jump_curve_reaches_the_higher_apex_with_its_gravity_unchanged(self):
        import math
        h=Host(air=True,jump=True);h.frame();h.equip(True);h.frame();self.launch_native_jump(h,height=160.)
        duration=C.c_float.from_address(h.actor+0x3b8).value;out=h.buffer(bytes(16))
        put(h.actor+0x3b0,struct.pack('<f',duration));bridge.bridge_move(h.game+0x2af530,h.actor,C.cast(out,C.POINTER(C.c_float)))
        self.assertAlmostEqual(C.c_float.from_address(out+4).value,-200.,places=4)
        put(h.actor+0x3b0,struct.pack('<f',duration+2.));bridge.bridge_move(h.game+0x2af530,h.actor,C.cast(out,C.POINTER(C.c_float)))
        gravity=struct.unpack('<f',bytes.fromhex(json.loads((ROOT/'fixtures/native_jump_constants.json').read_text())['0x3e9d14'])[:4])[0]
        self.assertAlmostEqual(C.c_float.from_address(out+4).value,-200.+.5*gravity*4.,places=3)

    def test_jump_boost_waits_for_native_takeoff_and_does_not_compound(self):
        h=Host(air=True,jump=True);h.frame();h.equip(True);h.frame()
        self.launch_native_jump(h,elapsed=0.);self.assertEqual(r32(h.actor+0x70),1)
        self.launch_native_jump(h,elapsed=4.);height=C.c_float.from_address(h.actor+0x3bc).value
        w32(h.actor+0x164,5);out=h.buffer(bytes(16));bridge.bridge_move(h.game+0x2afda0,h.actor,C.cast(out,C.POINTER(C.c_float)))
        self.assertEqual(C.c_float.from_address(h.actor+0x3bc).value,height)

    def test_second_attack_chain_opens_earlier_and_finished_pose_hold_runs_twice_as_fast(self):
        for request,slot,finish,rate in [(0xc9,99,24.,1.),(0xca,100,33.6,1.4)]:
            h=Host(guard=True,encoded_fields=True);h.frame();h.equip(True);h.frame();w32(h.actor+0x164,request)
            h.clock(finish);bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
            self.assertAlmostEqual(bridge.bridge_motion_delta(),rate*2.,places=5)
            self.assertEqual(h.event(slot,5,finish+.01),1)
            self.assertLess(finish/rate,30.)
            h.clock(finish-rate*.5);bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
            self.assertAlmostEqual(bridge.bridge_motion_delta(),rate*1.5,places=4)


    def test_shared_entry_points_are_never_hooked_twice_by_adapter(self):
        h=Host();self.assertTrue(h.adapter_ready);self.assertEqual(h.shared_before,h.shared_after)
    def test_entry_and_exit_wait_at_idle_before_other_styles_may_run(self):
        h=Host();before=h.snapshot();h.equip(True);w32(h.actor+0x164,0xc8)
        self.assertFalse(h.frame());self.assertEqual(h.snapshot(),before)
        w32(h.actor+0x164,0);self.assertFalse(h.frame());h.assert_all(self,True)
        h.equip(False);w32(h.actor+0x164,0xc9);self.assertFalse(h.frame());h.assert_all(self,True)
        w32(h.actor+0x164,0);self.assertTrue(h.frame());h.assert_all(self,False)
    def test_adapter_does_not_register_or_learn_any_standalone_abilities(self):
        h=Host();before=h.abilities();table=r64(h.game+0x2d36d48)
        h.equip(True);h.frame();self.assertEqual(h.abilities(),before)
        self.assertEqual(r64(h.game+0x2d36d48),table);self.assertEqual(C.string_at(table,65*12),h.native_table)
    def test_same_epoch_selection_is_immediate_and_repeated_callbacks_do_not_tick_twice(self):
        h=Host();h.frame(epoch=1);h.equip(True);h.frame(epoch=1);h.assert_all(self,True)
        h.arm_air();h.control(down=6,pressed=6,x=1,tilt=1)
        for _ in range(30):h.frame(epoch=h.epoch)
        self.assertEqual(h.move()[0],[21.,-1.125,0.,21.])
    def test_both_native_jump_types_get_boost_and_off_is_native(self):
        import math
        for bank in [98,60]:
            for request in [4,9]:
                for on in [False,True]:
                    h=Host(slot=bank);h.equip(on);h.frame()
                    self.launch_native_jump(h,request,160.)
                    self.assertAlmostEqual(C.c_float.from_address(h.actor+0x3bc).value,-200. if on else -160.)
    def test_required_controller_failure_never_publishes_aqua_bodies(self):
        for bad in ['stamp','alloc','protect']:
            h=Host(stamp=0 if bad=='stamp' else 1721645006,fail_alloc=bad=='alloc',fail_protect=1 if bad=='protect' else 0)
            self.assertFalse(h.adapter_ready);before=h.snapshot();h.equip(True);self.assertTrue(h.frame())
            self.assertEqual(h.snapshot(),before)

if __name__=='__main__':
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RuntimeTests))
    report={'passed':result.wasSuccessful(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'executed_final_integrated_pe_c_adapter':True,'rust_shared_dispatch_mocked':True,'native_event_sampler_jump_curve_and_glide_constructors_executed':True,'windows_or_game_executed':False}
    Path(os.environ.get('VALIDATION_OUT',str(TEST_ROOT/'runtime_validation.json'))).write_text(json.dumps(report,indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
