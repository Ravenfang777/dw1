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
u32 ABI VentusTestChoice(void){for(unsigned i=0;i<VENTUS_TEST_COUNT;i++)if(numbered_bits&(1ull<<i))return 3u+i;return 0u;}
static void numbered_toggle(u32 id){int index=numbered_index(id);if(index>=0)numbered_commit(numbered_bits^(1ull<<index));}

u32 ABI DarkTestChoice(void){for(unsigned i=0;i<DARK_TEST_COUNT;i++)if(numbered_bits&(1ull<<(i+VENTUS_TEST_COUNT)))return i+1u;return 0u;}
static const char*const dark_test_help[4]={
 "Dark Riku. Ground 3/4/5. Air 8/9/10.",
 "Dark Riku. Ground 11/12/13. Air 14/15/16.",
 "Dark Riku. Ground 17/18/19. Air 20/21/22.",
 "Dark Riku. Ground 23/24/25. Air 26/27/27."
};
static const char*numbered_test_help(unsigned id){return id<DARK_TEST_FIRST?terra_test_help[id-VENTUS_TEST_FIRST]:dark_test_help[id-DARK_TEST_FIRST];}
