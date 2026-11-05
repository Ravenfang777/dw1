/* The50 remaining unused native IDs have mod-wide test equip flags, outside save arrays. */
#define NUMBERED_COUNT 50u
#define NUMBERED_MASK (((1ull<<51u)-1ull)&~(1ull<<49u))
#define VENTUS_TEST_FIRST 66u
#define VENTUS_TEST_COUNT 35u
#define DARK_TEST_FIRST 101u
#define DARK_TEST_COUNT 4u
#define ANIMATION_TEST_COUNT 39u
#define ANIMATION_TEST_MASK ((1ull<<ANIMATION_TEST_COUNT)-1ull)
#define VENTUS_TEST_MASK ((1ull<<VENTUS_TEST_COUNT)-1ull)
#if TERRA_PROFILE_COUNT != VENTUS_TEST_COUNT + 2
#error Regenerate the shared payload with all Ventus numbered test profiles
#endif
/* IDs66..104 now select KH2 visual-only weapon effects, not body profiles. */
static const char*const*weapon_fx_text;
static u32 (ABI *weapon_fx_status)(u32);
static int weapon_fx_enabled=1;
void ABI WeaponFxPreviewInit(uptr descriptions,uptr status){weapon_fx_text=(const char*const*)descriptions;weapon_fx_status=(void*)status;}
void ABI WeaponFxEnable(u32 enabled){weapon_fx_enabled=enabled!=0;}
static u64 numbered_bits;
static void (ABI *numbered_persist)(u64);
static int numbered_index(u32 id){return id>=66u&&id<=114u?(int)(id-66u):id==127u?50:-1;}
static u8 numbered_id(unsigned index){return index<49u?(u8)(66u+index):index==49u?127u:0u;}
static int numbered_equipped(u32 id){int index=numbered_index(id);return index>=0&&(numbered_bits&(1ull<<index))!=0;}
static int numbered_is_test(u32 id){return id>=VENTUS_TEST_FIRST&&id<VENTUS_TEST_FIRST+ANIMATION_TEST_COUNT;}
static u64 numbered_exclusive(u64 bits){u64 tests=bits&ANIMATION_TEST_MASK;return (bits&~ANIMATION_TEST_MASK)|(tests&(~tests+1ull));}
static void numbered_commit(u64 bits){
 bits=numbered_exclusive(bits&NUMBERED_MASK);if(bits==numbered_bits)return;numbered_bits=bits;if(numbered_persist)numbered_persist(bits);
}
void ABI NumberedPassivesInit(u64 bits,uptr persist){numbered_bits=numbered_exclusive(bits&NUMBERED_MASK);numbered_persist=(void*)persist;}
u32 ABI VentusTestChoice(void){return 0u;}
u32 ABI WeaponFxChoice(void){if(remove_mode||!weapon_fx_enabled)return 0u;for(unsigned i=0;i<ANIMATION_TEST_COUNT;i++)if(numbered_bits&(1ull<<i))return VENTUS_TEST_FIRST+i;return 0u;}
static void numbered_toggle(u32 id){int index=numbered_index(id);if(index>=0)numbered_commit(numbered_bits^(1ull<<index));}

u32 ABI DarkTestChoice(void){return 0u;}
static const char*numbered_test_help(unsigned id){return weapon_fx_text&&numbered_is_test(id)?weapon_fx_text[(id-VENTUS_TEST_FIRST)*3u]:"KH2 weapon effect preview";}
