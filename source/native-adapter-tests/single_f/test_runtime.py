"""Run the final combined PE's C adapter with Win64 ABI mocks on Linux.

Rust DllMain, shared Rust dispatch and rendering are not executed. Private
source fixtures are provided through the documented environment variables.
"""
from pathlib import Path
import ctypes as C,json,struct,subprocess,sys,unittest,os
ROOT=Path(os.environ['TERRA_SOURCE']).resolve()
TEST_ROOT=Path(__file__).resolve().parent
subprocess.run(['gcc','-std=c11','-O2','-shared','-fPIC',str(TEST_ROOT/'test_bridge.c'),'-o',str(TEST_ROOT/'test_bridge.so'),'-lm'],cwd=ROOT,check=True)
bridge=C.CDLL(str(TEST_ROOT/'test_bridge.so'))
for name,args,ret in [('bridge_reset',[C.c_size_t],None),('bridge_range',[C.c_size_t,C.c_size_t,C.c_uint],None),('bridge_modes',[C.c_int,C.c_int],None),('bridge_log',[],C.c_char_p),('bridge_queries',[],C.c_uint),('bridge_encode',[C.c_size_t],C.c_uint),('bridge_symbol',[C.c_char_p],C.c_size_t),('bridge_call0',[C.c_size_t],None),('bridge_init',[C.c_size_t],None)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
bridge.bridge_test_options.argtypes=[C.c_int,C.c_int];bridge.bridge_test_options.restype=None
bridge.bridge_ability_count.argtypes=[C.c_size_t,C.c_uint,C.c_uint];bridge.bridge_ability_count.restype=C.c_uint
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
    def __init__(self,slot=98,encoded_fields=False,stamp=1721645006,remove=0,conflict=0,magic=False,hand_magic=1,fail_alloc=0,fail_protect=0,air=False,air_dodge=1,control_mode=0,guard=False,jump=False,test_page=1,profile_override=0):
        self.game=allocate(0x3000000);bridge.bridge_reset(self.game);bridge.bridge_range(self.game,0x3000000,0x40);bridge.bridge_modes(remove,conflict)
        bridge.bridge_test_options(test_page,profile_override)
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
        dll=Path(os.environ['STYLES_DLL']).resolve()
        if not dll.exists():dll=ROOT.parent/'dll/kh1-terra.dll'
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
        symoff,symcount=struct.unpack_from('<II',data,pe+12);strings=symoff+symcount*18
        sections=[struct.unpack_from('<I',data,sh+i*40+12)[0] for i in range(n)]
        self.symbols={};i=0
        while i<symcount:
            at=symoff+i*18;name=data[at:at+8]
            if name[:4]==bytes(4):
                start=strings+struct.unpack_from('<I',name,4)[0];name=data[start:data.index(0,start)]
            else:name=name.rstrip(b'\0')
            value,section=struct.unpack_from('<Ih',data,at+8)
            if section>0:self.symbols[name.decode(errors='replace')]=p+sections[section-1]+value
            i+=1+data[at+17]
        self.fn={}
    def frame(self):bridge.bridge_call0(self.exports['OnFrame'])
    def native_count(self,id_):
        w64(self.game+0x2868ba0,self.save)
        put(self.game+0x284be0,(ROOT/'fixtures/native_ability_count.bin').read_bytes())
        return bridge.bridge_ability_count(self.game+0x284be0,id_,0)
    def abilities(self):return C.string_at(self.save+0x44,48)
    def equip(self,on,profile=0):
        id_=116+profile;data=bytearray(self.abilities());i=next(i for i,v in enumerate(data) if v&127==id_);data[i]=id_ if on else id_|128;put(self.save+0x44,bytes(data))
    def decode(self,h):return r64(self.game+0x2ee3980+((h&0x7fffffff)>>25)*8)+(h&0x1ffffff)
    def body(self,slot=98):return C.string_at(self.motions[slot],len(self.runtime_originals[slot]))
    def expected(self,slot,on):
        r=self.record_by_slot[slot];folder=ROOT/'fixtures'
        if int(on)>1:
            candidate=ROOT/f'sets/p{int(on)-1}/fixtures'
            if (candidate/f"terra_{r['fixture_stem']}.bin").exists():folder=candidate
            elif (ROOT/f"sets/shared_v2/fixtures/terra_{r['fixture_stem']}.bin").exists():folder=ROOT/'sets/shared_v2/fixtures'
        return self.expected_from(slot,folder/f"{'terra' if on else 'original'}_{r['fixture_stem']}.bin")
    def expected_from(self,slot,path):
        r=self.record_by_slot[slot];data=bytearray(path.read_bytes())
        data[:80]=self.runtime_originals[slot][:80]
        event_at=struct.unpack_from('<I',(ROOT/f"fixtures/original_{r['fixture_stem']}.bin").read_bytes(),60)[0]
        while struct.unpack_from('<I',data,event_at)[0]!=0xffffffff:
            data[event_at+8:event_at+12]=self.runtime_originals[slot][event_at+8:event_at+12];event_at+=12
        return bytes(data)
    def expected_variant(self,slot):
        return self.expected_from(slot,ROOT/f"overlays/fixtures/terra_{self.record_by_slot[slot]['fixture_stem']}.bin")
    def assert_all(self,test,on):
        for r in self.records:test.assertEqual(self.body(r['normal_slot']),self.expected(r['normal_slot'],on),r['action'])
        test.assertEqual(r32(self.actor+0x1d8),self.original_request_handle)
        test.assertEqual(C.string_at(self.requests,len(self.request_original)),self.request_original)
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
        put(self.game+0x233fbdc,struct.pack('<f',dt))
        if not hasattr(self,'move_output'):self.move_output=self.buffer(bytes(16))
        out=self.move_output
        result=bridge.bridge_move(self.game+0x2af6a0,self.actor,C.cast(out,C.POINTER(C.c_float)))
        return list((C.c_float*4).from_address(out)),result
    def blizzard_body(self,slot):
        data=bytearray((ROOT/f'blizzard/fixtures/terra_s{slot:03}.bin').read_bytes());data[:80]=self.runtime_originals[slot][:80]
        at=struct.unpack_from('<I',(ROOT/f'blizzard/fixtures/terra_s{slot:03}.bin').read_bytes(),60)[0]
        while struct.unpack_from('<I',data,at)[0]!=0xffffffff:
            data[at+8:at+12]=self.runtime_originals[slot][at+8:at+12];at+=12
        return bytes(data)
    def dodge_body(self):
        data=bytearray((ROOT/'dodge/fixtures/terra_s010.bin').read_bytes());data[:80]=self.runtime_originals[10][:80];return bytes(data)
    def event(self,slot,kind,frame,track=0):
        p=bridge.bridge_event(self.game+0x394770,self.motions[slot],(kind<<16)|track,frame)
        return None if not p else r32(p+4)
    def native_glide(self):bridge.bridge_glide(self.game+0x2b26c0,self.actor)
    def native_super_glide(self):bridge.bridge_glide(self.game+0x2b2750,self.actor)
    def prepare_slide(self,profile=0):
        self.frame();self.equip(True,profile);self.frame();w32(self.game+0x2d5ec10,0x180)
        self.control(state=0,request=0,height=0);self.control(state=2,request=6)
    def tap_slide(self,x=1,z=0):self.control(down=0x10,pressed=0x10,state=2,request=6,height=100,tilt=1,x=x,z=z)
    def queue(self,request,frame=0):
        w32(self.actor+0x178,1);w32(self.actor+0x17c,request);put(self.actor+0x184,struct.pack('<f',frame))
    def clock(self,value):put(self.actor+0x16c,struct.pack('<f',value))
    def arm_air(self,profile=0):
        self.frame();self.equip(True,profile);self.frame();self.control(state=0,request=0,height=0)
        self.control(state=2,request=6)

BaseHost=Host
for name,args,ret in [('adapter_init',[C.c_size_t,C.c_size_t,C.c_int],C.c_int),('adapter_frame',[C.c_size_t,C.c_size_t,C.c_int,C.c_uint64],C.c_int),('adapter_control',[C.c_size_t]*3,None),('adapter_observe',[C.c_size_t]*2,None),('call_int0',[C.c_size_t],C.c_int),('call_ptr1',[C.c_size_t]*2,C.c_size_t),('call_void1',[C.c_size_t]*2,None)]:
 f=getattr(bridge,name);f.argtypes=args;f.restype=ret
class Host(BaseHost):
 def __init__(self,*args,**kwargs):
  kwargs['air']=True;self.want=0;self.epoch=0;super().__init__(*args,**kwargs)
  self.adapter_ready=bridge.adapter_init(self.symbols['SingleFInit'],self.game,1)
  w64(self.game+0x2868ba0,self.save)
 def equip(self,on,profile=0):assert not profile;self.want=bool(on)
 def frame(self,epoch=None):
  self.epoch=self.epoch+1 if epoch is None else epoch
  return bridge.adapter_frame(self.symbols['SingleFFrame'],self.actor,self.want,self.epoch)
 def control(self,down=0,pressed=0,state=2,request=6,height=100,tilt=0,x=0,z=0,actor=None):
  a=self.actor if actor is None else actor;w32(a+0x70,state);w32(a+0x164,request);put(a+0x3d4,struct.pack('<f',height))
  for field in [4,8,16,20]:w32(self.game+0x298ca90+field,(down if field in [4,16] else pressed))
  put(self.dir,struct.pack('<4f',x,0,z,tilt));bridge.adapter_control(self.symbols['SingleFControl'],a,self.dir)
 def move(self,dt=1.):
  put(self.game+0x233fbdc,struct.pack('<f',dt))
  if not hasattr(self,'move_output'):self.move_output=self.buffer(bytes(16))
  out=self.move_output;result=bridge.bridge_move(self.symbols['SingleFMove'],self.actor,C.cast(out,C.POINTER(C.c_float)))
  return list((C.c_float*4).from_address(out)),result
 def native_glide(self):
  if not bridge.call_ptr1(self.symbols['SingleFSuppressGlide'],self.actor):super().native_glide()
 def native_super_glide(self):
  if not bridge.call_ptr1(self.symbols['SingleFSuppressSuperglide'],self.actor):super().native_super_glide()
 def observe(self):bridge.adapter_observe(self.symbols['SingleFObserve'],self.actor)
 def expected_variant(self,slot):return self.expected(10,1) if slot==10 else super().expected_variant(slot)
 def ui_seed(self):
  exe=Path(os.environ['KH1_EXE']).read_bytes();pe=struct.unpack_from('<I',exe,60)[0];sh=pe+24+struct.unpack_from('<H',exe,pe+20)[0];sects=[struct.unpack_from('<4I',exe,sh+i*40+8) for i in range(struct.unpack_from('<H',exe,pe+6)[0])]
  def raw(r,n):
   for vs,va,rs,rp in sects:
    if va<=r and r+n<=va+rs:return exe[rp+r-va:rp+r-va+n]
   raise AssertionError(hex(r))
  anchors=[]
  import re
  for line in (Path(os.environ.get('STYLES_MENU_ANCHORS',str(Path(__file__).resolve().parents[2]/'src/single_f/styles_menu_anchors.h')))).read_text().splitlines():
   if line.startswith('{0x'):
    values=line.split(',',6);r=int(values[0][1:],16);n=int(values[1]);anchors.append((r,n));put(self.game+r,raw(r,n))
  for r,n in [(0x2dae20,15),(0x311c56,16),(0x2d0970,21)]:put(self.game+r,raw(r,n))
  for r,f in [(0x52af20,0x2d3840),(0x5490f0,0x310ef0),(0x5490c0,0x310b60),(0x549090,0x310a90)]:w64(self.game+r,self.game+f)
  # Relocate native definition/callback tables as a normal loaded executable.
  for r,n in [(0x52ad40,32),(0x52ad60,64),(0x52ada0,64),(0x52ade0,32),(0x52afb8,32)]:
   data=bytearray(raw(r,n))
   if r in [0x52ad60,0x52ada0]:
    for i in range(0,n,8):struct.pack_into('<Q',data,i,struct.unpack_from('<Q',data,i)[0]-0x140000000+self.game)
   put(self.game+r,data)
  w32(self.game+0x2e941d0,3);put(self.save+0x48e,b'\0\x01\x02');w32(self.game+0x545360,16);w32(self.game+0x545368,2)
  # A native function with the exact admitted prologue; unrelated page creation
  # and drawing are host mocks. The original ability pointer arithmetic runs.
  put(self.game+0x2dae2f,b'\xc3');put(self.game+0x311850,b'\xc3');put(self.game+0x310ef0,b'\xc3');put(self.game+0x310b60,b'\xc3');put(self.game+0x2d3840,b'\xc3')
  put(self.game+0x311c20,raw(0x311c20,0x36))
  # Tail returns the selected view record, retaining original native callee saves.
  self.ui_tail=bytes.fromhex('4c89e04881c498000000415e415c5f5dc3')
  put(self.game+0x311c66,self.ui_tail)
  put(self.game+0x310a90,b'\x48\xb8'+struct.pack('<Q',self.game+0x311c20)+b'\xff\xe0')
  w32(self.game+0x2e9cb80,0);w32(self.game+0x2e1f4c8,8);put(self.game+0x2e1f4a8,struct.pack('<8I',*range(8)))
  return anchors
 def ui_init(self):return bridge.call_int0(self.symbols['StylesMenuInit'])
 def ui_call(self,name,arg=0):bridge.call_void1(self.symbols[name],arg)
 def ui_window(self,slot=0):
  w=self.buffer(bytes(0x200));w32(w+0x48,slot);return w

class RuntimeTests(unittest.TestCase):
    def test_slide_fresh_square_plays009_and_release_does_not_shorten_it(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True,air=True);h.prepare_slide();h.tap_slide()
            self.assertEqual(h.body(10),h.expected_variant(10));self.assertEqual(r32(h.actor+0x164),6)
            self.assertEqual(bridge.bridge_queue_calls(),1)
            for i in range(5):
                h.clock(float(i));h.control(state=2,request=6);delta,_=h.move()
                self.assertEqual(delta,[16.,0.,0.,16.]);self.assertEqual(h.body(10),h.expected_variant(10))
            self.assertEqual(bridge.bridge_control_word(0)&0x16,0)
    def test_slide_distance_is_finite_and_independent_of_tick_size(self):
        for dt in [0.25,0.5,1.,1.25,2.5]:
            h=Host(air=True);h.prepare_slide();h.tap_slide();elapsed=0.;total=[0.,0.,0.]
            while elapsed<39.-1e-5:
                h.clock(elapsed);delta,_=h.move(dt)
                for i in range(3):total[i]+=delta[i]
                elapsed+=min(dt,39.-elapsed)
            self.assertEqual(total,[624.,0.,0.]);self.assertEqual(h.body(10),h.expected(10,1))
            delta,_=h.move();self.assertEqual(delta,[1.,2.,3.,4.])
    def test_native_animation_clock_completion_restores_fall_and_release_velocity(self):
        h=Host(air=True);h.prepare_slide();h.tap_slide();h.move();h.clock(39.);h.control(state=2,request=6)
        self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(struct.unpack('<f',C.string_at(h.actor+0x3c0,4))[0],8.)
        self.assertEqual(h.move()[0],[1.,2.,3.,4.])
    def test_slide_locks_initial_analog_direction_and_does_not_write_actor_position(self):
        h=Host(air=True);h.prepare_slide();put(h.actor+0x10,struct.pack('<4f',12.,13.,14.,1.));h.tap_slide(.6,.8)
        h.control(state=2,request=6,tilt=1,x=-1,z=0);delta,_=h.move()
        self.assertAlmostEqual(delta[0],9.6,places=5);self.assertAlmostEqual(delta[2],12.8,places=5)
        self.assertEqual(C.string_at(h.actor+0x10,16),struct.pack('<4f',12.,13.,14.,1.))
        self.assertEqual(delta[1],0.)
    def test_slide_neutral_stick_uses_character_facing(self):
        h=Host(air=True);h.prepare_slide();put(h.actor+0x30,struct.pack('<3f',0.,0.,-1.));h.tap_slide(0,0)
        self.assertEqual(h.move()[0],[0.,0.,-16.,16.])
    def test_holding_square_never_starts_or_restarts_slide(self):
        h=Host(air=True);h.prepare_slide()
        for _ in range(3):h.control(down=0x10,pressed=0,state=2,request=6)
        self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(bridge.bridge_queue_calls(),0)
        h.tap_slide()
        for _ in range(39):h.move()
        for _ in range(3):h.control(down=0x10,pressed=0,state=2,request=6)
        self.assertEqual(bridge.bridge_queue_calls(),1);self.assertEqual(h.body(10),h.expected(10,1))
        h.control(state=2,request=6);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
    def test_slide_requires_airborne_height_and_free_action(self):
        cases=[{'state':0,'request':0},{'state':2,'request':0xcc},{'height':1},{'height':float('nan')},{'x':float('nan')},{'x':3}]
        for extra in cases:
            h=Host(air=True);h.prepare_slide();args=dict(down=0x10,pressed=0x10,state=2,request=6,height=100,tilt=1,x=1,z=0);args.update(extra);h.control(**args)
            self.assertEqual(bridge.bridge_queue_calls(),0);self.assertEqual(h.body(10),h.expected(10,1))
    def test_main_grants_air_dash_without_native_superglide_or_legacy_cooldown(self):
        for height in [2.,10.,49.,50.,100.]:
            h=Host(air=True);h.prepare_slide();w32(h.game+0x2d5ec10,0);put(h.glide_work+0x100,struct.pack('<f',24.))
            h.control(down=0x10,pressed=0x10,state=2,request=10,height=height,tilt=1,x=1,z=0)
            self.assertEqual(bridge.bridge_queue_calls(),1);self.assertEqual(h.body(10),h.expected_variant(10));self.assertEqual(h.move()[0],[16.,0.,0.,16.])
    def test_slide_does_not_replace_queued_attack_or_spell_command(self):
        for queued in [0xcc,0x36,0x40000000]:
            h=Host(air=True);h.prepare_slide();w32(h.actor+0x178,1);w32(h.actor+0x17c,queued);h.tap_slide()
            self.assertEqual(bridge.bridge_queue_calls(),0);self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(r32(h.actor+0x17c),queued)
        h=Host(air=True);h.prepare_slide();w32(h.game+0x2d53a40,0x36);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),0)
    def test_slide_waits_for_native_queue_commit_before_movement(self):
        h=Host(air=True,control_mode=3);h.prepare_slide();h.tap_slide();self.assertEqual(h.move()[0],[1.,2.,3.,4.])
        bridge.bridge_commit(h.actor);h.clock(0.);self.assertEqual(h.move()[0],[16.,0.,0.,16.])
    def test_slide_pauses_at_zero_delta_and_aborts_invalid_delta(self):
        h=Host(air=True);h.prepare_slide();h.tap_slide();self.assertEqual(h.move(0.)[0],[0.,0.,0.,0.]);self.assertEqual(h.body(10),h.expected_variant(10))
        self.assertEqual(h.move()[0],[16.,0.,0.,16.])
        for dt in [-1.,float('nan'),5.]:
            h=Host(air=True);h.prepare_slide();h.tap_slide();self.assertEqual(h.move(dt)[0],[1.,2.,3.,4.]);self.assertEqual(h.body(10),h.expected(10,1))
    def test_damage_landing_and_unequip_cancel_slide_without_granting_defense(self):
        for state,request,height in [(0,7,0),(2,0x48,100),(3,0x4c,100),(2,0xcc,100)]:
            h=Host(air=True);h.prepare_slide();h.tap_slide();flags=r32(h.actor);h.control(state=state,request=request,height=height)
            self.assertEqual(h.move()[0],[1.,2.,3.,4.]);self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(r32(h.actor),flags)
        h=Host(air=True);h.prepare_slide();h.tap_slide();h.equip(False);h.frame();self.assertEqual(h.move()[0],[1.,2.,3.,4.])
        w32(h.actor+0x164,0);h.frame();h.assert_all(self,False);h.native_super_glide();self.assertEqual(r32(h.actor+0x70),21)
    def test_temporary_model_unload_cannot_resume_old_slide_travel(self):
        h=Host(air=True);h.prepare_slide();h.tap_slide();w32(h.actor+0x374,0);h.frame();w32(h.actor+0x374,1);h.frame()
        self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(h.move()[0],[1.,2.,3.,4.])
    def test_slide_and_spell_recovery_keep_native_events_headers_glide_and_reactions(self):
        h=Host(air=True,encoded_fields=True);h.prepare_slide();h.tap_slide()
        for slot in [10,54,55,57,79,80,82]:
            raw=h.body(slot);original=h.runtime_originals[slot]
            self.assertEqual(raw[:80],original[:80]);source=(ROOT/f"fixtures/original_{h.record_by_slot[slot]['fixture_stem']}.bin").read_bytes();at=struct.unpack_from('<I',source,60)[0];self.assertEqual(raw[at:],original[at:])
        for slot,p in h.native_glide_motions.items():self.assertEqual(C.string_at(p,len(h.native_glide_originals[slot])),h.native_glide_originals[slot])
        for slot,(p,raw) in h.native_reactions.items():self.assertEqual(C.string_at(p,len(raw)),raw)
        self.assertEqual(r32(h.actor+0x1d8),h.original_request_handle)
    def test_default_superglide_alias_exact_and_scoped_in_both_banks(self):
     for bank in [98,60]:
      h=Host(slot=bank,encoded_fields=True);h.prepare_slide();slot=10 if bank==98 else h.record_by_slot[10]['olympus_slot'];old=r32(h.array+slot*4);h.tap_slide()
      alias=r32(h.array+slot*4);self.assertEqual(h.decode(alias),h.native_glide_motions[76]);self.assertNotEqual(old,alias)
      h.clock(39);h.control();self.assertEqual(r32(h.array+slot*4),old)
    def test_once_per_airtime_survives_completion_release_damage_and_style_toggle(self):
     h=Host();h.prepare_slide();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.clock(39);h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.control(state=3,request=0x48);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.equip(False);w32(h.actor+0x164,0);h.frame();h.equip(True);h.frame();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_landing_while_other_style_selected_restores_budget(self):
     h=Host();h.prepare_slide();h.tap_slide();h.clock(39);h.control();h.equip(False);w32(h.actor+0x164,0);h.frame()
     h.control(state=0,request=0,height=0);h.observe();h.equip(True);h.frame();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_foreign_native_superglide_body_prevents_alias_and_does_not_spend_dash(self):
     h=Host();h.prepare_slide();motion=h.native_glide_motions[76];at=r32(motion+40);old=C.string_at(motion+at,1);put(motion+at,bytes([old[0]^1]));h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),0)
     put(motion+at,old);h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
    def test_ui_installer_checks_actual_executable_anchors_and_expands_all_tables(self):
     h=Host();anchors=h.ui_seed();self.assertTrue(h.ui_init());self.assertTrue(bridge.call_int0(h.symbols['StylesMenuReady']))
     h.ui_call('styles_root_init');storage=r64(h.symbols['styles_storage']);count=r32(h.game+0x2e1f4c8);self.assertEqual(count,9)
     self.assertEqual(list((C.c_uint*9).from_address(storage)),[0,1,2,8,3,4,5,6,7])
     self.assertEqual(r32(storage+0x40+8*4),0xff00);self.assertEqual(r64(storage+0x80+8*8),r64(storage+0x80+2*8));self.assertEqual(r64(storage+0xd0+8*8),h.symbols['styles_enter'])
    def test_ui_last_anchor_or_protection_failure_publishes_nothing(self):
     for kind in ['anchor','protect']:
      h=Host();anchors=h.ui_seed()
      if kind=='anchor':put(h.game+anchors[-1][0],b'\xcc')
      else:bridge.bridge_magic_modes(0,0,2)
      sites=[(r,n) for r,n in anchors]+[(0x2dae20,15),(0x311c56,16),(0x2d0970,21),(0x52af20,8)]
      before=[C.string_at(h.game+r,n) for r,n in sites];self.assertFalse(h.ui_init());self.assertEqual(before,[C.string_at(h.game+r,n) for r,n in sites])
    def test_ui_normal_abilities_filters_only_styles_and_native_row_write_commits_correct_id(self):
     h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97,6,21])+bytes(43));w=h.ui_window();h.ui_call('abilities_enter',w)
     # Execute the real native prologue and our R12 bridge; toggle visible row1.
     tail=bytes.fromhex('418074244180')+h.ui_tail;put(h.game+0x311c66,tail);h.ui_call('styles_list',w)
     self.assertEqual(h.abilities()[:6],bytes([6,0x17,6,21,117,0]));self.assertEqual(r32(h.game+0x2e9cbc8),4)
    def test_ui_styles_has_all_eleven_and_selects_single_f_exclusively(self):
     h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97,21])+bytes(44));w=h.ui_window();h.ui_call('styles_enter',w)
     # Display order is Singles A-F, Duals A-D, Anti; Single F is row5.
     put(h.game+0x311c66,bytes.fromhex('418074244580')+h.ui_tail);h.ui_call('styles_list',w)
     self.assertEqual(h.abilities()[:5],bytes([6,0x97,21,116,0]));self.assertEqual(r32(h.game+0x2e9cbc8),11)
     p=h.symbols['styles_shadow']+0x44;self.assertEqual(C.string_at(p,11),bytes([252,251,248,247,245,116,254,253,249,246,250]))
     # Unequip and re-equip that same row; both paths must work.
     h.ui_call('styles_list',w);self.assertEqual(h.abilities()[3],244);h.ui_call('styles_list',w);self.assertEqual(h.abilities()[3],116)
    def test_ui_legacy_save_compacts_ten_style_rows_without_losing_duplicate_natives(self):
     h=Host();h.ui_seed();self.assertTrue(h.ui_init());native=bytes([6,0x86,21,0x97]*9+[55]);old=native+bytes(range(117,127));put(h.save+0x44,old+b'\0')
     h.ui_call('StylesMenuFrame');out=h.abilities();self.assertEqual(out[:37],native);self.assertEqual(out[37],125);self.assertEqual(out[38:],bytes(10))
    def test_ui_full_or_malformed_native_ability_lists_are_never_evicted(self):
     for data in [bytes([6]*47+[0]),bytes([6,0,0x97])+bytes(45)]:
      h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,data);h.ui_call('StylesMenuFrame');self.assertEqual(h.abilities(),data)

    def test_main_all_motions_round_trip_both_banks_and_native_request_table(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.frame();h.assert_all(self,0);h.equip(True);h.frame();h.assert_all(self,1)
            h.equip(False);h.frame();h.assert_all(self,0)
    def test_foreign_early_or_late_motion_blocks_all_body_writes(self):
        for slot in [0,104,117]:
            h=Host();at=h.motions[slot]+r32(h.motions[slot]+40);put(at,bytes([C.c_ubyte.from_address(at).value^1]));before=h.snapshot();h.equip(True);h.frame();self.assertEqual(h.snapshot(),before)
    def test_all_main_magic_families_recover_with_their_matching_clip(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.equip(True);h.frame()
            for start,recovery,slot,wanted in [(0x36,0x3d,57,True),(0x37,0x3d,57,True),(0x3a,0x3d,57,True),(0x38,0x3d,57,False),(0x39,0x3d,57,False),(0x3b,0x3d,57,False),(0x3c,0x3d,57,False),(0x83,0x8a,82,True),(0x84,0x8a,82,True),(0x87,0x8a,82,True),(0x85,0x8a,82,False),(0x86,0x8a,82,False),(0x88,0x8a,82,False),(0x89,0x8a,82,False)]:
                h.control(state=2,request=start);h.control(state=2,request=recovery);self.assertEqual(h.body(slot),h.expected_variant(slot) if wanted else h.expected(slot,1))
    def test_native_menu_title_and_normal_message_lookup(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w=h.ui_window();h.ui_call('styles_enter',w);w32(h.game+0x2e1f4d0,8)
        ptr=bridge.call_ptr1(h.game+0x2d0970,0xff00);self.assertEqual(C.string_at(ptr,7),bytes([0x3d,0x58,0x5d,0x50,0x49,0x57,0]))
        ptr2=bridge.call_ptr1(h.game+0x2d0970,0xbd);self.assertEqual(ptr,ptr2)
        offsets=h.buffer(bytes([0,0,3,0]));text=h.buffer(b'abcNative\0');w64(h.game+0x2e1ac50,offsets);w64(h.game+0x2e1ac48,text)
        self.assertEqual(bridge.call_ptr1(h.game+0x2d0970,2),text+3)

    def test_terra_aqua_terra_switch_restores_bodies_and_lookup_before_next_owner(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True,guard=True,jump=True)
            self.assertTrue(bridge.adapter_init(h.symbols['SingleEInit'],h.game,1))
            h.equip(True);h.frame();h.assert_all(self,1)
            h.equip(False);self.assertTrue(h.frame());h.assert_all(self,0)
            self.assertFalse(bridge.adapter_frame(h.symbols['SingleEFrame'],h.actor,1,1));self.assertNotEqual(h.body(98),h.expected(98,0))
            self.assertTrue(bridge.adapter_frame(h.symbols['SingleEFrame'],h.actor,0,2));h.assert_all(self,0)
            h.equip(True);h.frame();h.assert_all(self,1)
    def test_native_abilities_for_other_party_members_use_original_record(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97])+bytes(45));put(h.save+0x74+0x44,bytes([7,0x88,0])+bytes(45));w32(h.game+0x2e9cbcc,2)
        w=h.ui_window(1);h.ui_call('abilities_enter',w);put(h.game+0x311c66,bytes.fromhex('418074244080')+h.ui_tail);h.ui_call('styles_list',w)
        self.assertEqual(C.string_at(h.save+0x74+0x44,3),bytes([0x87,0x88,0]));self.assertEqual(h.abilities()[:4],bytes([6,117,0x97,0]))
    def test_root_menu_keeps_last_selected_native_option_after_styles_insert(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w32(h.game+0x2e1f4d0,6);h.ui_call('styles_root_init');w=h.ui_window();h.ui_call('styles_root',w)
        self.assertEqual(r32(h.game+0x2e1f4cc),7);self.assertEqual(C.c_ushort.from_address(w+0xfe).value,7<<4);self.assertEqual(C.c_ushort.from_address(w+0xf8).value,9)
    def test_external_native_ability_change_cannot_be_overwritten_by_stale_view(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97])+bytes(45));w=h.ui_window();h.ui_call('styles_enter',w)
        put(h.symbols['styles_shadow']+0x44+5,bytes([116]));new=bytes([6,117,0x97,42])+bytes(44);put(h.save+0x44,new)
        h.ui_call('styles_page',w);self.assertEqual(h.abilities(),new)

    def test_model_unload_restores_alias_and_main_readmits_without_resetting_air_budget(self):
        h=Host();h.prepare_slide();slot=10;original=r32(h.array+slot*4);h.tap_slide();w32(h.actor+0x374,0);h.frame()
        self.assertEqual(r32(h.array+slot*4),original);w32(h.actor+0x374,1);h.frame();h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
        h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_returning_resource_array_recovers_its_temporary_pointer_lease(self):
        h=Host();h.prepare_slide();array=h.array;handle=r32(h.actor+0x1d4);original=r32(array+40);h.tap_slide()
        h.activate_bank(False,True);w32(h.actor+0x164,0);h.frame();self.assertNotEqual(r32(array+40),original)
        w32(h.actor+0x1d4,handle);h.observe();h.frame();self.assertEqual(r32(array+40),original)
        h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_reported_square_marker_bits_are_accepted_and_preserved(self):
        h=Host();h.prepare_slide();h.control(down=0x00140010,pressed=0x00140010,tilt=1,x=1)
        self.assertEqual(bridge.bridge_queue_calls(),1);self.assertEqual(bridge.bridge_control_word(0)&0x00140000,0x00140000)
        self.assertEqual(r32(h.game+0x298ca94),0x00140010)
    def test_full_native_list_rejects_style_selection_without_losing_abilities(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());data=bytes([6]*47+[0]);put(h.save+0x44,data);w=h.ui_window();h.ui_call('styles_enter',w)
        put(h.game+0x311c66,bytes.fromhex('418074244580')+h.ui_tail);h.ui_call('styles_list',w);self.assertEqual(h.abilities(),data)
        self.assertEqual(C.c_ubyte.from_address(h.symbols['styles_shadow']+0x44+5).value,244)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RuntimeTests))
 report={'passed':result.wasSuccessful(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'executed_final_integrated_pe_c_adapter':True,'native_ability_record_prologue_executed':True,'native_menu_references_checked_against_supplied_executable':True,'rendering_and_rust_dispatch_mocked':True,'windows_or_game_executed':False}
 Path(os.environ.get('VALIDATION_OUT',str(TEST_ROOT/'runtime_validation.json'))).write_text(json.dumps(report,indent=2)+'\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)
