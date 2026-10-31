KH1FM NINE STYLES -- PROTOTYPE v43 (s382)

INSTALL
1. Fully close KH1FM. Disable v42 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v43, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s382 / PROTOTYPE v43 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save settings are retained.

AERIAL DODGE -- TWICE THE ORIGINAL DISTANCE
The same Master Aerial Dodge now replaces REGULAR Glide for:
  Style: Single A
  Style: Single C
  Style: Dual C
  Style: Dual D

It requests2x its original travel (rise and directional movement), reduced
from v42's3x. Animation/controller speed and guard duration stay original.
Jump normally, release Jump/Circle, then press it again in free air.
One use per airtime; land to rearm. Requires the existing native Glide ability.
Circle is default; KH1's confirm/jump swap remains respected.
Holding/releasing uses the original dodge rules. Repeated taps cannot extend
it forever. Walls, ceilings, landing, damage and native commands still apply.
No offensive hit, spell, added invulnerability or growth ability is granted.

Single A/C retain one weapon; Dual C/D retain their equipped-weapon duplicate.
The C variants use Master/Sora body calibration during this action, then return
to their normal Riku/Roxas rigs. Master body, source weapon tracks, attachment
binds and body size are selected together for the shared action.
If complete replacement data fails admission, native control is retained.

SUPERGLIDE AND OTHER STYLES
Superglide keeps its current behavior for every style, including Single A and
Dual A's actual attack-finisher paths. This change affects regular Glide only.
Dual A, Dual B, Single B, Single D and Anti receive no new Aerial Dodge route.
Quick Run, Guard, attacks, magic and items retain their current routes.
Dual D retains its Wisdom Quick Run, held Superglide weapon and KH2 Sora Guard.
Dual A's stable standard Glide grip/color and finisher remain.
Single C keeps ground152/151/Vicinity Break, its mixed air combo with77-frame
Riku182,193 air casts/parry, Quick Run and native Square/Triangle behavior.

FIRST TEST
For Single A, Single C, Dual C and Dual D separately:
- Jump, release/repress Circle in free air; compare timing and increased travel.
- Try neutral and directional input, tap/hold/release, steering and landing.
- Confirm Single styles show one weapon and Dual styles show both correctly.
- Land, attack and cast; test Quick Run/Guard where available and Superglide.
- Switch styles and change maps, then repeat.
Useful log markers: STYLE AERIAL DODGE HOOK / DATA / START
The START marker includes style, distance=2x, timing=original and duplicate.
Return the full fresh kh1-dual-wield.log if the action fails or poses are wrong.

SINGLE D -- MAIN DARK RIKU SOURCE RECEIVED
The supplied main1160 source ZIP is valid:247 bones,31 clips,12 helpers each,
no parser warnings. The source files are now available for adapter development.
No additional capture is needed for this work.
Offline FK inspection confirms that the arm/leg IK chain joints have no direct
keyed channels in any31 clips. The current FK evaluator leaves those limbs
straight; a proper helper/constraint solver is needed before retargeting moves.
Single D therefore STILL USES NATIVE KH1 MOVES. Its playable adapter is pending.
No slot names, hit windows, boss AI or raw animation pointers were guessed.
The source remains xa_ex_1160; alternate1168 and Ansem/Riku banks are excluded.
The automatic local source capture remains available for diagnostic use.
Its generated ZIP is source data, NOT an OpenKH mod; do not install it.
No game assets, poses, skeleton dumps, recordings or original files ship here.
DARK_RIKU_ANIMATION_LIST.txt retains the earlier numbered74-slot inventory.

PRESERVED CONFIGURATION
Menu order: Single A/B/C/D, Dual A/B/C/D, Anti. All9 entries are exclusive,0 AP.
IDs: Singles A124/B123/C120/D119; Duals A126/B125/C121/D118; Anti122.
Only Dual styles duplicate the currently equipped weapon. No second selection,
gauge, outfit, party, stat or extra ability changes. Native attack-ability
priority, existing B Fire/effects/Quick Run and Anti restrictions are preserved.
INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full restart.
To remove entries: set remove_dual_wield on; launch/load/save with v43;
close; disable the mod and Build again.

VALIDATION AND LIMITS
531 tests across31 suites, including173 style tests, pass. Windows x64 release,
4 exports/8 imports,90 source-scope checks,15 native anchors and7 model checks
pass. Builds use -C codegen-units=1. No new native hook/address/dependency.
Tests cover2x travel with original frame/state/guard timing, steering,
tap/hold/release, terminal/ground behavior, exact four-style eligibility,
C calibration routing and unchanged single/dual weapon policy.
The existing ordinary animation sampler and native world mover remain.
Installer ZIP CRC, extraction and every entry hash are verified.
No actual v43 game/GPU test here; please test all four styles in a fresh process.
Source patch (43 derivative commits), credits/licences and validation included.
Rules/confidence: docs/combat-model.md Stage382.
