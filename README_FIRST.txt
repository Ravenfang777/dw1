KH1FM NINE STYLES -- PROTOTYPE v42 (s381)

INSTALL
1. Fully close KH1FM. Disable v41 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v42, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s381 / PROTOTYPE v42 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save settings are retained.

DUAL D -- THREE TIMES THE TRAVEL, ORIGINAL TIMING
This corrects v41's misunderstanding of the requested change.
Jump normally, release Jump/Circle, then press it again in free air.
The Master Aerial Dodge runs at its original animation/controller speed.
Its requested rise and directional travel are multiplied by3. The animation,
weapon tracks, defensive window and tap/hold rules keep their original timing.
The ending airborne handoff velocity is scaled with the move too.
KH1 collision remains active: a wall, ceiling or early landing can shorten
actual travel. Landing/damage/native commands can interrupt it normally.
One use per airtime; land to rearm. Requires the existing native Glide ability.
Circle is default; KH1's confirm/jump swap remains respected.
Other actions are unscaled. No new attack, invulnerability or growth grant.

QUICK RUN / GUARD / SUPERGLIDE
Dual D keeps v41's Wisdom Quick Run (203/end204) with both Master blades,
normal native Dodge Roll selection/ability gates and held/released input.
It also keeps the corrected KH2 base Sora Guard pose and native block rules.
Superglide retains native movement and its held offhand weapon.
Dual A Superglide remains its actual attack finisher.

SINGLE D -- DARK RIKU MAIN BANK SOURCE CAPTURE
The chosen source is KH1 Dark Riku's main bank, xa_ex_1160.
The previous CSV contains slot numbers/durations but not skeleton or curves.
A playable Dark Riku retarget cannot be built from that metadata alone.
This version automatically reads the original main MDLS/MSET and writes:

  kh1-dual-wield-dark-riku-main.zip

It is beside KINGDOM HEARTS FINAL MIX.exe, with kh1-dual-wield.log.
After launch, wait for SINGLE D MAIN SOURCE CAPTURE COMPLETE in the log.
Then return that generated source ZIP and the full log to continue Single D.
No enemies, attacks, manual archive extraction or F1 reload are needed.
You do not need to equip Single D to create the source capture.
If a different capture already exists, a numbered ZIP is written instead;
the log reports the exact complete path. Identical captures are reused.
If capture fails, return the startup log with the failure marker.

The generated capture ZIP is source data, NOT an OpenKH mod. Do not install it.
It contains only xa_ex_1160.mdls/.mset, a README and parser/rig diagnostics.
All original IK/helper bytes are kept, including data our FK reader cannot yet
evaluate. Parser warnings remain in capture_report.txt for investigation.
It is generated locally on your PC; no automatic upload occurs.
Single D STILL USES NATIVE KH1 MOVES until the source rig/moves are mapped.
No animation names, hit windows or boss AI have been guessed. No duplicate.
The alternate1168 and Ansem/Riku1580/1588 banks are not used for this capture.
DARK_RIKU_ANIMATION_LIST.txt retains the previous full74-slot metadata list.

FIRST TEST
- Dual D: compare Aerial Dodge speed against its original speed; it should cover
  more distance while finishing in the original time. Test neutral/directional
  input, tap/hold/release, turning, walls and landing, then another jump.
- Confirm both blades stay aligned, and Quick Run, Guard, attacks, casts and
  Superglide still work. Test a map change and switching/unequipping styles.
- Return the generated Dark Riku main source ZIP and kh1-dual-wield.log.
Useful markers: DUAL D AERIAL DODGE DATA / START: distance=3x; timing=original
SINGLE D MAIN SOURCE CAPTURE COMPLETE (or FAILED).

PRESERVED
Menu order: Single A/B/C/D, Dual A/B/C/D, Anti. All9 entries are exclusive,0 AP.
IDs: Singles A124/B123/C120/D119; Duals A126/B125/C121/D118; Anti122.
Only Dual styles duplicate the currently equipped weapon. No second selection,
gauge, outfit, party, stat or extra ability changes.
Single C keeps its77-frame Riku182 endpoint, ground/air sequence, Quick Run,
193 air cast/parry, native Square/Triangle and KH1 attack-ability priority.
Other B Quick Run/Guard/Fire and Anti restrictions/effects are retained.
Master combos/hops/body3 finisher, magic and separate trails are retained.
INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full restart.
To remove entries: set remove_dual_wield on; launch/load/save with v42;
close; disable the mod and Build again.

VALIDATION AND LIMITS
530 tests across31 suites, including172 style tests, pass. Windows x64 release,
4 exports/8 imports,79 source-scope checks,15 native anchors and7 model checks
pass. Builds use -C codegen-units=1. No new native hook/address/dependency.
Controller tests compare3x travel and unchanged frame/state/guard timing,
tap/hold/release, directional steering, terminal velocity and ground retirement.
Paired synthetic model/motion capture preserves exact IK/helper bytes and
reports a mismatched skeleton; an independent Python ZIP decoder verifies CRCs,
binary and empty entries. No external ZIP/Python dependency in the game DLL.
Installer ZIP CRC, extraction and every entry hash are verified.
No actual v42 game/GPU test or original Dark Riku payload playback here.
Source patch (42 derivative commits), credits/licences and validation included.
Rules/confidence: docs/combat-model.md Stage381. No game assets or dumps ship.
