/* Linux-only test host: executes the actual PE DLL with Win64 ABI mocks. */
#define _GNU_SOURCE
#include <stdint.h>
#include <stddef.h>
#include <string.h>
#include <sys/mman.h>
#include <math.h>
#define ABI __attribute__((ms_abi))
typedef struct {uintptr_t base,allocation;uint32_t allocation_protect;uint16_t partition,pad;size_t size;uint32_t state,protect,type,pad2;} MemInfo;
static struct {uintptr_t start;size_t size;uint32_t protect;} ranges[128];
static unsigned nranges,queries,protect_calls;
static uintptr_t game_base;
static int remove_mode,conflict,test_page=1,profile_override;
static int glide_eligible=1;
static int hand_magic=1,air_enabled=1,alloc_failure,protect_failure;
static unsigned control_calls,control_words[4],control_mode,queue_calls,native_glide_calls;
static unsigned matrix_code,point_code;static float point_fraction;
static char output[131072];static size_t used;
static uint64_t numbered_saved;static unsigned numbered_save_calls;
void bridge_reset(uintptr_t game){game_base=game;nranges=queries=protect_calls=0;remove_mode=conflict=0;hand_magic=air_enabled=1;control_calls=control_mode=queue_calls=native_glide_calls=0;glide_eligible=1;memset(control_words,0,sizeof(control_words));alloc_failure=protect_failure=0;matrix_code=point_code=0;used=0;output[0]=0;numbered_saved=0;numbered_save_calls=0;}
static void ABI numbered_save(uint64_t bits){numbered_saved=bits;numbered_save_calls++;}
uint64_t bridge_numbered_saved(void){return numbered_saved;}
unsigned bridge_numbered_save_calls(void){return numbered_save_calls;}
void bridge_magic_modes(int enabled,int noalloc,int noprotect){hand_magic=enabled;alloc_failure=noalloc;protect_failure=noprotect;}
void bridge_range(uintptr_t start,size_t size,uint32_t protect){ranges[nranges].start=start;ranges[nranges].size=size;ranges[nranges].protect=protect;nranges++;}
void bridge_modes(int remove,int other){remove_mode=remove;conflict=other;}
void bridge_test_options(int page,int override){test_page=page;profile_override=override;}
uint32_t bridge_ability_count(uintptr_t fn,uint32_t id,uint32_t member){typedef uint32_t (ABI *F)(uint32_t,uint32_t);return ((F)fn)(id,member);}
const char* bridge_log(void){return output;}
unsigned bridge_queries(void){return queries;}
static uintptr_t ABI get_module(const char*name){if(!name)return game_base;return (conflict==1&&strcmp(name,"kh1-dual-wield.dll")==0)||(conflict==2&&strcmp(name,"kh1-aqua.dll")==0)||(conflict==3&&strcmp(name,"kh1-kh2.dll")==0)?1:0;}
static uint32_t ABI file_name(uintptr_t module,uint16_t*out,uint32_t count){(void)module;const char*s="C:\\mock\\KINGDOM HEARTS FINAL MIX.exe";uint32_t i=0;for(;s[i]&&i+1<count;i++)out[i]=(unsigned char)s[i];out[i]=0;return i;}
static size_t ABI query(const void*p,MemInfo*out,size_t size){queries++;uintptr_t a=(uintptr_t)p;if(size!=sizeof(*out))return 0;for(unsigned i=0;i<nranges;i++)if(a>=ranges[i].start&&a<ranges[i].start+ranges[i].size){memset(out,0,sizeof(*out));out->base=out->allocation=ranges[i].start;out->size=ranges[i].size;out->state=0x1000;out->protect=ranges[i].protect;return sizeof(*out);}return 0;}
static uintptr_t ABI create_file(const uint16_t*path,uint32_t a,uint32_t b,void*c,uint32_t d,uint32_t e,uintptr_t f){(void)path;(void)a;(void)b;(void)c;(void)d;(void)e;(void)f;return 7;}
static int ABI write_file(uintptr_t f,const void*data,uint32_t n,uint32_t*done,void*overlap){(void)f;(void)overlap;if(used+n>=sizeof(output))return 0;memcpy(output+used,data,n);used+=n;output[used]=0;if(done)*done=n;return 1;}
static int ABI close_file(uintptr_t f){(void)f;return 1;}
static uint32_t ABI profile(const uint16_t*a,const uint16_t*b,int c,const uint16_t*d){(void)a;(void)c;(void)d;return b[0]=='t'?(uint32_t)test_page:b[0]=='p'?(uint32_t)profile_override:b[0]=='h'?(uint32_t)hand_magic:b[0]=='a'?(uint32_t)air_enabled:(uint32_t)remove_mode;}
static void* ABI valloc(void*p,size_t n,uint32_t kind,uint32_t protect){(void)p;(void)kind;(void)protect;if(alloc_failure)return 0;void*q=mmap(0,n,PROT_READ|PROT_WRITE|PROT_EXEC,MAP_PRIVATE|MAP_ANONYMOUS,-1,0);if(q==MAP_FAILED)return 0;bridge_range((uintptr_t)q,n,0x40);return q;}
static int ABI vfree(void*p,size_t n,uint32_t kind){(void)n;(void)kind;return munmap(p,4096)==0;}
static int ABI vprotect(void*p,size_t n,uint32_t protect,uint32_t*old){(void)p;(void)n;(void)protect;protect_calls++;if(protect_failure==1||(protect_failure>1&&protect_calls==(unsigned)protect_failure))return 0;*old=0x20;return 1;}
static int ABI flush(uintptr_t process,const void*p,size_t n){(void)process;(void)p;(void)n;return 1;}
static void ABI native_matrix(uintptr_t actor,uint32_t code,float*out){(void)actor;matrix_code=code;memset(out,0,16*sizeof(float));out[0]=out[5]=out[10]=out[15]=1;out[12]=code==0x20ce?-11:code==0x2065?11:100;out[13]=(code==0x20ce||code==0x2065)?22:200;out[14]=(code==0x20ce||code==0x2065)?33:300;}
static void ABI native_point(uintptr_t actor,uint32_t code,float fraction,float*out){(void)actor;point_code=code;point_fraction=fraction;out[0]=100;out[1]=200;out[2]=300;out[3]=1;}
void bridge_matrix(uintptr_t f,uintptr_t actor,uint32_t code,float*out){((void(ABI*)(uintptr_t,uint32_t,float*))f)(actor,code,out);}
void bridge_point(uintptr_t f,uintptr_t actor,uint32_t code,float fraction,float*out){((void(ABI*)(uintptr_t,uint32_t,float,float*))f)(actor,code,fraction,out);}
unsigned bridge_matrix_code(void){return matrix_code;}
unsigned bridge_point_code(void){return point_code;}
float bridge_point_fraction(void){return point_fraction;}
static uint32_t ABI handle(const void*p){uintptr_t addr=(uintptr_t)p,aligned=addr&~(uintptr_t)0x1ffffff;uintptr_t*t=(uintptr_t*)(game_base+0x2ee3980);for(unsigned i=1;i<64;i++)if(t[i]==aligned)return 0x80000000u|(i<<25)|(uint32_t)(addr-aligned);for(unsigned i=1;i<64;i++)if(!t[i]){t[i]=aligned;return 0x80000000u|(i<<25)|(uint32_t)(addr-aligned);}return 0;}
uint32_t bridge_encode(uintptr_t p){return handle((void*)p);}
void bridge_air_modes(int enabled,unsigned mode){air_enabled=enabled;control_mode=mode;}
void bridge_control(uintptr_t f,uintptr_t actor,uintptr_t dir){
    ((void(ABI*)(uintptr_t,uintptr_t))f)(actor,dir);
    if(control_mode==5&&(*(uint32_t*)(game_base+0x2d5ec10)&0x80u))((void(ABI*)(uintptr_t))(game_base+0x2b26c0))(actor);
    if(control_mode==6&&(*(uint32_t*)(game_base+0x2d5ec10)&0x100u))((void(ABI*)(uintptr_t))(game_base+0x2b2750))(actor);
}
void bridge_glide_eligible(int enabled){glide_eligible=enabled;}
unsigned bridge_native_glide_calls(void){return native_glide_calls;}
void bridge_glide(uintptr_t f,uintptr_t actor){((void(ABI*)(uintptr_t))f)(actor);}
uintptr_t bridge_event(uintptr_t f,uintptr_t motion,uint32_t track,float frame){return ((uintptr_t(ABI*)(uintptr_t,uint32_t,float))f)(motion,track,frame);}
static uintptr_t ABI native_decode(uint32_t h){
    if(!(h&0x80000000u))return h;
    return *(uintptr_t*)(game_base+0x2ee3980+((h&0x7fffffffu)>>25)*8)+(h&0x1ffffffu);
}
static int ABI native_glide_common(uintptr_t actor){
    native_glide_calls++;if(!glide_eligible)return 0;*(uint32_t*)(actor+0x70)=21;*(uint32_t*)(actor+0x164)=0x71;*(uint32_t*)(actor+0x178)=0;return 1;
}
static uintptr_t ABI native_append(uintptr_t actor,uint32_t request,float frame){
    uint32_t count=*(uint32_t*)(actor+0x178);uintptr_t p=actor+0x17c+count*16;
    memset((void*)p,0,16);*(uint32_t*)p=request;*(float*)(p+8)=frame;*(uint32_t*)(actor+0x178)=count+1;return p;
}
unsigned bridge_control_calls(void){return control_calls;}
unsigned bridge_control_word(unsigned i){return i<4?control_words[i]:0;}
unsigned bridge_queue_calls(void){return queue_calls;}
void bridge_commit(uintptr_t actor){
    uint32_t count=*(uint32_t*)(actor+0x178),request=*(uint32_t*)(actor+0x17c)&0xffff;
    if(count==1&&(request==6||(request>=0x71&&request<=0x74)||(request>=0x76&&request<=0x79))){
        *(uint32_t*)(actor+0x164)=request;*(float*)(actor+0x16c)=*(float*)(actor+0x184);*(uint32_t*)(actor+0x178)=0;
    }
}
static void ABI native_queue(uintptr_t actor,uint32_t request,float frame){
    queue_calls++;
    *(uint32_t*)(actor+0x178)=1;*(uint32_t*)(actor+0x17c)=request;*(float*)(actor+0x184)=frame;
}
static void ABI native_control(uintptr_t actor,uintptr_t dir){
    control_calls++;uint32_t*pad=(uint32_t*)(game_base+0x298ca90);
    unsigned fields[4]={1,2,4,5};for(unsigned i=0;i<4;i++)control_words[i]=pad[fields[i]];
    if(control_mode==1)pad[2]^=0x40000000u;
    if(control_mode!=3)bridge_commit(actor);
    if(control_mode==4&&(pad[1]&6u)&&(*(uint32_t*)(actor+0x70)==1||*(uint32_t*)(actor+0x70)==2)){
        *(uint32_t*)(actor+0x70)=21;*(uint32_t*)(actor+0x164)=0x71;*(uint32_t*)(actor+0x178)=0;
    }
    if(control_mode==2)*(uint32_t*)(actor+0x164)=0xcc;
    if(control_mode==7&&((const float*)dir)[3]>.15f){
        const float*v=(const float*)dir;float yaw=atan2f(v[0],v[2]);
        *(float*)(actor+0x30)=v[0];*(float*)(actor+0x34)=0;*(float*)(actor+0x38)=v[2];
        *(float*)(actor+0x3c)=yaw;*(float*)(actor+0x150)=yaw;
    }
    /* Native control0x2A630C clears its command record after dispatch. */
    *(uint64_t*)(game_base+0x2d53a40)=0;*(uint32_t*)(game_base+0x2d53a48)=0;
}
static unsigned move_calls;
static float last_motion_delta;static unsigned motion_calls,guard_row_calls,angle_calls;
static uintptr_t ABI native_guard_row(uintptr_t actor,uint32_t row){
    guard_row_calls++;
    if(row==0x3d){*(uint32_t*)(actor+0x164)=0xd4;*(float*)(actor+0x16c)=0;*(uint32_t*)(actor+0x70)=0;}
    return 0x1234;
}
static uintptr_t ABI native_motion_advance(uintptr_t actor,float delta){
    motion_calls++;last_motion_delta=delta;*(float*)(actor+0x16c)+=delta;return 0x5678;
}
static int ABI native_guard_angle(uintptr_t first,uintptr_t second){
    (void)first;angle_calls++;return *(float*)(second+0x10)>=0.f;
}
static uintptr_t ABI native_guard_create(uintptr_t actor,uint32_t mask,const void*data){
    uintptr_t pool=game_base+0x2db4710;
    for(unsigned i=0;i<64;i++){
        uintptr_t p=pool+i*0xc0;if(*(uint32_t*)p&0x800)continue;
        memset((void*)p,0,0xc0);*(uint32_t*)p=0x80800;
        *(uint32_t*)(p+0x34)=handle((void*)actor);*(uint32_t*)(p+0x5c)=handle(data);
        *(uint32_t*)(p+0x54)=mask;*(uint32_t*)(game_base+0x2db7710)|=mask;return p;
    }return 0;
}
static uint32_t ABI native_guard_mask(void){
    uint32_t used=*(uint32_t*)(game_base+0x2db7710);
    for(unsigned i=0;i<31;i++)if(!(used&(1u<<i)))return 1u<<i;
    return 0;
}
static void ABI native_guard_free(uintptr_t p){
    uint32_t mask=*(uint32_t*)(p+0x54);*(uint32_t*)p=0;
    *(uint32_t*)(game_base+0x2db7710)&=~mask;
}
static int ABI native_guard_pool(uintptr_t work){
    (void)work;return 19;
}
int bridge_guard_pool(uintptr_t f){return ((int(ABI*)(uintptr_t))f)(0);}
uintptr_t bridge_guard_row(uintptr_t f,uintptr_t actor,uint32_t row){return ((uintptr_t(ABI*)(uintptr_t,uint32_t))f)(actor,row);}
uintptr_t bridge_motion_advance(uintptr_t f,uintptr_t actor,float delta){return ((uintptr_t(ABI*)(uintptr_t,float))f)(actor,delta);}
int bridge_guard_angle(uintptr_t f,uintptr_t first,uintptr_t second){return ((int(ABI*)(uintptr_t,uintptr_t))f)(first,second);}
float bridge_motion_delta(void){return last_motion_delta;}
static float ABI native_move(uintptr_t actor,float*out){
    move_calls++;out[0]=1;out[1]=2;out[2]=3;out[3]=4;
    return *(float*)(actor+0x124);
}
static uint32_t ABI native_set_state(uintptr_t actor,uint32_t state){
    uint32_t old=*(uint32_t*)(actor+0x70);
    if(old!=state){*(uint32_t*)(actor+0x378)=old;*(uint32_t*)(actor+0x70)=state;*(uint32_t*)actor|=0x400;}
    return old;
}
float bridge_move(uintptr_t f,uintptr_t actor,float*out){return ((float(ABI*)(uintptr_t,float*))f)(actor,out);}
unsigned bridge_move_calls(void){return move_calls;}
static float ABI native_sinf(float x){return sinf(x);}
static char menu_drawn[4096];static unsigned menu_text_count,menu_panels,menu_last_sound,menu_rects,menu_glyphs,menu_scrolls;
static int menu_clip_on,menu_clip_top,menu_clip_bottom,menu_rect_data[32][5];
static unsigned menu_plain_count;static int menu_plain_words[128][4];static unsigned char menu_plain_texts[128][256];
void bridge_menu_reset(void){menu_drawn[0]=0;menu_text_count=menu_panels=menu_last_sound=menu_rects=menu_glyphs=menu_scrolls=menu_plain_count=0;menu_clip_on=0;}
unsigned bridge_menu_plain_count(void){return menu_plain_count;}
int bridge_menu_plain_word(unsigned row,unsigned field){return row<menu_plain_count&&field<4?menu_plain_words[row][field]:-1;}
uintptr_t bridge_menu_plain_text(unsigned row){return row<menu_plain_count?(uintptr_t)menu_plain_texts[row]:0;}
const char* bridge_menu_text(void){return menu_drawn;}
unsigned bridge_menu_panel_count(void){return menu_panels;}
unsigned bridge_menu_sound(void){return menu_last_sound;}
unsigned bridge_menu_rect_count(void){return menu_rects;}
unsigned bridge_menu_glyph_count(void){return menu_glyphs;}
unsigned bridge_menu_scroll_count(void){return menu_scrolls;}
int bridge_menu_rect_word(unsigned row,unsigned field){return row<menu_rects&&field<5?menu_rect_data[row][field]:-1;}
static int menu_clipped(int y){return menu_clip_on&&(y>=menu_clip_bottom||y+26<=menu_clip_top);}
static void ABI native_menu_sound(unsigned id){menu_last_sound=id;}
static void ABI native_menu_panel(uintptr_t w){(void)w;menu_panels++;}
static void ABI native_menu_text(uintptr_t w,int palette,int flags,int x,int y,int width,const unsigned char*text){
    (void)w;(void)palette;(void)flags;(void)x;(void)y;(void)width;
    if(menu_clipped(y))return;
    if(menu_text_count++&&strlen(menu_drawn)+1<sizeof(menu_drawn))strcat(menu_drawn,"|");
    size_t at=strlen(menu_drawn);
    while(*text&&at+1<sizeof(menu_drawn)){
        unsigned char c=*text++;menu_drawn[at++]=c==1?' ':c==2?'\n':c==0x68?'.':c==0x66?'/':c>=0x21&&c<=0x2a?(char)('0'+c-0x21):c>=0x2b&&c<=0x44?(char)('A'+c-0x2b):c>=0x45&&c<=0x5e?(char)('a'+c-0x45):'?';
    }menu_drawn[at]=0;
}
static void ABI native_menu_pill(uintptr_t w,int kind,int flags,int x,int y,int width,int text_x,uintptr_t color,const unsigned char*text,int font){
    (void)kind;(void)color;(void)font;if(menu_clipped(y))return;menu_panels++;
    native_menu_text(w,0,flags,text_x,y,width-x+text_x,text);
}
static void ABI native_menu_rect(uintptr_t w,int x,int y,int width,int height,uint32_t color){
    (void)w;if(menu_clipped(y)||menu_rects>=32)return;
    int*row=menu_rect_data[menu_rects++];row[0]=x;row[1]=y;row[2]=width;row[3]=height;row[4]=(int)color;
}
static void ABI native_menu_ap_panel(uintptr_t w,int x,int y,uint32_t color){
    native_menu_rect(w,x,y,*(int*)(game_base+0x545370),*(int*)(game_base+0x545380),color);
}
static void ABI native_menu_plain_text(uintptr_t w,int flags,int x,int y,const unsigned char*text,int font,uint32_t color,int wrap){
    (void)wrap;if(!menu_clipped(y)&&menu_plain_count<128){
      unsigned row=menu_plain_count++;menu_plain_words[row][0]=x;menu_plain_words[row][1]=y;menu_plain_words[row][2]=font;menu_plain_words[row][3]=(int)color;
      unsigned i=0;for(;i<255&&text[i];i++)menu_plain_texts[row][i]=text[i];menu_plain_texts[row][i]=0;
    }native_menu_text(w,0,flags,x,y,512,text);
}
static int ABI native_menu_width(const unsigned char*text,int font){int width=0;while(*text){unsigned c=*text++;if(c==2||c==3)break;width+=(font+1)/2;}return width;}
static unsigned char native_gpu_packets[32][4096];static unsigned native_gpu_count;
void bridge_gpu_reset(void){native_gpu_count=0;memset(native_gpu_packets,0,sizeof(native_gpu_packets));}
unsigned bridge_gpu_count(void){return native_gpu_count;}
uintptr_t bridge_gpu_packet(unsigned i){return i<native_gpu_count?(uintptr_t)native_gpu_packets[i]:0;}
static uintptr_t ABI native_gpu_alloc(unsigned bytes,unsigned align){
    (void)align;if(bytes>4096||native_gpu_count>=32)return 0;
    return (uintptr_t)native_gpu_packets[native_gpu_count++];
}
static void ABI native_menu_glyph(uintptr_t w,int x,int y,int width,int code,unsigned alpha){
    (void)w;(void)x;(void)width;(void)code;(void)alpha;if(!menu_clipped(y))menu_glyphs++;
}
static void ABI native_menu_clip(uintptr_t w){
    menu_clip_on=1;menu_clip_top=(*(int32_t*)(w+0xe0)-0x7400)/16;
    menu_clip_bottom=menu_clip_top+*(int16_t*)(w+0xfa)**(int16_t*)(w+0xf0)/16-*(int16_t*)(w+0xf4)/16;
}
static void ABI native_menu_unclip(void){menu_clip_on=0;}
static void ABI native_menu_scroll(uintptr_t w){if(*(uint16_t*)(w+0xf8)>*(uint16_t*)(w+0xfa))menu_scrolls++;}
static void ABI native_menu_nav(uintptr_t w){
    uintptr_t input=*(uintptr_t*)(game_base+0x2e95940);unsigned count=*(uint16_t*)(w+0xf8),visible=*(uint16_t*)(w+0xfa),top=*(uint16_t*)(w+0xfc)/16u,row=top+*(uint16_t*)(w+0xfe)/16u;
    if(!input||!count)return;uint32_t pressed=*(uint32_t*)(input+8);
    if(pressed&0x1000u)row=(row+count-1u)%count;
    if(pressed&0x4000u)row=(row+1u)%count;
    if(pressed&0x400u){row=row>visible?row-visible:0;}
    if(pressed&0x800u){row=row+visible<count?row+visible:count-1u;}
    if(row<top)top=row;if(row>=top+visible)top=row-visible+1u;
    *(uint16_t*)(w+0xfc)=(uint16_t)(top*16u);*(uint16_t*)(w+0xfe)=(uint16_t)((row-top)*16u);
}
uintptr_t bridge_symbol(const char*n){
    if(!strcmp(n,"NumberedPersist"))return (uintptr_t)numbered_save;
    if(!strcmp(n,"NativeMenuApPanel"))return (uintptr_t)native_menu_ap_panel;
    if(!strcmp(n,"NativeMenuPlainText"))return (uintptr_t)native_menu_plain_text;
    if(!strcmp(n,"NativeMenuWidth"))return (uintptr_t)native_menu_width;
    if(!strcmp(n,"NativeGpuAlloc"))return (uintptr_t)native_gpu_alloc;
    if(!strcmp(n,"NativeMenuPill"))return (uintptr_t)native_menu_pill;
    if(!strcmp(n,"NativeMenuRect"))return (uintptr_t)native_menu_rect;
    if(!strcmp(n,"NativeMenuGlyph"))return (uintptr_t)native_menu_glyph;
    if(!strcmp(n,"NativeMenuClip"))return (uintptr_t)native_menu_clip;
    if(!strcmp(n,"NativeMenuUnclip"))return (uintptr_t)native_menu_unclip;
    if(!strcmp(n,"NativeMenuScroll"))return (uintptr_t)native_menu_scroll;
    if(!strcmp(n,"NativeMenuText"))return (uintptr_t)native_menu_text;
    if(!strcmp(n,"NativeMenuPanel"))return (uintptr_t)native_menu_panel;
    if(!strcmp(n,"NativeMenuSound"))return (uintptr_t)native_menu_sound;
    if(!strcmp(n,"NativeMenuNav"))return (uintptr_t)native_menu_nav;
    if(!strcmp(n,"NativeSinf"))return (uintptr_t)native_sinf;
    if(!strcmp(n,"NativeGuardCreate"))return (uintptr_t)native_guard_create;
    if(!strcmp(n,"NativeGuardMask"))return (uintptr_t)native_guard_mask;
    if(!strcmp(n,"NativeGuardFree"))return (uintptr_t)native_guard_free;
    if(!strcmp(n,"NativeGuardPool"))return (uintptr_t)native_guard_pool;
    if(!strcmp(n,"NativeGuardRow"))return (uintptr_t)native_guard_row;
    if(!strcmp(n,"NativeMotionAdvance"))return (uintptr_t)native_motion_advance;
    if(!strcmp(n,"NativeGuardAngle"))return (uintptr_t)native_guard_angle;
    if(!strcmp(n,"GetModuleHandleA"))return (uintptr_t)get_module;
    if(!strcmp(n,"GetModuleFileNameW"))return (uintptr_t)file_name;
    if(!strcmp(n,"VirtualQuery"))return (uintptr_t)query;
    if(!strcmp(n,"CreateFileW"))return (uintptr_t)create_file;
    if(!strcmp(n,"WriteFile"))return (uintptr_t)write_file;
    if(!strcmp(n,"CloseHandle"))return (uintptr_t)close_file;
    if(!strcmp(n,"GetPrivateProfileIntW"))return (uintptr_t)profile;
    if(!strcmp(n,"NativeDecode"))return (uintptr_t)native_decode;
    if(!strcmp(n,"NativeGlideCommon"))return (uintptr_t)native_glide_common;
    if(!strcmp(n,"NativeAppend"))return (uintptr_t)native_append;
    if(!strcmp(n,"NativeMove"))return (uintptr_t)native_move;
    if(!strcmp(n,"NativeSetState"))return (uintptr_t)native_set_state;
    if(!strcmp(n,"NativeControl"))return (uintptr_t)native_control;
    if(!strcmp(n,"NativeQueue"))return (uintptr_t)native_queue;
    if(!strcmp(n,"NativeHandle"))return (uintptr_t)handle;
    if(!strcmp(n,"VirtualAlloc"))return (uintptr_t)valloc;
    if(!strcmp(n,"VirtualFree"))return (uintptr_t)vfree;
    if(!strcmp(n,"VirtualProtect"))return (uintptr_t)vprotect;
    if(!strcmp(n,"FlushInstructionCache"))return (uintptr_t)flush;
    if(!strcmp(n,"NativeMatrix"))return (uintptr_t)native_matrix;
    if(!strcmp(n,"NativePoint"))return (uintptr_t)native_point;
    return 0;
}
void bridge_call0(uintptr_t f){((void(ABI*)(void))f)();}
void bridge_init(uintptr_t f){((void(ABI*)(const uint16_t*))f)(0);}

static void ABI integrated_note(const char*s){uint32_t done;write_file(7,s,(uint32_t)strlen(s),&done,0);write_file(7,"\n",1,&done,0);}
int adapter_init(uintptr_t fn,uintptr_t game,int shared){uintptr_t api[]={(uintptr_t)query,(uintptr_t)valloc,(uintptr_t)vfree,(uintptr_t)vprotect,(uintptr_t)flush,(uintptr_t)integrated_note,(uintptr_t)native_move};return ((int(ABI*)(uintptr_t,uintptr_t*,int))fn)(game,api,shared);}
int adapter_frame(uintptr_t fn,uintptr_t actor,int choice,uint64_t epoch){return ((int(ABI*)(uintptr_t,int,uint64_t))fn)(actor,choice,epoch);}
void adapter_control(uintptr_t fn,uintptr_t actor,uintptr_t dir){((void(ABI*)(uintptr_t,uintptr_t,uintptr_t))fn)(actor,dir,(uintptr_t)native_control);}
void adapter_observe(uintptr_t fn,uintptr_t actor){((void(ABI*)(uintptr_t))fn)(actor);}
int call_int0(uintptr_t fn){return ((int(ABI*)(void))fn)();}
uintptr_t call_ptr1(uintptr_t fn,uintptr_t a){return ((uintptr_t(ABI*)(uintptr_t))fn)(a);}
void call_void1(uintptr_t fn,uintptr_t a){((void(ABI*)(uintptr_t))fn)(a);}
void call_panel(uintptr_t fn,uintptr_t w,int x,int y,uint32_t color){((void(ABI*)(uintptr_t,int,int,uint32_t))fn)(w,x,y,color);}

uintptr_t call_ptr2(uintptr_t fn,uintptr_t a,uintptr_t b){return ((uintptr_t(ABI*)(uintptr_t,uintptr_t))fn)(a,b);}
