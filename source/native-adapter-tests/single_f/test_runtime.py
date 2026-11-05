"""Run the final combined PE's C adapter with Win64 ABI mocks on Linux.

Rust DllMain, shared Rust dispatch and rendering are not executed. Private
source fixtures are provided through the documented environment variables.
"""
from pathlib import Path
import ctypes as C,json,struct,subprocess,sys,unittest,os,math,re
ROOT=Path(os.environ['TERRA_SOURCE']).resolve()
TEST_ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(TEST_ROOT if (TEST_ROOT/'reverse_grip.py').exists() else TEST_ROOT.parents[3]/'tools/ventus-retarget'))
from reverse_grip import reverse_native_grip
NUMBERED_HEADER=Path(os.environ.get('NUMBERED_PASSIVES_HEADER',str(TEST_ROOT/'numbered_passives.h' if (TEST_ROOT/'numbered_passives.h').exists() else TEST_ROOT.parents[1]/'src/single_f/numbered_passives.h')))
TEST_COUNT=int(re.search(r'#define ANIMATION_TEST_COUNT (\d+)u',NUMBERED_HEADER.read_text()).group(1))
VENTUS_COUNT=int(re.search(r'#define VENTUS_TEST_COUNT (\d+)u',NUMBERED_HEADER.read_text()).group(1))
TEST_MASK=(1<<TEST_COUNT)-1
ALL_NUMBERED=((1<<51)-1)&~(1<<49)
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
for name,args,ret in [('bridge_menu_reset',[],None),('bridge_menu_text',[],C.c_char_p),('bridge_menu_panel_count',[],C.c_uint),('bridge_menu_sound',[],C.c_uint),('bridge_menu_rect_count',[],C.c_uint),('bridge_menu_glyph_count',[],C.c_uint),('bridge_menu_scroll_count',[],C.c_uint),('bridge_menu_rect_word',[C.c_uint,C.c_uint],C.c_int)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
for name,args,ret in [('bridge_gpu_reset',[],None),('bridge_gpu_count',[],C.c_uint),('bridge_gpu_packet',[C.c_uint],C.c_size_t)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
bridge.call_panel.argtypes=[C.c_size_t,C.c_size_t,C.c_int,C.c_int,C.c_uint];bridge.call_panel.restype=None
bridge.bridge_numbered_saved.argtypes=[];bridge.bridge_numbered_saved.restype=C.c_uint64
bridge.bridge_numbered_save_calls.argtypes=[];bridge.bridge_numbered_save_calls.restype=C.c_uint
for name,args,ret in [('bridge_menu_plain_count',[],C.c_uint),('bridge_menu_plain_word',[C.c_uint,C.c_uint],C.c_int),('bridge_menu_plain_text',[C.c_uint],C.c_size_t)]:
    f=getattr(bridge,name);f.argtypes=args;f.restype=ret
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
        if os.environ.get('VENTUS_SOURCE'):
            known={r['normal_slot'] for r in self.all_records}
            self.all_records += [r for r in json.loads((Path(os.environ['VENTUS_SOURCE'])/'curve_validation.json').read_text())['motions'] if r['normal_slot'] not in known and r['normal_slot']!=75]
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
        raw={r['normal_slot']:self.original_path(r).read_bytes() for r in self.records}
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
            if slot in self.motions:
                self.native_glide_motions[slot]=self.motions[slot];self.native_glide_originals[slot]=self.runtime_originals[slot];continue
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
    def original_path(self,r):
        p=ROOT/f"fixtures/original_{r['fixture_stem']}.bin"
        return p if p.exists() else Path(os.environ['VENTUS_SOURCE'])/f"fixtures/original_{r['fixture_stem']}.bin"
    def body(self,slot=98):return C.string_at(self.motions[slot],len(self.runtime_originals[slot]))
    def expected(self,slot,on):
        r=self.record_by_slot[slot];folder=ROOT/'fixtures'
        if int(on)==2 and os.environ.get('VENTUS_SOURCE'):
            return self.expected_from(slot,Path(os.environ['VENTUS_SOURCE'])/f"fixtures/ventus_{r['fixture_stem']}.bin")
        if int(on)>=3 and os.environ.get('VENTUS_TEST_SOURCE'):
            folder=Path(os.environ['VENTUS_TEST_SOURCE'])/f'p{int(on)+63}'/'fixtures' if slot in range(98,105) else Path(os.environ['VENTUS_TEST_SOURCE'])/'common/fixtures'
            path=folder/f"ventus_{r['fixture_stem']}.bin"
            return self.expected_from(slot,path if path.exists() else self.original_path(r))
        if int(on)>1:
            candidate=ROOT/f'sets/p{int(on)-1}/fixtures'
            if (candidate/f"terra_{r['fixture_stem']}.bin").exists():folder=candidate
            elif (ROOT/f"sets/shared_v2/fixtures/terra_{r['fixture_stem']}.bin").exists():folder=ROOT/'sets/shared_v2/fixtures'
        path=folder/f"{'terra' if on else 'original'}_{r['fixture_stem']}.bin"
        return self.expected_from(slot,path if path.exists() else self.original_path(r))
    def expected_from(self,slot,path,reverse=True):
        r=self.record_by_slot[slot];data=bytearray(reverse_native_grip(path.read_bytes()) if reverse and path.name.startswith('ventus_') else path.read_bytes())
        data[:80]=self.runtime_originals[slot][:80]
        event_at=struct.unpack_from('<I',self.original_path(r).read_bytes(),60)[0]
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
for name,args,ret in [('adapter_init',[C.c_size_t,C.c_size_t,C.c_int],C.c_int),('adapter_frame',[C.c_size_t,C.c_size_t,C.c_int,C.c_uint64],C.c_int),('adapter_control',[C.c_size_t]*3,None),('adapter_observe',[C.c_size_t]*2,None),('call_int0',[C.c_size_t],C.c_int),('call_ptr1',[C.c_size_t]*2,C.c_size_t),('call_void1',[C.c_size_t]*2,None),('call_ptr2',[C.c_size_t]*3,C.c_size_t)]:
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
 def expected_variant(self,slot):return self.expected_from(10,Path(os.environ['VENTUS_SOURCE'])/'variants/dash/fixtures/ventus_s010.bin',reverse=False) if slot==10 else super().expected_variant(slot)
 def finish_slide(self):
  for i in range(40):
   if not r32(self.symbols['slide_active']):return
   self.move()
  raise AssertionError('Dash exceeded its movement duration')
 def ui_seed(self):
  exe=Path(os.environ['KH1_EXE']).read_bytes();pe=struct.unpack_from('<I',exe,60)[0];sh=pe+24+struct.unpack_from('<H',exe,pe+20)[0];sects=[struct.unpack_from('<4I',exe,sh+i*40+8) for i in range(struct.unpack_from('<H',exe,pe+6)[0])]
  def raw(r,n):
   for vs,va,rs,rp in sects:
    if va<=r and r+n<=va+rs:return exe[rp+r-va:rp+r-va+n]
   raise AssertionError(hex(r))
  self.ui_raw=raw
  anchors=[]
  import re
  for line in Path(os.environ.get('STYLES_SLOT_ANCHORS',str(Path(__file__).resolve().parents[2]/'src/single_f/styles_slots_anchors.h'))).read_text().splitlines():
   if line.startswith('{0x'):
    r=int(line.split('u,',1)[0][1:],16);anchors.append((r,32));put(self.game+r,raw(r,32))
  for line in (Path(os.environ.get('STYLES_MENU_ANCHORS',str(Path(__file__).resolve().parents[2]/'src/single_f/styles_menu_anchors.h')))).read_text().splitlines():
   if line.startswith('{0x'):
    values=line.split(',',6);r=int(values[0][1:],16);n=int(values[1]);anchors.append((r,n));put(self.game+r,raw(r,n))
  for r,n in [(0x2dae20,15),(0x311c56,16),(0x2d0970,21),(0x311f9e,15),(0x310d26,5),(0x31127c,5),(0x2e4325,14),(0x2e5220,34)]:put(self.game+r,raw(r,n))
  put(self.game+0x53bd10,raw(0x53bd10,96))
  for r,f in [(0x52af20,0x2d3840),(0x5490f0,0x310ef0),(0x5490c0,0x310b60),(0x549090,0x310a90)]:
   data=bytearray(raw(r,48));struct.pack_into('<Q',data,0,self.game+f);struct.pack_into('<Q',data,8,0);put(self.game+r,data)
  # Relocate native definition/callback tables as a normal loaded executable.
  for r,n in [(0x52ad40,32),(0x52ad60,64),(0x52ada0,64),(0x52ade0,32),(0x52afb8,32)]:
   data=bytearray(raw(r,n))
   if r in [0x52ad60,0x52ada0]:
    for i in range(0,n,8):struct.pack_into('<Q',data,i,struct.unpack_from('<Q',data,i)[0]-0x140000000+self.game)
   put(self.game+r,data)
  w32(self.game+0x2e941d0,3);put(self.save+0x48e,b'\0\x01\x02');put(self.game+0x545360,raw(0x545360,64));put(self.game+0x52a8d0,raw(0x52a8d0,80))
  # A native function with the exact admitted prologue; unrelated page creation
  # and drawing are host mocks. The original ability pointer arithmetic runs.
  put(self.game+0x2dae2f,b'\xc3');put(self.game+0x310ef0,b'\xc3');put(self.game+0x310b60,b'\xc3');put(self.game+0x2d3840,b'\xc3')
  put(self.game+0x311c20,raw(0x311c20,0x36))
  # Tail returns the selected view record, retaining original native callee saves.
  self.ui_tail=bytes.fromhex('4c89e04881c498000000415e415c5f5dc3')
  put(self.game+0x311c66,self.ui_tail)
  put(self.game+0x310a90,b'\x48\xb8'+struct.pack('<Q',self.game+0x311c20)+b'\xff\xe0')
  w32(self.game+0x2e9cb80,0);w32(self.game+0x2e1f4c8,8);put(self.game+0x2e1f4a8,struct.pack('<8I',*range(8)))
  return anchors
 def ui_init(self):
  ok=bridge.call_int0(self.symbols['StylesMenuInit'])
  if ok:
   # Rendering/navigation are mocks; real focus, selected-row, confirmation,
   # and close-chain leaf routines execute from the admitted native EXE.
   for r,n in [(0x311850,0x150),(0x2e5a40,0x2e3),(0x2e2de0,5),(0x2e2e40,5),(0x28f8f0,0x19),(0x2e8120,0x20),(0x2e8660,0x86)]:put(self.game+r,self.ui_raw(r,n))
   for r,n in [(0x2e5220,34),(0x2ef470,26),(0x2f0340,223),(0x2e3d10,50),(0x2ef440,48),(0x2ef550,11),(0x2ef560,47),(0x2f0510,125)]:put(self.game+r,self.ui_raw(r,n))
   put(self.game+0x2d9920,b'\xc3')
   for r,name in [(0x2d0e10,b'NativeMenuWidth'),(0x38adc0,b'NativeDecode'),(0x2ebcd0,b'NativeMenuPlainText'),(0x2f2430,b'NativeMenuApPanel'),(0x2e7d20,b'NativeMenuPanel'),(0x17a040,b'NativeMenuSound'),(0x2ef670,b'NativeMenuNav'),(0x2f3810,b'NativeMenuPill'),(0x2f3a80,b'NativeMenuRect'),(0x2d5da0,b'NativeMenuGlyph'),(0x2f0cd0,b'NativeMenuClip'),(0x2f0790,b'NativeMenuUnclip'),(0x2f4d10,b'NativeMenuScroll')]:
    put(self.game+r,b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(name))+b'\xff\xe0')
   self.ui_pad=self.buffer(bytes(24));w64(self.game+0x2e95940,self.ui_pad);w32(self.game+0x5456a0,0x20);w32(self.game+0x5456a4,0x40)
  return ok
 def ui_call(self,name,arg=0):bridge.call_void1(self.symbols[name],arg)
 def ui_window(self,slot=0):
  w=self.buffer(bytes(0x200));w32(w+0x48,slot);w32(w+0xb8,2);w32(w+0xdc,0x700*16);w32(w+0xe0,0x740*16);return w
 def ui_page_frame(self,w,pressed=0):
  w64(self.game+0x2e941c0,w);w32(self.ui_pad+8,pressed);bridge.bridge_menu_reset();self.ui_call('styles_page',w)
  return bridge.bridge_menu_text().decode()
 def ui_choose(self,w,row):
  C.c_ushort.from_address(w+0xfc).value=max(0,row-7)*16;C.c_ushort.from_address(w+0xfe).value=min(row,7)*16;return self.ui_page_frame(w,0x20)
 def intrinsic_seed(self):
  if not hasattr(self,'ui_raw'):self.ui_seed()
  put(self.game+0x284be0,self.ui_raw(0x284be0,0x4b))
  put(self.game+0x38adc0,b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(b'NativeDecode'))+b'\xff\xe0')
 def intrinsic_init(self,enabled=True):return bridge.call_ptr1(self.symbols['IntrinsicAbilitiesInit'],int(enabled))
 def intrinsic_frame(self,enabled=True):bridge.call_void1(self.symbols['IntrinsicAbilitiesFrame'],int(enabled))
 def ability_count(self,id,member=0):return bridge.bridge_ability_count(self.game+0x284be0,id,member)
 def numbered_init(self,bits=0):bridge.call_ptr2(self.symbols['NumberedPassivesInit'],bits,bridge.bridge_symbol(b'NumberedPersist'))
 def passive_table(self):
  def encode(text):return bytes([1 if c==' ' else ord(c)-ord('A')+0x2b if 'A'<=c<='Z' else ord(c)-ord('a')+0x45 if 'a'<=c<='z' else ord(c)-ord('0')+0x21 if '0'<=c<='9' else 0x68 for c in text])+b'\0'
  text=bytearray(127*192);table=bytearray(127*12)
  for id in range(1,128):
   name=str(id) if 66<=id<=114 or id==127 else 'Native '+str(id);help='Native help.'
   for at,value in [(id*192-192,name),(id*192-96,help)]:
    encoded=encode(value);text[at:at+len(encoded)]=encoded
  text_ptr=self.buffer(text);self.passive_text_ptr=text_ptr
  for id in range(1,128):
   at=(id-1)*12;table[at]={6:3,7:2,23:1}.get(id,0)
   struct.pack_into('<I',table,at+4,bridge.bridge_encode(text_ptr+(id-1)*192));struct.pack_into('<I',table,at+8,bridge.bridge_encode(text_ptr+(id-1)*192+96))
  w64(self.game+0x2d36d48,self.buffer(table));w32(self.game+0x2e942c4,30)
 def passive_setup(self,abilities=None):
  self.ui_seed();assert self.ui_init();self.passive_table();self.intrinsic_seed();self.numbered_init()
  if abilities is not None:put(self.save+0x44,bytes(abilities)+bytes(48-len(abilities)))
  assert self.intrinsic_init();self.ui_call('StylesMenuFrame');root=self.ui_window();self.ui_call('styles_enter',root);page=r64(self.symbols['styles_custom_page']);self.ui_page_frame(page)
  self.ui_page_frame(page,0x4000);self.ui_page_frame(page,0x20);return root,page

class RuntimeTests(unittest.TestCase):
    def g_prepare(self,bank=98):
        h=Host(slot=bank,encoded_fields=True);h.want=2;h.frame();h.control(state=0,request=0,height=0);h.control();return h
    def g_variant(self,h,kind,slot):
        return h.expected_from(slot,Path(os.environ['VENTUS_SOURCE'])/f"variants/{kind}/fixtures/ventus_s{slot:03}.bin")

    def test_type_g_motion_rate_reaches_the_real_shared_native_motion_hook(self):
        h=Host(guard=True,jump=True,encoded_fields=True)
        self.assertEqual(bridge.adapter_init(h.symbols['SingleEInit'],h.game,1),1)
        h.want=2;h.frame();h.control(state=0,request=0,height=0);h.control();h.tap_slide()
        self.assertEqual(bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.),0x5678)
        self.assertAlmostEqual(bridge.bridge_motion_delta(),4./3.,places=6)
        h.clock(38.9);bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
        self.assertGreaterEqual(bridge.bridge_motion_delta(),0.);self.assertLess(bridge.bridge_motion_delta(),.1)
        h.finish_slide();bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
        self.assertEqual(bridge.bridge_motion_delta(),1.)

    def test_type_f_copied330_uses_g_timing_with_one_point_five_g_distance(self):
        for bank in [98,60]:
            for dt in [.5,1.,2.5]:
                h=Host(slot=bank,guard=True,jump=True,encoded_fields=True)
                self.assertEqual(bridge.adapter_init(h.symbols['SingleEInit'],h.game,1),1)
                h.prepare_slide();h.tap_slide()
                bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.)
                self.assertAlmostEqual(bridge.bridge_motion_delta(),4./3.,places=6)
                distance=0.;elapsed=0.
                while r32(h.symbols['slide_active']):
                    movement=h.move(dt)[0];distance+=movement[0];elapsed+=movement[0]/24.
                self.assertAlmostEqual(elapsed,29.25);self.assertAlmostEqual(distance,468.*1.5)
                self.assertEqual(h.body(10),h.expected(10,1))
                bridge.bridge_motion_advance(h.game+0x29f0a0,h.actor,1.);self.assertEqual(bridge.bridge_motion_delta(),1.)

    def test_type_g_both_actions_finish_in_three_quarters_the_previous_time(self):
        for button,lift in [(0x10,0.),(6,-43.875)]:
            for dt in [.5,1.,2.5]:
                h=self.g_prepare();h.control(down=button,pressed=button,x=1,tilt=1)
                elapsed=0.;distance=0.;rise=0.
                while r32(h.symbols['slide_active']):
                    movement=h.move(dt)[0];distance+=movement[0];rise+=movement[1];elapsed+=movement[0]/16.
                self.assertAlmostEqual(elapsed,29.25);self.assertAlmostEqual(distance,468.);self.assertAlmostEqual(rise,lift)

    def test_type_g_dash330_has_double_old_speed_and_one_point_five_distance_until_landing(self):
        for bank in [98,60]:
            for dt in [.5,1.,2.5]:
                h=self.g_prepare(bank);h.tap_slide();self.assertEqual(h.body(10),self.g_variant(h,'dash',10))
                distance=0.
                while r32(h.symbols['slide_active']):
                    distance+=h.move(dt)[0][0]
                self.assertAlmostEqual(distance,468.,places=4);self.assertEqual(h.body(10),h.expected(10,2))
                calls=bridge.bridge_queue_calls();h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),calls)
                h.control(state=0,request=0,height=0);h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),calls+1)

    def test_type_g_circle410_has_lift_once_per_airtime_and_retains_held_glide038(self):
        h=self.g_prepare();h.control(down=6,pressed=6,tilt=1,x=1)
        self.assertEqual(h.body(10),self.g_variant(h,'dodge',10));self.assertEqual(bridge.call_ptr1(h.symbols['SingleGAction'],h.actor),2)
        lift=0.
        while r32(h.symbols['slide_active']):lift+=h.move()[0][1]
        self.assertAlmostEqual(lift,-43.875);self.assertEqual(h.body(10),h.expected(10,2))
        h.control();calls=bridge.bridge_queue_calls();h.control(down=6,pressed=6)
        self.assertEqual(bridge.bridge_queue_calls(),calls);self.assertEqual(bridge.bridge_control_word(0)&6,6)
        self.assertEqual(bridge.call_ptr1(h.symbols['SingleFSuppressGlide'],h.actor),0)
        self.assertEqual(C.string_at(h.native_glide_motions[75],len(h.native_glide_originals[75])),h.native_glide_originals[75])
        h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),calls+1)

    def test_type_g_both_air_buttons_exclude_shortcuts_grounding_damage_and_scripted_actions(self):
        for button in [6,0x10]:
            for flags in ['shortcut','ground','damage','script']:
                h=self.g_prepare()
                if flags=='script':w32(h.actor+0x444,1)
                h.control(down=button|(0x40000 if flags=='shortcut' else 0),pressed=button,state=0 if flags=='ground' else 2,request=0x6e if flags=='damage' else 6,height=0 if flags=='ground' else 100,x=1,tilt=1)
                self.assertEqual(bridge.bridge_queue_calls(),0);self.assertEqual(r32(h.symbols['slide_active']),0)
                self.assertEqual(h.body(10),h.expected(10,2))

    def test_type_g_dash_faces_the_initial_direction_through_release_and_steering(self):
        h=self.g_prepare();h.tap_slide(x=1,z=0)
        for x,z in [(-1,0),(0,1),(0,0)]:
            h.control(tilt=1,x=x,z=z);self.assertEqual(h.move()[0],[16.,0.,0.,16.])
            self.assertAlmostEqual(C.c_float.from_address(h.actor+0x30).value,1.)
            self.assertAlmostEqual(C.c_float.from_address(h.actor+0x38).value,0.)

    def test_type_g_ground_jump_press_requires_release_before_circle_dodge(self):
        h=self.g_prepare();h.control(down=6,pressed=6,state=0,request=0,height=0)
        h.control(down=6,pressed=6,state=1,request=4,height=100)
        self.assertEqual(bridge.bridge_queue_calls(),0)
        h.control();h.control(down=6,pressed=6)
        self.assertEqual(bridge.bridge_queue_calls(),1)

    def test_type_g_cast_recovery_uses416_417_only_for_fire_blizzard_gravity(self):
        h=self.g_prepare()
        for start,recovery,slot,kind,wanted in [(0x36,0x3d,57,'ground_cast',True),(0x37,0x3d,57,'ground_cast',True),(0x3a,0x3d,57,'ground_cast',True),(0x38,0x3d,57,'ground_cast',False),(0x83,0x8a,82,'air_cast',True),(0x84,0x8a,82,'air_cast',True),(0x87,0x8a,82,'air_cast',True),(0x85,0x8a,82,'air_cast',False)]:
            h.control(request=start);h.control(request=recovery)
            self.assertEqual(h.body(slot),self.g_variant(h,kind,slot) if wanted else h.expected(slot,2))
        h.control(state=0,request=0,height=0);h.want=0;h.frame();h.assert_all(self,0)

    def test_type_g_contact_timing_changes_only_float_timestamps_and_restores_on_exit(self):
        h=self.g_prepare()
        for slot in [99,100,101,104]:
            original=self.original_for_events(h,slot);current=h.body(slot);at=struct.unpack_from('<I',original,60)[0];changed=0
            while struct.unpack_from('<I',original,at)[0]!=0xffffffff:
                kind,n,keys=struct.unpack_from('<3I',original,at)
                for i in range(n):
                    off=keys+i*16;self.assertEqual(current[off+4:off+16],original[off+4:off+16]);changed+=current[off:off+4]!=original[off:off+4]
                at+=12
            self.assertGreater(changed,0)
        h.control(state=0,request=0,height=0);h.want=1;h.frame();h.assert_all(self,1)

    def test_type_g_native_on_off_windows_do_not_collapse_after_the_second_swing(self):
        h=self.g_prepare()
        for slot in [99,100,101,104]:
            data=h.body(slot);original=self.original_for_events(h,slot);at=struct.unpack_from('<I',original,60)[0]
            while struct.unpack_from('<I',original,at)[0]!=0xffffffff:
                kind,n,keys=struct.unpack_from('<3I',original,at)
                if kind>>16 in (1,5) and n==2:
                    lo,hi=[struct.unpack_from('<f',data,keys+i*16)[0]for i in range(2)]
                    self.assertGreater(hi,lo);self.assertEqual(h.event(slot,kind>>16,(lo+hi)/2),1)
                at+=12
    def original_for_events(self,h,slot):return h.original_path(h.record_by_slot[slot]).read_bytes()

    def test_type_g_live_glide_stream_changes_cannot_block_entry_exit_or_terra(self):
        # Reproduce the user's rejected request71/field20 without weakening
        # admission for any mapped combo, cast or travel record.
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);p=h.native_glide_motions[75]
            flags=h.decode(r32(p+20));w32(flags,r32(flags)^0x01000000)
            changed=C.string_at(p,len(h.native_glide_originals[75]))
            h.want=2;h.frame();h.assert_all(self,2)
            self.assertEqual(bridge.call_ptr1(h.symbols['SingleGActive'],h.actor),1)
            h.want=0;self.assertTrue(h.frame());h.assert_all(self,0)
            h.want=1;h.frame();h.assert_all(self,1)
            h.want=0;self.assertTrue(h.frame());h.assert_all(self,0)
            self.assertEqual(C.string_at(p,len(changed)),changed)

    def test_failed_type_g_entry_does_not_hold_native_or_another_style_hostage(self):
        h=Host(encoded_fields=True);raw=h.snapshot();p=h.motions[98]
        flags=h.decode(r32(p+20));before=r32(flags);w32(flags,before^1)
        h.want=2;h.frame();self.assertEqual(r32(h.symbols['body_owned']),0)
        h.want=0;self.assertTrue(h.frame())
        # The unrelated bad stream remains untouched. Once the game reloads
        # it, an ordinary Terra admission still works.
        self.assertEqual(r32(flags),before^1);w32(flags,before)
        h.want=1;h.frame();h.assert_all(self,1)

    def test_immutable_glide038_matches_converted_source_without_live_record_writes(self):
        h=Host();p=bridge.call_ptr1(h.symbols['SingleGGlideData'],0);n=bridge.call_ptr1(h.symbols['SingleGGlideBytes'],0)
        source=reverse_native_grip((Path(os.environ['VENTUS_SOURCE'])/'fixtures/ventus_s075.bin').read_bytes())
        data=C.string_at(p,n);self.assertEqual(data[:8],struct.pack('<2I',1,8));self.assertEqual(data[8:12],b'MMTN')
        self.assertEqual(data[8+72:],source)

    def test_type_g_event_descriptor_corruption_blocks_all_body_writes(self):
        h=self.g_prepare();h.control(state=0,request=0,height=0);slot=99;raw=self.original_for_events(h,slot);at=struct.unpack_from('<I',raw,60)[0]
        desc=r32(h.motions[slot]+60);desc=h.decode(desc) if desc&0x80000000 else h.motions[slot]+desc
        w32(desc,r32(desc)^1);before=h.snapshot();h.want=1;h.frame();self.assertEqual(h.snapshot(),before)

    def test_dark_riku_test_passives_use101_104_and_clear_stance_and_ventus_tests(self):
        h=Host();root,page=h.passive_setup([6,119]);h.ui_choose(page,1)
        for index in range(4):
            text=h.ui_choose(page,1+35+index)
            self.assertEqual(bridge.call_ptr1(h.symbols['VentusTestChoice'],0),0)
            self.assertEqual(bridge.call_ptr1(h.symbols['DarkTestChoice'],0),index+1)
            self.assertEqual(r64(h.symbols['numbered_bits']),1<<(35+index));self.assertEqual(h.ability_count(119),0)
            self.assertIn('Dark Riku',text)

    def test_ventus_numbered_profiles_apply_all_records_and_restore_both_banks(self):
        if not os.environ.get('VENTUS_TEST_SOURCE'):self.skipTest('Provide numbered Ventus test fixtures')
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True)
            for choice in range(3,3+VENTUS_COUNT):
                h.want=choice;h.frame();h.assert_all(self,choice)
                self.assertEqual(r32(h.symbols['cache_choice']),choice);self.assertEqual(r32(h.symbols['action_variant_mask']),0)
                h.want=0;self.assertTrue(h.frame());h.assert_all(self,0)

    def test_animation_test_unequips_every_stance_and_preserves_native_flags_ap_and_neighbors(self):
        for stance in [124,123,120,119,117,116,115,126,125,121,118,122]:
            h=Host();root,page=h.passive_setup([6,0x87,stance]);before=C.string_at(h.save,0x1000)
            h.ui_choose(page,2)
            expected=bytearray(before);expected[0x46]=stance|128
            self.assertEqual(C.string_at(h.save,0x1000),bytes(expected));self.assertEqual(h.ability_count(66),1)
            self.assertEqual(bridge.call_ptr1(h.symbols['VentusTestChoice'],0),3)
            self.assertEqual(bridge.call_ptr1(h.game+0x2e8660,0),27)
            for other in [124,123,120,119,117,116,115,126,125,121,118,122]:self.assertEqual(h.ability_count(other),0)

    def test_equipping_each_stance_clears_test_and_preserves_unassigned_numbered_flag(self):
        for row in range(12):
            h=Host();root,page=h.passive_setup([6,117]);h.ui_choose(page,1);h.numbered_init((1<<50)|1)
            h.ui_page_frame(page,0x40);h.ui_page_frame(page,0x1000);h.ui_page_frame(page,0x20);h.ui_choose(page,row)
            self.assertEqual(r64(h.symbols['numbered_bits']),1<<50)
            self.assertEqual(bridge.call_ptr1(h.symbols['VentusTestChoice'],0),0)
            self.assertEqual(sum(h.ability_count(id) for id in [124,123,120,119,117,116,115,126,125,121,118,122]),1)

    def test_only_one_animation_test_can_be_active_and_off_restores_no_stance(self):
        h=Host();root,page=h.passive_setup([6,117])
        for index in range(TEST_COUNT):
            h.ui_choose(page,1+index)
            self.assertEqual(r64(h.symbols['numbered_bits']),1<<index)
            self.assertEqual(bridge.call_ptr1(h.symbols['VentusTestChoice'],0),3+index if index<VENTUS_COUNT else 0)
            self.assertEqual(bridge.call_ptr1(h.symbols['DarkTestChoice'],0),0 if index<VENTUS_COUNT else 1+index-VENTUS_COUNT)
            self.assertEqual(h.abilities()[:3],bytes([6,245,0]))
        h.ui_choose(page,TEST_COUNT)
        self.assertEqual(r64(h.symbols['numbered_bits']),0);self.assertEqual(h.abilities()[:3],bytes([6,245,0]))

    def test_animation_test_selection_rejects_invalid_native_list_without_partial_writes(self):
        h=Host();root,page=h.passive_setup([6,117]);before=h.abilities()
        put(h.save+0x44,bytes([6,0,117])+bytes(45));snapshot=C.string_at(h.save,0x1000)
        h.ui_choose(page,1)
        self.assertEqual(C.string_at(h.save,0x1000),snapshot);self.assertEqual(r64(h.symbols['numbered_bits']),0)

    def test_ventus_profile_all_records_restore_in_normal_and_olympus_banks(self):
        if not os.environ.get('VENTUS_SOURCE'):self.skipTest('Provide converted Ventus fixtures')
        for bank in [98,60]:
            for encoded in [False,True]:
                h=Host(slot=bank,encoded_fields=encoded);self.assertTrue(h.adapter_ready);h.want=2
                self.assertFalse(h.frame());h.assert_all(self,2)
                self.assertEqual(r32(h.symbols['cache_choice']),2);self.assertEqual(r32(h.symbols['action_variant_mask']),0)
                h.want=0;self.assertTrue(h.frame());h.assert_all(self,0)

    def test_ventus_numbered_air_square_is_native_and_does_not_activate_main_dash(self):
        h=Host(encoded_fields=True);h.want=3;h.frame();h.control(down=0x10,pressed=0x10,tilt=1,x=1)
        self.assertEqual(r32(h.symbols['slide_active']),0);self.assertEqual(bridge.bridge_queue_calls(),0)
        self.assertEqual(bridge.bridge_control_word(0)&0x10,0x10);self.assertEqual(h.move()[0],[1.,2.,3.,4.])
        self.assertEqual(bridge.call_ptr1(h.symbols['SingleFSuppressSuperglide'],h.actor),0)
        self.assertEqual(bridge.call_ptr1(h.symbols['SingleFSuppressGlide'],h.actor),0)

    def test_ventus_switch_retires_terra_dash_body_and_never_uses_terra_variants(self):
        if not os.environ.get('VENTUS_SOURCE'):self.skipTest('Provide converted Ventus fixtures')
        h=Host(encoded_fields=True);h.prepare_slide();h.tap_slide();self.assertEqual(r32(h.symbols['slide_active']),1)
        h.want=0;h.frame();self.assertEqual(r32(h.symbols['slide_active']),0)
        h.control(state=0,request=0,height=0);self.assertTrue(h.frame());h.assert_all(self,0)
        h.want=2;h.frame();h.assert_all(self,2);self.assertEqual(r32(h.symbols['action_variant_mask']),0)
        h.want=0;self.assertTrue(h.frame());h.want=1;h.frame();h.assert_all(self,1)

    def test_type_g_menu_uses115_and_legacy_numbered_flag_cannot_equip_it(self):
        h=Host();root,page=h.passive_setup([6,117]);h.numbered_init((1<<49)|(1<<50)|3)
        self.assertEqual(r64(h.symbols['numbered_bits']),(1<<50)|1);self.assertEqual(h.ability_count(115),0);self.assertEqual(h.ability_count(127),1)
        h.ui_page_frame(page,0x40);h.ui_page_frame(page,0x1000);h.ui_page_frame(page,0x20)
        text=h.ui_choose(page,6);self.assertIn('Type G|Single|I',text);self.assertEqual(h.ability_count(115),1)
        self.assertEqual(h.abilities()[:3],bytes([6,115,0]));self.assertEqual(h.ability_count(127),1)
        self.assertEqual(r64(h.symbols['numbered_bits']),1<<50)

    def test_numbered_passives_all_50_ids_are_visible_with_native_rows_without_save_writes(self):
        h=Host();root,page=h.passive_setup([6]*46+[117]);before=C.string_at(h.save,0x1000);seen=set();expected=set(map(str,list(range(66,115))+[127]))
        self.assertEqual(C.c_ushort.from_address(page+0xf8).value,96)
        for row in range(46,96):
            C.c_ushort.from_address(page+0xfc).value=max(0,row-7)*16;C.c_ushort.from_address(page+0xfe).value=min(row,7)*16;text=h.ui_page_frame(page)
            seen.update(set(text.split('|'))&expected);self.assertNotIn('Donald',text);self.assertNotIn('Goofy',text);self.assertNotIn('Shared',text)
        self.assertEqual(seen,expected);self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(bridge.bridge_numbered_save_calls(),0)
        self.assertEqual(r64(page+0x20),0)

    def test_numbered_all_50_flags_toggle_at_zero_ap_with_full_48_native_list(self):
        h=Host();root,page=h.passive_setup([6]*48);before=C.string_at(h.save,0x1000);self.assertEqual(C.c_ushort.from_address(page+0xf8).value,98)
        self.assertEqual(bridge.call_ptr1(h.game+0x2e8660,0),0)
        for i,id in enumerate(list(range(66,115))+[127]):h.ui_choose(page,48+i);self.assertEqual(h.ability_count(id),1)
        self.assertEqual(bridge.bridge_numbered_saved(),(ALL_NUMBERED&~TEST_MASK)|(1<<(TEST_COUNT-1)));self.assertEqual(bridge.bridge_numbered_save_calls(),50);self.assertEqual(C.string_at(h.save,0x1000),before)
        h.ui_choose(page,48+TEST_COUNT-1)
        for i in range(TEST_COUNT,50):
            id=66+i if i<49 else 127;h.ui_choose(page,48+i);self.assertEqual(h.ability_count(id),0)
        self.assertEqual(bridge.bridge_numbered_saved(),0);self.assertEqual(bridge.bridge_numbered_save_calls(),101-TEST_COUNT);self.assertEqual(C.string_at(h.save,0x1000),before)

    def test_direct_passives_native_ap_checks_equipping_removing_and_duplicate_rows(self):
        h=Host();root,page=h.passive_setup([0x86,0x87,117]);w32(h.game+0x2e942c4,3)
        text=h.ui_choose(page,0);self.assertEqual(h.abilities()[:4],bytes([6,0x87,117,0]));self.assertIn('AP Used|3 / 3',text)
        h.ui_choose(page,1);self.assertEqual(bridge.bridge_menu_sound(),4);self.assertEqual(h.abilities()[:4],bytes([6,0x87,117,0]))
        h.ui_choose(page,0);h.ui_choose(page,1);self.assertEqual(h.abilities()[:4],bytes([0x86,7,117,0]));self.assertEqual(bridge.call_ptr1(h.game+0x2e8660,0),1)
        h.ui_choose(page,2);self.assertEqual(h.ability_count(66),1);self.assertEqual(bridge.call_ptr1(h.game+0x2e8660,0),1);self.assertEqual(h.abilities()[:4],bytes([0x86,7,245,0]))

    def test_passives_preserves_native_names_and_help_while_numbered_names_are_decimal(self):
        h=Host();root,page=h.passive_setup([6,117]);text=h.ui_page_frame(page)
        self.assertIn('Native 6',text);self.assertIn('Native help.',text);self.assertIn('|66|AP 0|',text);self.assertNotIn('Type E',text)
        self.assertIn('AP Used|3 / 30',text);self.assertEqual(bridge.bridge_menu_rect_count(),8)

    def test_passives_and_limits_show_the_same_spent_ap_and_refresh_after_toggles(self):
        h=Host();root,page=h.passive_setup([0x86,0x87,117]);before=h.abilities()
        self.assertIn('AP Used|0 / 30',h.ui_page_frame(page))
        self.assertIn('AP Used|3 / 30',h.ui_choose(page,0))
        self.assertIn('AP Used|5 / 30',h.ui_choose(page,1))
        self.assertIn('AP Used|5 / 30',h.ui_choose(page,2))  # Numeric66 is free.
        h.ui_page_frame(page,0x40);text=h.ui_page_frame(page,0x4000)
        self.assertIn('AP Used|5 / 30',text);self.assertIn('No entries available yet',text)
        h.ui_page_frame(page,0x1000);h.ui_page_frame(page,0x20)
        self.assertIn('AP Used|2 / 30',h.ui_choose(page,0))
        self.assertIn('AP Used|0 / 30',h.ui_choose(page,1));self.assertEqual(h.abilities(),before[:2]+bytes([245])+before[3:])
        h.ui_page_frame(page,0x40);self.assertIn('AP Used|0 / 30',h.ui_page_frame(page,0x4000))

    def test_spent_ap_zero_max_overbudget_and_category_scope(self):
        h=Host();root,page=h.passive_setup([6,7,117]);w32(h.game+0x2e942c4,3)
        self.assertIn('AP Used|3 / 3',h.ui_page_frame(page))  # Native clamps overspend.
        w32(h.game+0x2e942c4,0);self.assertIn('AP Used|0 / 0',h.ui_page_frame(page))
        h.ui_page_frame(page,0x40);self.assertIn('AP Used|0 / 0',h.ui_page_frame(page,0x4000))
        self.assertNotIn('AP Used',h.ui_page_frame(page,0x4000))  # Outfits.
        h.ui_page_frame(page,0x1000);h.ui_page_frame(page,0x1000)
        self.assertNotIn('AP Used',h.ui_page_frame(page,0x1000))  # Stance.

    def test_description_uses_native_width_and_fixed_footer_lines_with_white_large_ap(self):
        h=Host();root,page=h.passive_setup([6,117])
        message='Deliver combo attacks even if attacks do not land.'
        encoded=bytes([1 if c==' ' else ord(c)-ord('A')+0x2b if 'A'<=c<='Z' else ord(c)-ord('a')+0x45 if 'a'<=c<='z' else 0x68 for c in message])
        # Native descriptions may request48-unit leading. It must not escape
        # the footer or shrink the explicit AP font/color.
        put(h.passive_text_ptr+5*192+96,bytes([3,48,12,12])+encoded+b'\0')
        h.ui_page_frame(page)
        rows=[([bridge.bridge_menu_plain_word(i,j) for j in range(4)],C.string_at(bridge.bridge_menu_plain_text(i))) for i in range(bridge.bridge_menu_plain_count())]
        help=[(v,t) for v,t in rows if v[0]==174]
        self.assertGreaterEqual(len(help),2)
        self.assertEqual([v[1] for v,_ in help],[309+18*i for i in range(len(help))])
        self.assertTrue(all(v[2]==16 and len(t)*8<=226 and b'\x02' not in t and b'\x03' not in t for v,t in help))
        ap=[(v,t) for v,t in rows if v[0]==414]
        self.assertEqual([(v[1],v[2],v[3]&0xffffffff) for v,t in ap],[(310,16,0x80ffffff),(333,22,0x80ffffff)])
        self.assertIn('AP Used|3 / 30',bridge.bridge_menu_text().decode())
        self.assertLessEqual(max(v[1]+v[2] for v,t in help),361)
        self.assertLessEqual(max(v[1]+v[2] for v,t in ap),355)

    def test_long_native_help_controls_stay_in_footer_and_truncate_cleanly(self):
        h=Host();root,page=h.passive_setup([6,117])
        # Color operands and explicit positions contain low bytes including0.
        # They must be consumed with their commands, not interpreted as text.
        encoded=bytes([8,255,255,255,128,13,50,0,14,90,0,3,48,12,8])
        word=bytes([0x2b,0x56,0x45,0x5e,0x5e,1])
        put(h.passive_text_ptr+5*192+96,encoded+word*25+b'\0');h.ui_page_frame(page)
        rows=[([bridge.bridge_menu_plain_word(i,j) for j in range(4)],C.string_at(bridge.bridge_menu_plain_text(i))) for i in range(bridge.bridge_menu_plain_count())]
        help=[(v,t) for v,t in rows if v[0]==174]
        self.assertEqual([v[1] for v,t in help],[309,327,345]);self.assertTrue(help[-1][1].endswith(bytes([0x68])*3))
        self.assertTrue(all(v[2]==16 and len(t)*8<=226 and all(c>=0x21 or c==1 for c in t) for v,t in help))

    def test_passives_toggles_an_existing_full_list_with_and_without_a_style_token(self):
        for entries in [[6]*48,[6]*47+[117]]:
            h=Host();root,page=h.passive_setup(entries);before=h.abilities();h.ui_choose(page,0)
            self.assertEqual(h.abilities(),bytes([0x86])+before[1:]);self.assertEqual(C.c_ushort.from_address(page+0xf8).value,98 if len(set(entries))==1 else 97)

    def test_numbered_state_load_clamps_bits_and_persists_only_changes(self):
        h=Host();root,page=h.passive_setup([6,117]);h.numbered_init((1<<64)-1);self.assertEqual(bridge.bridge_numbered_save_calls(),0)
        self.assertEqual(r64(h.symbols['numbered_bits']),(ALL_NUMBERED&~TEST_MASK)|1);self.assertEqual(h.ability_count(66),1);self.assertEqual(h.ability_count(127),1)
        h.ui_choose(page,50);self.assertEqual(bridge.bridge_numbered_saved(),(ALL_NUMBERED&~TEST_MASK&~(1<<50))|1);self.assertEqual(bridge.bridge_numbered_save_calls(),1);self.assertEqual(h.ability_count(127),0)
        h.intrinsic_frame();self.assertEqual(bridge.bridge_numbered_save_calls(),2);self.assertEqual(r64(h.symbols['numbered_bits'])&TEST_MASK,0)

    def test_numbered_test_settings_are_mod_wide_and_not_written_into_a_new_save(self):
        h=Host();root,page=h.passive_setup([6,117]);h.ui_choose(page,1);self.assertEqual(h.ability_count(66),1)
        new=h.buffer(bytes(0x1000));put(new+4,b'\x01\x02\x03');w64(h.game+0x2868ba0,new);h.intrinsic_frame();self.assertEqual(h.ability_count(66),1)
        self.assertEqual(C.string_at(new+0x44,48),bytes(48));self.assertEqual(bridge.bridge_numbered_save_calls(),1)

    def test_numbered_legacy_entries_migrate_once_and_keep_existing_mod_flags(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());h.passive_table();h.intrinsic_seed();h.numbered_init(1<<7)
        put(h.save+0x44,bytes([66,0xc2,114,255,127,6,117])+bytes(41));self.assertTrue(h.intrinsic_init())
        self.assertEqual(h.abilities()[:3],bytes([6,117,0]));self.assertEqual(bridge.bridge_numbered_saved(),(1<<48)|(1<<50));self.assertEqual(bridge.bridge_numbered_save_calls(),1)
        h.intrinsic_frame();self.assertEqual(bridge.bridge_numbered_save_calls(),1)

    def test_party_removal_clears_all_nine_ability_arrays_and_preserves_other_save_bytes(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([6,117])+bytes(46))
        for member in range(1,10):put(h.save+member*0x74+0x44,bytes([6,0x86,21,66,127])*9+bytes([26,22,23]))
        before=bytearray(C.string_at(h.save,0x1000));self.assertTrue(h.intrinsic_init());after=bytearray(C.string_at(h.save,0x1000))
        for member in range(1,10):
            off=member*0x74+0x44;self.assertEqual(after[off:off+48],bytes(48));before[off:off+48]=after[off:off+48]=bytes(48)
            for id in [6,21,26,66,127]:self.assertEqual(h.ability_count(id,member),0)
        self.assertEqual(after,before);self.assertEqual(r64(h.symbols['numbered_bits']),0)

    def test_party_reawards_are_blocked_immediately_and_removed_on_next_update(self):
        h=Host();h.intrinsic_seed();self.assertTrue(h.intrinsic_init());off=h.save+3*0x74+0x44;put(off,bytes([6,21])+bytes(46))
        self.assertEqual(h.ability_count(6,3),0);h.intrinsic_frame();self.assertEqual(C.string_at(off,48),bytes(48))
        h.intrinsic_frame(False);put(off,bytes([6])+bytes(47));self.assertEqual(h.ability_count(6,3),1)

    def test_original_native_paging_reaches_id127_beyond_the_48_entry_boundary(self):
        h=Host();root,page=h.passive_setup([6,117]);put(h.game+0x2ef670,h.ui_raw(0x2ef670,0x870))
        for r in [0x2eb370,0x2f1100]:put(h.game+r,b'\xc3')
        put(h.game+0x2eb130,bytes.fromhex('31c0c3'));w32(h.ui_pad+16,0x800);seen=set()
        for i in range(8):seen.update(h.ui_page_frame(page,0x800).split('|'))
        self.assertIn('127',seen);self.assertIn('66',seen);self.assertEqual(C.c_ushort.from_address(page+0xf8).value,51);self.assertEqual(h.abilities()[:3],bytes([6,117,0]))

    def test_numbered_uninstall_disables_virtual_flags_and_keeps_partners_removed(self):
        h=Host();root,page=h.passive_setup([6,117]);h.ui_choose(page,1);self.assertEqual(h.ability_count(66),1);h.intrinsic_frame(False)
        self.assertEqual(h.ability_count(66),0);self.assertEqual(r64(h.symbols['numbered_bits']),1)
        for member in range(1,10):self.assertEqual(C.string_at(h.save+member*0x74+0x44,48),bytes(48))

    def test_native_save_ability_append_stops_at_48_for_sora_and_shared(self):
        h=Host();h.ui_seed();put(h.game+0x284e10,h.ui_raw(0x284e10,0x4e))
        for member,offset in [(0,0x44),(11,0x599)]:
            put(h.save+offset,bytes(48));put(h.save+offset+48,b'\x5a')
            for i in range(48):bridge.call_ptr2(h.game+0x284e10,6,member)
            self.assertEqual(C.string_at(h.save+offset,48),bytes([0x86]*48))
            before=C.string_at(h.save+offset,49);bridge.call_ptr2(h.game+0x284e10,7,member);self.assertEqual(C.string_at(h.save+offset,49),before)

    def test_native_7bit_definition_lookup_resolves_enabled_and_disabled_id127(self):
        h=Host();h.intrinsic_seed();put(h.game+0x28f8f0,h.ui_raw(0x28f8f0,0x19));table=h.buffer(bytes(127*12));w64(h.game+0x2d36d48,table)
        for raw in [127,255]:self.assertEqual(bridge.call_ptr1(h.game+0x28f8f0,raw),table+126*12)
        put(h.save+0x44,bytes([127,255])+bytes(46));self.assertTrue(h.intrinsic_init());self.assertEqual(h.ability_count(127),1)

    def test_intrinsic_seven_abilities_work_without_any_learned_entry(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes(48));put(h.save+0x599,bytes(48));before=C.string_at(h.save,0x1000)
        self.assertTrue(h.intrinsic_init())
        for id in [21,22,26]:self.assertEqual(h.ability_count(id),1)
        for id in [1,2,3,4]:self.assertEqual(h.ability_count(id,11),1)
        self.assertEqual(C.string_at(h.save,0x1000),before)

    def test_intrinsic_compaction_preserves_other_entries_flags_duplicates_and_save_fields(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([21,0x95,22,0x96,26,0x9a,6,6,0x87,117])+bytes(38));put(h.save+0x599,bytes([1,0x81,2,0x82,3,0x83,4,0x84,9,0x8a])+bytes(38))
        before=bytearray(C.string_at(h.save,0x1000));self.assertTrue(h.intrinsic_init());after=bytearray(C.string_at(h.save,0x1000))
        self.assertEqual(h.abilities()[:5],bytes([6,6,0x87,117,0]));self.assertEqual(C.string_at(h.save+0x599,48),bytes([9,0x8a])+bytes(46))
        for off in [0x44,0x599]:before[off:off+48]=bytes(48);after[off:off+48]=bytes(48)
        self.assertEqual(after,before);h.intrinsic_frame();self.assertEqual(h.ability_count(6),2)

    def test_intrinsic_counter_preserves_sora_shared_counts_and_suppresses_other_party(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([21,6,6,0x86,117])+bytes(43));put(h.save+0x599,bytes([1,9,9,0x89])+bytes(44))
        for member in [1,9]:put(h.save+member*0x74+0x44,bytes([21,21,0x96,26])+bytes(44))
        self.assertTrue(h.intrinsic_init())
        self.assertEqual(h.ability_count(6),2);self.assertEqual(h.ability_count(117),1);self.assertEqual(h.ability_count(9,11),2)
        for member in [1,9]:
            self.assertEqual(h.ability_count(21,member),0);self.assertEqual(h.ability_count(22,member),0);self.assertEqual(h.ability_count(26,member),0)
        for member in [0,1]:self.assertEqual(h.ability_count(1,member),0)
        self.assertEqual(h.ability_count(1,10),1)

    def test_intrinsic_native_ap_accounting_refunds_only_sora_builtin_entries(self):
        h=Host();h.intrinsic_seed();put(h.game+0x2e8660,h.ui_raw(0x2e8660,0x86));put(h.game+0x28f8f0,h.ui_raw(0x28f8f0,0x19))
        table=bytearray(127*12)
        for id,cost in [(21,2),(22,1),(26,1),(6,3)]:table[(id-1)*12]=cost
        w64(h.game+0x2d36d48,h.buffer(table));w32(h.game+0x2e942c4,30);w32(h.game+0x2e943c4,30)
        put(h.save+0x44,bytes([21,22,26,6])+bytes(44));put(h.save+0x74+0x44,bytes([21,22,26])+bytes(45))
        ap=lambda member:bridge.call_ptr1(h.game+0x2e8660,member)
        self.assertEqual(ap(0),23);self.assertEqual(ap(1),26);self.assertTrue(h.intrinsic_init())
        self.assertEqual(ap(0),27);self.assertEqual(ap(1),30)

    def test_intrinsic_native_ability_cache_builds_guard_roll_and_shared_movement_bits(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes(48));self.assertTrue(h.intrinsic_init())
        put(h.game+0x2a6380,h.ui_raw(0x2a6380,0x548));bridge.call_void1(h.game+0x2a6380,0)
        self.assertEqual(r32(h.game+0x2d5ec10),0x3f0)
        # Native restrictions still gate physical actions; the mod does not OR
        # cache bits after the original cache builder has made its decision.
        w32(h.game+0x298c9a0,1);bridge.call_void1(h.game+0x2a6380,0)
        self.assertEqual(r32(h.game+0x2d5ec10),0x40)

    def test_intrinsic_native_scan_cache_sets_the_original_actor_flag(self):
        h=Host();h.intrinsic_seed();self.assertTrue(h.intrinsic_init());work=h.glide_work;w32(work+0x184,0x400)
        # Execute the original Scan cache block with its native query and
        # actor-work decode, preserving the host's nonvolatile registers.
        put(h.game+0x2a64a2,h.ui_raw(0x2a64a2,0x2c));put(h.game+0x2a64ce,bytes.fromhex('4883c4205e5f5bc3'))
        shim=h.buffer(bytes.fromhex('5357564883ec204889cf89d6b91a00000048b8')+struct.pack('<Q',h.game+0x2a64a2)+bytes.fromhex('ffe0'))
        bridge.call_ptr2(shim,h.actor,0);self.assertEqual(r32(work+0x184),0x420)

    def test_intrinsic_full_48_entry_lists_compact_without_writing_following_fields(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([6]*45+[21,22,26]));put(h.save+0x599,bytes([9]*44+[1,2,3,4]));put(h.save+0x74,b'\xa5');put(h.save+0x5c9,b'\x5a')
        self.assertTrue(h.intrinsic_init());self.assertEqual(h.abilities(),bytes([6]*45)+bytes(3));self.assertEqual(C.string_at(h.save+0x599,48),bytes([9]*44)+bytes(4))
        self.assertEqual(C.string_at(h.save+0x74,1),b'\xa5');self.assertEqual(C.string_at(h.save+0x5c9,1),b'\x5a')

    def test_intrinsic_full_list_without_targets_and_malformed_lists_are_preserved(self):
        for sora,shared in [(bytes([6]*48),bytes([9]*48)),(bytes([21,0,6])+bytes(45),bytes(48)),(bytes([21])+bytes(47),bytes([1,0,9])+bytes(45))]:
            h=Host();h.intrinsic_seed();put(h.save+0x44,sora);put(h.save+0x599,shared);before=C.string_at(h.save,0x1000)
            self.assertTrue(h.intrinsic_init());self.assertEqual(C.string_at(h.save,0x1000),before)

    def test_intrinsic_admission_checks_the_whole_counter_and_failed_install_keeps_save(self):
        for offset in [0,0x29,0x4a]:
            h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([21,22,26])+bytes(45));put(h.game+0x284be0+offset,bytes([h.ui_raw(0x284be0+offset,1)[0]^1]))
            before=C.string_at(h.save,0x1000);code=C.string_at(h.game+0x284be0,0x4b)
            self.assertFalse(h.intrinsic_init());h.intrinsic_frame();self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(C.string_at(h.game+0x284be0,0x4b),code)

    def test_intrinsic_allocation_and_protection_failure_leave_native_counter_and_lists(self):
        for alloc,protect in [(1,0),(0,1)]:
            h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([21,22,26])+bytes(45));before=C.string_at(h.save,0x1000)
            bridge.bridge_magic_modes(1,alloc,protect);self.assertFalse(h.intrinsic_init());h.intrinsic_frame()
            self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(C.string_at(h.game+0x284be0,0x4b),h.ui_raw(0x284be0,0x4b))

    def test_intrinsic_uninstall_restores_native_entries_without_spending_ap(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([6])+bytes(47));put(h.save+0x599,bytes([9])+bytes(47));self.assertTrue(h.intrinsic_init());h.intrinsic_frame(False)
        self.assertEqual(h.abilities()[:5],bytes([6,0x95,0x96,0x9a,0]));self.assertEqual(C.string_at(h.save+0x599,6),bytes([9,1,2,3,4,0]))
        self.assertEqual(h.ability_count(21),0);self.assertEqual(h.ability_count(1,11),1)
        before=C.string_at(h.save,0x1000);h.intrinsic_frame(False);self.assertEqual(C.string_at(h.save,0x1000),before)
        h.intrinsic_frame(True);self.assertEqual(h.abilities()[:2],bytes([6,0]));self.assertEqual(h.ability_count(21),1)

    def test_intrinsic_uninstall_never_evicts_a_full_native_list(self):
        h=Host();h.intrinsic_seed();put(h.save+0x44,bytes([6]*47+[0]));self.assertTrue(h.intrinsic_init());before=h.abilities();h.intrinsic_frame(False)
        self.assertEqual(h.abilities(),before);self.assertIn(b'could not be restored',bridge.bridge_log());self.assertEqual(h.ability_count(21),0)

    def test_intrinsic_switches_save_identity_and_reclaims_reawarded_entries(self):
        h=Host();h.intrinsic_seed();self.assertTrue(h.intrinsic_init());old=C.string_at(h.save,0x1000)
        new=h.buffer(bytes(0x1000));put(new+4,b'\x01\x02\x03');put(new+0x44,bytes([26,6])+bytes(46));put(new+0x599,bytes([4,9])+bytes(46));w64(h.game+0x2868ba0,new)
        h.intrinsic_frame();self.assertEqual(C.string_at(new+0x44,3),bytes([6,0,0]));self.assertEqual(C.string_at(new+0x599,3),bytes([9,0,0]));self.assertEqual(C.string_at(h.save,0x1000),old)
        put(new+0x45,bytes([0x95]));h.intrinsic_frame();self.assertEqual(C.string_at(new+0x44,3),bytes([6,0,0]))
        put(new+4,b'\0');self.assertEqual(h.ability_count(21),0)

    def test_intrinsic_cleanup_and_customize_keep_one_stance_and_native_passives(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());h.intrinsic_seed();put(h.save+0x44,bytes([21,22,26,6,117])+bytes(43));put(h.save+0x599,bytes([1,2,3,4])+bytes(44));self.assertTrue(h.intrinsic_init())
        h.ui_call('StylesMenuFrame');root=h.ui_window();h.ui_call('styles_enter',root);parent=r64(h.symbols['styles_custom_page']);h.ui_page_frame(parent);h.ui_page_frame(parent,0x4000);h.ui_page_frame(parent,0x20)
        self.assertEqual(C.string_at(h.symbols['styles_shadow']+0x44,3),bytes([6,0,0]));self.assertEqual(h.abilities()[:3],bytes([6,117,0]));self.assertEqual(h.ability_count(21),1)

    def test_slide_fresh_square_plays330_and_release_does_not_shorten_it(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True,air=True);h.prepare_slide();h.tap_slide()
            self.assertEqual(h.body(10),h.expected_variant(10));self.assertEqual(r32(h.actor+0x164),6)
            self.assertEqual(bridge.bridge_queue_calls(),1)
            for i in range(5):
                h.clock(float(i));h.control(state=2,request=6);delta,_=h.move()
                self.assertEqual(delta,[24.,0.,0.,24.]);self.assertEqual(h.body(10),h.expected_variant(10))
            self.assertEqual(bridge.bridge_control_word(0)&0x16,0)
    def test_slide_distance_is_finite_and_independent_of_tick_size(self):
        for dt in [0.25,0.5,1.,1.25,2.5]:
            h=Host(air=True);h.prepare_slide();h.tap_slide();elapsed=0.;total=[0.,0.,0.]
            while elapsed<29.25-1e-5:
                h.clock(elapsed);delta,_=h.move(dt)
                for i in range(3):total[i]+=delta[i]
                elapsed+=min(dt,29.25-elapsed)
            self.assertEqual(total,[702.,0.,0.]);self.assertEqual(h.body(10),h.expected(10,1))
            delta,_=h.move();self.assertEqual(delta,[1.,2.,3.,4.])
    def test_movement_duration_completion_restores_fall_and_release_velocity(self):
        h=Host(air=True);h.prepare_slide();h.tap_slide();h.move();h.finish_slide();h.control(state=2,request=6)
        self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(struct.unpack('<f',C.string_at(h.actor+0x3c0,4))[0],12.)
        self.assertEqual(h.move()[0],[1.,2.,3.,4.])
    def test_slide_locks_initial_analog_direction_and_does_not_write_actor_position(self):
        h=Host(air=True);h.prepare_slide();put(h.actor+0x10,struct.pack('<4f',12.,13.,14.,1.));h.tap_slide(.6,.8)
        h.control(state=2,request=6,tilt=1,x=-1,z=0);delta,_=h.move()
        self.assertAlmostEqual(delta[0],14.4,places=5);self.assertAlmostEqual(delta[2],19.2,places=5)
        self.assertEqual(C.string_at(h.actor+0x10,16),struct.pack('<4f',12.,13.,14.,1.))
        self.assertEqual(delta[1],0.)
    def test_slide_neutral_stick_uses_character_facing(self):
        h=Host(air=True);h.prepare_slide();put(h.actor+0x30,struct.pack('<3f',0.,0.,-1.));h.tap_slide(0,0)
        self.assertEqual(h.move()[0],[0.,0.,-24.,24.])
    def test_dash_facing_stays_at_initial_direction_and_releases_after_end(self):
        for x,z in [(1,0),(0,-1),(-.6,.8),(.6,-.8)]:
            h=Host(control_mode=7);h.prepare_slide();h.tap_slide(x,z);yaw=math.atan2(x,z)
            for _ in range(4):
                # Simulate a native turn between callbacks, and opposite input.
                put(h.actor+0x30,struct.pack('<4f',-x,3.,-z,-yaw));put(h.actor+0x150,struct.pack('<f',-yaw))
                h.control(tilt=1,x=-x,z=-z);h.move()
                face=struct.unpack('<4f',C.string_at(h.actor+0x30,16))
                for a,b in zip(face,[x,0.,z,yaw]):self.assertAlmostEqual(a,b,places=5)
                self.assertAlmostEqual(C.c_float.from_address(h.actor+0x150).value,yaw,places=5)
            h.finish_slide();put(h.actor+0x30,struct.pack('<4f',0.,0.,1.,0.));h.control()
            self.assertEqual(struct.unpack('<4f',C.string_at(h.actor+0x30,16)),(0.,0.,1.,0.))
    def test_magic_shortcut_chord_and_active_shortcut_menu_never_dash_or_spend_budget(self):
        for held,pressed,root in [(0x940010,0x900010,0),(0x900010,0x940010,0),(0x900010,0x900010,0x528a18)]:
            h=Host();h.prepare_slide();w64(h.game+0x2d539f0,h.game+root if root else 0)
            h.control(down=held,pressed=pressed,tilt=1,x=1)
            self.assertEqual(bridge.bridge_queue_calls(),0);self.assertFalse(r32(h.symbols['slide_air_used']))
            self.assertEqual(bridge.bridge_control_word(0),held);self.assertEqual(bridge.bridge_control_word(1),pressed)
            w64(h.game+0x2d539f0,0);h.control(down=0x900010,pressed=0x900010,tilt=1,x=1)
            self.assertEqual(bridge.bridge_queue_calls(),0) # Release required after a shortcut press.
            h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
    def test_cast_cancels_dash_before_facing_is_written_again(self):
        h=Host();h.prepare_slide();h.tap_slide();put(h.actor+0x30,struct.pack('<4f',0.,0.,-1.,3.14))
        h.control(state=0,request=0x36,height=100)
        self.assertEqual(struct.unpack('<3f',C.string_at(h.actor+0x30,12)),(0.,0.,-1.))
        self.assertEqual(h.move()[0],[1.,2.,3.,4.])
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
            self.assertEqual(bridge.bridge_queue_calls(),1);self.assertEqual(h.body(10),h.expected_variant(10));self.assertEqual(h.move()[0],[24.,0.,0.,24.])
    def test_slide_does_not_replace_queued_attack_or_spell_command(self):
        for queued in [0xcc,0x36,0x40000000]:
            h=Host(air=True);h.prepare_slide();w32(h.actor+0x178,1);w32(h.actor+0x17c,queued);h.tap_slide()
            self.assertEqual(bridge.bridge_queue_calls(),0);self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(r32(h.actor+0x17c),queued)
        h=Host(air=True);h.prepare_slide();w32(h.game+0x2d53a40,0x36);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),0)
    def test_slide_waits_for_native_queue_commit_before_movement(self):
        h=Host(air=True,control_mode=3);h.prepare_slide();h.tap_slide();self.assertEqual(h.move()[0],[1.,2.,3.,4.])
        bridge.bridge_commit(h.actor);h.clock(0.);self.assertEqual(h.move()[0],[24.,0.,0.,24.])
    def test_slide_pauses_at_zero_delta_and_aborts_invalid_delta(self):
        h=Host(air=True);h.prepare_slide();h.tap_slide();self.assertEqual(h.move(0.)[0],[0.,0.,0.,0.]);self.assertEqual(h.body(10),h.expected_variant(10))
        self.assertEqual(h.move()[0],[24.,0.,0.,24.])
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
    def test_f_copied_dash330_keeps_normal_grip_and_native_pointer_in_both_banks(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.prepare_slide();slot=10 if bank==98 else h.record_by_slot[10]['olympus_slot'];old=r32(h.array+slot*4);h.tap_slide()
            self.assertEqual(r32(h.array+slot*4),old)
            self.assertEqual(h.body(10),h.expected_variant(10));self.assertNotEqual(h.body(10),self.g_variant(h,'dash',10))
            self.assertEqual(bridge.call_ptr1(h.symbols['SingleFAirAction'],h.actor),1)
            self.assertEqual(bridge.call_ptr1(h.symbols['SingleGAction'],h.actor),0)
            h.finish_slide();h.control();self.assertEqual(r32(h.array+slot*4),old);self.assertEqual(h.body(10),h.expected(10,1))
            self.assertEqual(bridge.call_ptr1(h.symbols['SingleFAirAction'],h.actor),0)

    def test_once_per_airtime_survives_completion_release_damage_and_style_toggle(self):
     h=Host();h.prepare_slide();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.finish_slide();h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.control(state=3,request=0x48);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.equip(False);w32(h.actor+0x164,0);h.frame();h.equip(True);h.frame();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
     h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_landing_while_other_style_selected_restores_budget(self):
     h=Host();h.prepare_slide();h.tap_slide();h.finish_slide();h.control();h.equip(False);w32(h.actor+0x164,0);h.frame()
     h.control(state=0,request=0,height=0);h.observe();h.equip(True);h.frame();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_f_dash_does_not_read_or_modify_native_superglide_curves(self):
        h=Host();h.prepare_slide();motion=h.native_glide_motions[76];w32(motion,1)
        keys=motion+r32(motion+40);put(keys,b'\x55');native=C.string_at(motion,len(h.native_glide_originals[76]));h.tap_slide()
        self.assertEqual(bridge.bridge_queue_calls(),1);self.assertEqual(h.body(10),h.expected_variant(10))
        self.assertEqual(C.string_at(motion,len(native)),native)
        h.finish_slide();h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)

    def test_dash_needs_no_new_handle_or_animation_allocation(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.prepare_slide()
            # Reproduce unavailable pointer registration and deny allocations
            # after adapter setup. The existing native record still works.
            put(h.game+0x38ad90,bytes.fromhex('31c0c3'))
            bridge.bridge_magic_modes(1,1,0)
            banks=C.string_at(h.game+0x2ee3980,64*8);h.tap_slide()
            self.assertEqual(bridge.bridge_queue_calls(),1)
            self.assertEqual(C.string_at(h.game+0x2ee3980,64*8),banks)
            total=0.
            while r32(h.symbols['slide_active']):total+=h.move()[0][0]
            self.assertEqual(total,702.)

    def test_dash_survives_full_pointer_bank_table_in_both_banks(self):
        data=Path(os.environ['KH1_EXE']).read_bytes();pe=struct.unpack_from('<I',data,60)[0];sh=pe+24+struct.unpack_from('<H',data,pe+20)[0]
        for i in range(struct.unpack_from('<H',data,pe+6)[0]):
            vs,va,rs,rp=struct.unpack_from('<4I',data,sh+i*40+8)
            if va<=0x38aee0 and 0x38af36<=va+rs:
                encoder=data[rp+0x38aee0-va:rp+0x38af36-va];break
        else:raise AssertionError('Native pointer encoder unavailable')
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.prepare_slide()
            # Execute the original encoder's leaf body. Its two RIP-relative
            # references still resolve to the host's bank table at the same RVA.
            put(h.game+0x38aee0,encoder)
            put(h.game+0x38ad90,bytes.fromhex('4889ca48b8')+struct.pack('<Q',h.game+0x38aee0)+bytes.fromhex('ffe0'))
            for i in range(64):
                at=h.game+0x2ee3980+i*8
                if not r64(at):w64(at,0x600000000000+i*0x2000000)
            before=C.string_at(h.game+0x2ee3980,64*8)
            missing=0x5fffabcdef10;encoded=bridge.call_ptr2(h.game+0x38aee0,0,missing)
            self.assertNotEqual(h.decode(encoded),missing)
            for count in range(1,4):
                h.control(state=0,request=0,height=-.05);h.tap_slide()
                self.assertEqual(bridge.bridge_queue_calls(),count)
                h.finish_slide();h.control()
            self.assertEqual(C.string_at(h.game+0x2ee3980,64*8),before)
    def test_ui_installer_checks_actual_executable_anchors_and_expands_all_tables(self):
     h=Host();anchors=h.ui_seed();self.assertTrue(h.ui_init());self.assertTrue(bridge.call_int0(h.symbols['StylesMenuReady']))
     h.ui_call('styles_root_init');storage=r64(h.symbols['styles_storage']);count=r32(h.game+0x2e1f4c8);self.assertEqual(count,8)
     self.assertEqual(list((C.c_uint*8).from_address(storage)),[0,8,1,3,4,5,6,7])
     self.assertEqual(r32(storage+0x40+8*4),0xff00);self.assertEqual(r64(storage+0x80+8*8),r64(storage+0x80+2*8));self.assertEqual(r64(storage+0xd0+8*8),h.symbols['styles_enter'])
    def test_ui_last_anchor_or_protection_failure_publishes_nothing(self):
     for kind in ['anchor','slots_helper','ap_column','ap_create','protect']:
      h=Host();anchors=h.ui_seed()
      if kind=='anchor':put(h.game+anchors[-1][0],b'\xcc')
      elif kind=='slots_helper':put(h.game+0x2ebcd0,b'\xcc')
      elif kind=='ap_column':put(h.game+0x311f9e,b'\xcc')
      elif kind=='ap_create':put(h.game+0x310d26,b'\xcc')
      else:bridge.bridge_magic_modes(0,0,2)
      sites=[(r,n) for r,n in anchors]+[(0x2dae20,15),(0x311c56,16),(0x2d0970,21),(0x52af20,8),(0x311f9e,15),(0x310d26,5),(0x31127c,5)]
      before=[C.string_at(h.game+r,n) for r,n in sites];self.assertFalse(h.ui_init());self.assertEqual(before,[C.string_at(h.game+r,n) for r,n in sites])
    def test_ui_normal_abilities_filters_only_styles_and_native_row_write_commits_correct_id(self):
     h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97,6,21])+bytes(43));w=h.ui_window();h.ui_call('abilities_enter',w)
     # Execute the real native prologue and our R12 bridge; toggle visible row1.
     tail=bytes.fromhex('418074244180')+h.ui_tail;put(h.game+0x311c66,tail);h.ui_call('styles_list',w)
     self.assertEqual(h.abilities()[:6],bytes([6,0x17,6,21,117,0]));self.assertEqual(r32(h.game+0x2e9cbc8),4)
    def test_ui_styles_has_all_twelve_and_selects_single_f_exclusively(self):
     h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97,21])+bytes(44));w=h.ui_window();h.ui_call('styles_enter',w)
     # Display order is Singles A-F, Duals A-D, Anti; Single F is row5.
     w32(h.symbols['styles_customize_active'],0);put(h.game+0x311c66,bytes.fromhex('418074244580')+h.ui_tail);h.ui_call('styles_list',w)
     self.assertEqual(h.abilities()[:5],bytes([6,0x97,21,116,0]));self.assertEqual(r32(h.game+0x2e9cbc8),12)
     p=h.symbols['styles_shadow']+0x44;self.assertEqual(C.string_at(p,12),bytes([252,251,248,247,245,116,243,254,253,249,246,250]))
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
        ptr=bridge.call_ptr1(h.game+0x2d0970,0xff00);self.assertEqual(C.string_at(ptr,10),bytes([0x2d,0x59,0x57,0x58,0x53,0x51,0x4d,0x5e,0x49,0]))
        ptr2=bridge.call_ptr1(h.game+0x2d0970,0x6b);self.assertEqual(ptr,ptr2)
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
        self.assertEqual(r32(h.game+0x2e1f4cc),6);self.assertEqual(C.c_ushort.from_address(w+0xfe).value,6<<4);self.assertEqual(C.c_ushort.from_address(w+0xf8).value,8)
    def test_external_native_ability_change_cannot_be_overwritten_by_stale_view(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6,117,0x97])+bytes(45));w=h.ui_window();h.ui_call('styles_enter',w);w=r64(h.symbols['styles_custom_page'])
        put(h.symbols['styles_shadow']+0x44+5,bytes([116]));new=bytes([6,117,0x97,42])+bytes(44);put(h.save+0x44,new)
        h.ui_call('styles_page',w);self.assertEqual(h.abilities(),new)

    def test_model_unload_retires_dash_and_main_readmits_without_resetting_air_budget(self):
        h=Host();h.prepare_slide();slot=10;original=r32(h.array+slot*4);h.tap_slide();w32(h.actor+0x374,0);h.frame()
        self.assertEqual(r32(h.array+slot*4),original);w32(h.actor+0x374,1);h.frame();h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)
        h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)
    def test_returning_resource_array_restores_its_known_f_body_variant(self):
        h=Host();h.prepare_slide();array=h.array;handle=r32(h.actor+0x1d4);original=r32(array+40);h.tap_slide()
        h.activate_bank(False,True);w32(h.actor+0x164,0);h.frame();self.assertEqual(r32(array+40),original)
        w32(h.actor+0x1d4,handle);h.observe();h.frame();self.assertEqual(r32(array+40),original);self.assertEqual(h.body(10),h.expected(10,1))
        h.control(state=0,request=0,height=0);h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),2)

    def test_reported_square_marker_bits_are_accepted_and_preserved(self):
        h=Host();h.prepare_slide();h.control(down=0x00900010,pressed=0x00900010,tilt=1,x=1)
        self.assertEqual(bridge.bridge_queue_calls(),1);self.assertEqual(bridge.bridge_control_word(0)&0x00900000,0x00900000)
        self.assertEqual(r32(h.game+0x298ca94),0x00900010)
    def test_full_native_list_rejects_style_selection_without_losing_abilities(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());data=bytes([6]*47+[0]);put(h.save+0x44,data);w=h.ui_window();h.ui_call('styles_enter',w)
        w32(h.symbols['styles_customize_active'],0);put(h.game+0x311c66,bytes.fromhex('418074244580')+h.ui_tail);h.ui_call('styles_list',w);self.assertEqual(h.abilities(),data)
        self.assertEqual(C.c_ubyte.from_address(h.symbols['styles_shadow']+0x44+5).value,244)

    def test_repeated_landings_rearm_f_and_restore330_without_pointer_changes(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.prepare_slide();slot=10 if bank==98 else h.record_by_slot[10]['olympus_slot'];original=r32(h.array+slot*4)
            for count in range(1,9):
                h.control(state=0,request=0,height=-.05);h.control(state=2,request=6);h.control(down=0x900010,pressed=0x900010,x=1,tilt=1)
                self.assertEqual(bridge.bridge_queue_calls(),count);self.assertEqual(h.body(10),h.expected_variant(10));self.assertEqual(r32(h.array+slot*4),original)
                h.finish_slide();h.control();self.assertEqual(h.body(10),h.expected(10,1));self.assertEqual(r32(h.array+slot*4),original)
                h.control();h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),count)

    def test_f_dash_refuses_foreign_fall_body_without_overwriting_it(self):
        h=Host();h.prepare_slide();motion=h.motions[10];key=motion+r32(motion+40);value=C.string_at(key,1);put(key,bytes([value[0]^1]));before=h.body(10)
        h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),0);self.assertEqual(h.body(10),before)

    def test_dash_ignores_unrelated_native_superglide_cache_fields(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True);h.prepare_slide();h.tap_slide();h.finish_slide()
            source=h.native_glide_motions[76];scratch=h.buffer(bytes(256))
            w32(source+64,3);w32(source+68,bridge.bridge_encode(scratch));w32(source+72,7)
            native=C.string_at(source,len(h.native_glide_originals[76]))
            for count in range(2,6):
                h.control(state=0,request=0,height=-.05);h.tap_slide()
                self.assertEqual(bridge.bridge_queue_calls(),count);total=0.
                while r32(h.symbols['slide_active']):total+=h.move()[0][0]
                self.assertEqual(total,702.);self.assertEqual(C.string_at(source,len(native)),native)

    def test_inherited_and_looping_animation_clock_cannot_shorten_dash_distance(self):
        for bank in [98,60]:
            h=Host(slot=bank,encoded_fields=True,control_mode=3);h.prepare_slide();h.tap_slide()
            # A committed native Fall can retain a clock from before the tap.
            w32(h.actor+0x178,0);w32(h.actor+0x164,6);h.clock(120);h.control()
            total=0.
            for tick in range(30):
                h.clock(float((120+tick)%60));h.control();total+=h.move()[0][0]
            self.assertEqual(total,702.);self.assertFalse(r32(h.symbols['slide_active']))
            h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),1)

    def test_changed_fall_header_or_pointer_is_refused_before_f_dash(self):
        for field in [16,24,32,44,52,40]:
            h=Host();h.prepare_slide();source=h.motions[10];w32(source+field,r32(source+field)+4);before=h.body(10)
            h.tap_slide();self.assertEqual(bridge.bridge_queue_calls(),0);self.assertEqual(h.body(10),before)

    def test_customize_is_below_items_with_native_cursor_ids_preserved(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w32(h.game+0x2e1f4d0,3);h.ui_call('styles_root_init')
        storage=r64(h.symbols['styles_storage'])
        self.assertEqual(list((C.c_uint*8).from_address(storage)),[0,8,1,3,4,5,6,7])
        self.assertEqual(r32(h.game+0x2e1f4cc),3)

    def test_styles_keeps_native_blue_without_palette_overrides(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());root=h.ui_window();page=h.ui_window();child=h.ui_window()
        w64(root+0x20,page);w64(page+0x18,root);w64(page+0x20,child);w64(child+0x18,page)
        before=C.string_at(h.game+0x53bd10,96)
        h.ui_call('styles_enter',root);page=r64(h.symbols['styles_custom_page']);h.ui_page_frame(page)
        for w in [root,page,child]:self.assertEqual(r64(w+0x90),0)
        self.assertEqual(C.string_at(h.game+0x53bd10,96),before)
        self.assertEqual(bridge.bridge_menu_panel_count(),12)

    def test_customize_categories_stance_toggle_and_reserved_categories_preserve_save(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());native=bytes([6,0x97,6,21]);put(h.save+0x44,native+bytes([117])+bytes(43))
        root=h.ui_window();w=h.ui_window();h.ui_call('styles_enter',root);w=r64(h.symbols['styles_custom_page'])
        text=h.ui_page_frame(w,0x20);self.assertTrue(text.startswith('Stance|Passives|Limits|Outfits|'))
        self.assertFalse(r32(h.symbols['styles_picker'])) # Entry press cannot enter the list too.
        self.assertIn('Type A|Single|I',text);self.assertIn('Type H?|Dual|I',text);self.assertNotIn('Type I?',text)
        for row in [2,3]:
            C.c_ushort.from_address(w+0xfe).value=(row-1)*16
            old=C.string_at(h.save,0x1000);text=h.ui_page_frame(w,0x4000)
            self.assertNotIn('Type A',text);self.assertIn('No entries available yet',text)
            h.ui_page_frame(w,0x20);self.assertEqual(bridge.bridge_menu_sound(),4)
            self.assertEqual(C.string_at(h.save,0x1000),old);self.assertFalse(r32(h.symbols['styles_picker']))
        h.ui_page_frame(w,0x4000);h.ui_page_frame(w,0x20)
        self.assertTrue(r32(h.symbols['styles_picker']));self.assertEqual(C.c_ushort.from_address(w+0xfa).value,8)
        h.ui_choose(w,5);self.assertEqual(h.abilities(),native+bytes([116])+bytes(43))
        # Abilities-style confirmation on the equipped row unequips it.
        h.ui_choose(w,5);self.assertEqual(h.abilities(),native+bytes([244])+bytes(43))
        h.ui_choose(w,5);self.assertEqual(h.abilities(),native+bytes([116])+bytes(43))
        changed=C.string_at(h.save,0x1000)
        self.assertEqual(changed[:0x44],old[:0x44]);self.assertEqual(changed[0x74:],old[0x74:])

    def test_customize_stance_scroll_reaches_all_twelve_and_keeps_metadata_aligned(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w=h.ui_window();h.ui_call('styles_enter',w);w=r64(h.symbols['styles_custom_page']);h.ui_page_frame(w);h.ui_page_frame(w,0x20)
        names=set()
        for i in range(12):
            text=h.ui_page_frame(w,0 if i==0 else 0x4000)
            for name in ['Type A','Type B','Type C','Type D','Type E','Type F','Type G','Type H?','Type I?','Type K?','Type L?','Type M?']:
                if name in text:names.add(name)
            rects=[[bridge.bridge_menu_rect_word(j,k) for k in range(4)] for j in range(bridge.bridge_menu_rect_count())]
            self.assertEqual(len(rects),16)
            for j in range(8):
                self.assertEqual(rects[j*2],[327,73+j*28,42,22]);self.assertEqual(rects[j*2+1],[373,73+j*28,42,22])
            self.assertEqual(bridge.bridge_menu_scroll_count(),1)
        self.assertEqual(len(names),12);self.assertIn('Type M?|None|0',text)
        h.ui_page_frame(w,0x20);self.assertEqual(h.abilities()[2],122)
        top=C.c_ushort.from_address(w+0xfc).value;self.assertEqual(top,4*16)
        h.ui_page_frame(w,0x40);h.ui_page_frame(w,0x20)
        self.assertEqual(C.c_ushort.from_address(w+0xfc).value,top)
        self.assertEqual(bridge.call_ptr1(h.game+0x2ef440,w),11)

    def test_customize_cancel_list_then_close_native_menu_chain(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());root=h.ui_window();page=h.ui_window();other=h.ui_window()
        w64(root+0x20,page);w64(page+0x18,root);w64(h.game+0x2e9cb70,root);h.ui_call('styles_enter',root);page=r64(h.symbols['styles_custom_page']);h.ui_page_frame(page)
        old=h.abilities();h.ui_page_frame(page,0x20);h.ui_page_frame(page,0x40)
        self.assertFalse(r32(h.symbols['styles_picker']));self.assertEqual(h.abilities(),old);self.assertFalse(r32(page+0x68)&1)
        h.ui_page_frame(page,0x40)
        self.assertTrue(r32(root+0x68)&1);self.assertTrue(r32(page+0x68)&1);self.assertFalse(r32(other+0x68)&1)

    def test_customize_confirmation_uses_native_swapped_button_setting(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w=h.ui_window();h.ui_call('styles_enter',w);w=r64(h.symbols['styles_custom_page']);h.ui_page_frame(w)
        w32(h.game+0x5456a0,0x40);w32(h.game+0x5456a4,0x20);h.ui_page_frame(w,0x40)
        self.assertTrue(r32(h.symbols['styles_picker']))

    def test_shortcuts_rename_is_visual_and_original_callback_stays_native(self):
        h=Host();h.ui_seed();native_callback=r64(h.game+0x52ada0+24);self.assertTrue(h.ui_init())
        storage=r64(h.symbols['styles_storage']);self.assertEqual(r64(storage+0xd0+24),native_callback)
        self.assertEqual(r32(storage+0x40+12),0xff02)
        expected=bytes([0x3d,0x4c,0x53,0x56,0x58,0x47,0x59,0x58,0x57,0])
        self.assertEqual(C.string_at(bridge.call_ptr1(h.game+0x2d0970,0xff02),10),expected)
        w32(h.game+0x2e1f4d0,3);self.assertEqual(C.string_at(bridge.call_ptr1(h.game+0x2d0970,0x6c),10),expected)
        offsets=h.buffer(bytes(0x100));text=h.buffer(b'Native text\0');w64(h.game+0x2e1ac50,offsets);w64(h.game+0x2e1ac48,text)
        w32(h.game+0x2e1f4d0,2);self.assertEqual(bridge.call_ptr1(h.game+0x2d0970,0x6c),text)

    def test_full_native_save_rejects_new_stance_without_ap_or_equipment_changes(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6]*47+[0]))
        before=C.string_at(h.save,0x1000);w=h.ui_window();h.ui_call('styles_enter',w);w=r64(h.symbols['styles_custom_page']);h.ui_page_frame(w);h.ui_page_frame(w,0x20);h.ui_choose(w,5)
        self.assertEqual(C.string_at(h.save,0x1000),before);self.assertEqual(bridge.bridge_menu_sound(),4)

    def test_original_native_page_scroll_reaches_last_stances_and_wraps(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w=h.ui_window();h.ui_call('styles_enter',w);w=r64(h.symbols['styles_custom_page']);h.ui_page_frame(w);h.ui_page_frame(w,0x20)
        # Execute the same original navigation code as native Abilities. Only
        # its mouse, sound and cursor-animation tails are host substitutes.
        put(h.game+0x2ef670,h.ui_raw(0x2ef670,0x870))
        for r in [0x2eb370,0x2f1100]:put(h.game+r,b'\xc3')
        put(h.game+0x2eb130,bytes.fromhex('31c0c3'))
        w32(h.ui_pad+16,0x800);text=h.ui_page_frame(w,0x800)
        self.assertEqual(C.c_ushort.from_address(w+0xfc).value,64)
        self.assertIn('Type M?|None|0',text);self.assertNotIn('Type A|',text)
        text=h.ui_page_frame(w,0x800)
        self.assertEqual(C.c_ushort.from_address(w+0xfc).value,0);self.assertIn('Type A|Single|I',text)
        w32(h.ui_pad+16,0)

    def test_passives_opens_sora_directly_and_returns_without_a_member_selector(self):
        h=Host();root,page=h.passive_setup([6,0x97,117]);w32(h.game+0x2e1f4d0,8)
        self.assertEqual(r32(h.symbols['styles_picker']),2);self.assertEqual(r64(page+0x20),0)
        self.assertEqual(r64(h.game+0x2e9cb70),root);self.assertEqual(r32(h.symbols['styles_view']),0)
        self.assertEqual(C.c_ushort.from_address(page+0xf8).value,52)
        title=bridge.call_ptr1(h.game+0x2d0970,0x6b)
        self.assertEqual(C.string_at(title,9),bytes([0x3a,0x45,0x57,0x57,0x4d,0x5a,0x49,0x57,0]))
        h.ui_choose(page,0);self.assertEqual(h.abilities()[:4],bytes([0x86,0x97,117,0]))
        text=h.ui_page_frame(page,0x40);self.assertFalse(r32(h.symbols['styles_picker']));self.assertEqual(r64(page+0x20),0)
        self.assertFalse(r32(root+0x68)&1);self.assertFalse(r32(page+0x68)&1)
        self.assertIn('Stance|Passives|Limits|Outfits',text);h.ui_page_frame(page,0x20)
        self.assertEqual(r32(h.symbols['styles_picker']),2);self.assertEqual(h.abilities()[:4],bytes([0x86,0x97,117,0]))

    def test_removed_root_abilities_selection_redirects_to_customize(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w32(h.game+0x2e1f4d0,2);h.ui_call('styles_root_init')
        storage=r64(h.symbols['styles_storage']);entries=list((C.c_uint*8).from_address(storage))
        self.assertNotIn(2,entries);self.assertEqual(entries[:4],[0,8,1,3])
        self.assertEqual(r32(h.game+0x2e1f4d0),8);self.assertEqual(r32(h.game+0x2e1f4cc),1)

    def test_full_native_passives_can_toggle_without_allocating_a_style_token(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([6]*47+[0]));w=h.ui_window();h.ui_call('abilities_enter',w)
        put(h.game+0x311c66,bytes.fromhex('418074244080')+h.ui_tail);h.ui_call('styles_list',w)
        self.assertEqual(h.abilities(),bytes([0x86]+[6]*46+[0]))

    def test_passives_native_dialog_enforces_ap_rejection_and_equips_or_removes(self):
        # Execute vanilla's complete equip/remove decision callback. Its AP
        # availability result is an input; rendering/animation are substituted.
        for initial,blocked,expected,sound in [(0x86,1,0x86,4),(0x86,0,6,5),(6,1,0x86,0x4b)]:
            h=Host();h.ui_seed();self.assertTrue(h.ui_init());put(h.save+0x44,bytes([initial,117])+bytes(46))
            root=h.ui_window();h.ui_call('styles_enter',root);parent=r64(h.symbols['styles_custom_page']);h.ui_page_frame(parent)
            h.ui_page_frame(parent,0x4000);h.ui_page_frame(parent,0x20)
            put(h.game+0x310650,h.ui_raw(0x310650,0x28b))
            for r in [0x2e6350,0x2d6aa0,0x34b4f0]:put(h.game+r,b'\xc3')
            put(h.game+0x2e5510,bytes.fromhex('488b4118c3'))
            put(h.game+0x2d1160,bytes.fromhex('31c0c3'))
            definition=bytearray(h.ui_raw(0x549000,48));struct.pack_into('<Q',definition,0,h.game+0x310310);struct.pack_into('<Q',definition,8,0);put(h.game+0x549000,definition)
            popup=h.ui_window();back=h.ui_window();w64(popup+0x18,back);w32(popup+0x104,1)
            C.c_ushort.from_address(popup+0xf8).value=3;C.c_ushort.from_address(popup+0xfa).value=3
            w32(h.game+0x2e9cb7c,0);w32(h.game+0x2e9cb84,0);w32(h.game+0x2e9cb90,initial);w32(h.game+0x2e9cb94,blocked)
            w64(h.game+0x2e9cb88,h.symbols['styles_shadow']+4);w64(h.game+0x2e941c0,popup);w32(h.ui_pad+8,0x20)
            bridge.bridge_menu_reset();bridge.call_void1(h.game+0x310650,popup);h.ui_call('styles_commit')
            self.assertEqual(h.abilities()[:3],bytes([expected,117,0]));self.assertEqual(bridge.bridge_menu_sound(),sound)
            self.assertEqual(bool(r64(back+0x20)),bool(blocked and initial&0x80))

    def test_native_ap_renderer_geometry_has_one_aligned_panel_and_no_frame_layer(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());root=h.ui_window();h.ui_call('styles_enter',root);page=r64(h.symbols['styles_custom_page'])
        # Execute the original AP panel renderer to its finished draw packets.
        # GPU allocation/submission and color fading are substitutes, not shape math.
        put(h.game+0x2f2430,h.ui_raw(0x2f2430,0x260))
        for r in [0x30c2d0,0x316e60,0x28dd40]:put(h.game+r,b'\xc3')
        put(h.game+0x2e9110,bytes.fromhex('89c8c3'))
        put(h.game+0x28dcf0,b'\x48\xb8'+struct.pack('<Q',bridge.bridge_symbol(b'NativeGpuAlloc'))+b'\xff\xe0')
        bridge.bridge_gpu_reset();h.ui_page_frame(page)
        # Eight visible rows plus the ninth row outside the native scissor,
        # needed when the list animates between scroll positions.
        self.assertEqual(bridge.bridge_gpu_count(),18);packets=[]
        for i in range(18):
            p=bridge.bridge_gpu_packet(i);packets.append(C.string_at(p,0xd0))
            x,y,right,bottom=[r32(p+j) for j in [0xa0,0xa4,0xc0,0xc4]]
            expected_x=327 if i%2==0 else 373;expected_y=73+(i//2)*28
            self.assertEqual((x-0x7000,y-0x7400,right-x,bottom-y),(expected_x*16,expected_y*16,42*16,22*16))
        # Same first packet as a direct vanilla AP-box call, including UV/layout.
        full=h.buffer(C.string_at(page,0x118));w32(full+0xdc,0x7000);w32(full+0xe0,0x7400)
        bridge.bridge_gpu_reset();bridge.call_panel(h.game+0x2f2430,full,327,73,r32(h.game+0x52a8d0+40))
        self.assertEqual(C.string_at(bridge.bridge_gpu_packet(0),0xd0),packets[0])
        self.assertEqual(bridge.bridge_menu_panel_count(),12)

    def test_styles_hides_native_ap_column_but_normal_abilities_runs_original_path(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w=h.ui_window()
        # Execute the real ability prologue, record bridge, and AP-column bridge.
        save_rbx=bytes.fromhex('48899c2490000000');load_rbx=bytes.fromhex('488b9c2490000000')
        put(h.game+0x311c66,save_rbx+bytes.fromhex('bb0200000048b8')+struct.pack('<Q',h.game+0x311f9e)+bytes.fromhex('ffe0'))
        put(h.game+0x311fad,bytes.fromhex('4889c8')+load_rbx+h.ui_tail[3:])
        put(h.game+0x31206b,bytes.fromhex('4889d8')+load_rbx+h.ui_tail[3:])
        h.ui_call('abilities_enter',w);self.assertEqual(bridge.call_ptr1(h.game+0x311c20,w),h.game+40)
        h.ui_call('styles_enter',w);self.assertEqual(bridge.call_ptr1(h.game+0x311c20,w),1)
    def test_native_ap_box_is_not_created_only_in_styles(self):
        h=Host();h.ui_seed();self.assertTrue(h.ui_init());w=h.ui_window()
        put(h.game+0x2e5a40,bytes.fromhex('b855000000c3'))
        for site in [0x310d26,0x31127c]:
            shim=h.buffer(bytes.fromhex('4883ec2848b8')+struct.pack('<Q',h.game+site)+bytes.fromhex('ffe0'))
            put(h.game+site+5,bytes.fromhex('4883c428c3'))
            w32(h.symbols['styles_view'],0);self.assertEqual(bridge.call_ptr2(shim,h.game+0x548f40,6),0x55)
            w32(h.symbols['styles_view'],1);self.assertEqual(bridge.call_ptr2(shim,h.game+0x548f40,6),0)
            self.assertEqual(bridge.call_ptr2(shim,h.game+0x549090,6),0x55)

if __name__=='__main__':
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(RuntimeTests))
 report={'passed':result.wasSuccessful(),'tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),'executed_final_integrated_pe_c_adapter':True,'native_ability_record_prologue_executed':True,'native_menu_references_checked_against_supplied_executable':True,'rendering_and_rust_dispatch_mocked':True,'windows_or_game_executed':False}
 Path(os.environ.get('VALIDATION_OUT',str(TEST_ROOT/'runtime_validation.json'))).write_text(json.dumps(report,indent=2)+'\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)
