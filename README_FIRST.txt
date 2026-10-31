KH1FM NINE STYLES -- PROTOTYPE v47 (s386)

SINGLE D LEG AND JUMP REFINEMENT
Corrects the hip placement behind the narrow/crossed stance. Source3's
rotation did not match the solved hip separation used by the leg poses.
The map now derives the pelvis turn from the solved hips and torso, retaining
Sora's own hip width, bone lengths and scales. The upper body and equipped
weapon mapping are unchanged.

Takeoff, rising and falling now share source6: the falling animation from v46.
It plays once at normal source timing, then holds its end until native landing
or interruption. Rise/fall transitions and native animation-clock wraps cannot
restart it. Repeated drawing and paused game time do not advance it.
Landing still uses source7. Native jump height, controls and collision remain.

INSTALL
1. Fully close KH1FM and disable v46 and all older Dual Wield prototypes.
2. Import THIS ZIP in OpenKH, enable only v47, then Build and Run.
   Requires Panacea and installed KH2FM resources. F1 cannot reload the DLL.
   Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
   Sora model mods disabled. Existing INI/save settings remain in use.
3. Confirm s386 / PROTOTYPE v47 in kh1-dual-wield.log beside the game EXE.

TEST
Use normal Sora, equip Style: Single D, and check the legs from front/back
and side while idle, walking, running and turning. Repeat standing and moving
jumps; walk off a ledge for a longer fall if convenient. The previous falling
pose should now remain through the air, holding after its single play.
Check landing, a second jump, map changes and battle entry/exit. Unequipping
Single D should restore normal movement. No enemy is needed for this test.
Return the fresh log and describe any remaining leg clipping or jump issue.
No new source capture is needed; the original main bank is already received.

EXPECTED LOG
SINGLE D SOLVER READY -- original checked main1160 source.
SINGLE D MAP READY -- mapped=103 source_joints=101; checked rest; solved hip
  frame; airborne source6 play-once/hold; one equipped weapon.
SINGLE D MOVEMENT ACTIVE -- airborne kinds use source_slot=6. Logged once
  per action kind; a single line is not a per-frame recording of the hold.
MAP UNAVAILABLE, MAPPING POSE REJECTED or FINAL POSE REJECTED are unexpected.
MAPPING WAIT during scenes/control locks/landing handoffs can be normal.

CURRENT SINGLE D SCOPE
Idle0, walk1, run2; takeoff/rise/fall6 once then held; landing7.
Idle uses idle_speed (default0.75). Walking/running/landing retain native phase.
Checked immutable Sora rest supplies hair/cloth/keychain during mapped moves,
so those parts remain more rigid for this test. The v46 final skin-basis guard
and bind-scale retention remain. All unmodified native actions, including
Single D attacks, magic, items, Guard, Roll, damage, ledges and glides, keep
their native execution/poses. Combat/contact mapping is still pending.

PRESERVED
All other styles, combos, magic effects, contacts, Quick Run, Superglide and
finishers, including Dual A's finisher. Confirmed regular Glide replacements
for Single A/C and Dual C/D retain2x Aerial Dodge travel and original timing.
Nine exclusive0-AP style entries; Singles retain one equipped weapon, Duals
use an equipped-weapon duplicate. No extra ability, stat, outfit, party, gauge
or weapon-selection change. Existing INI defaults remain idle_speed=0.75,
dual_b_spell_fx=on, offhand_only_test=off and remove_dual_wield=off.
Removal: set remove_dual_wield on, launch/load/save with v47, close the game,
disable the mod and Build again. Restart after DLL/INI changes.

VALIDATION
590 tests /31 suites pass (173 existing style tests;16 map tests;8 D policy
and clock tests). Windows x64 release passes with the same4 exports/8 imports.
All2139 mapped poses/31 clips pass independent matrix/invariant comparison.
Across494 samples of slots0..7,49 incorrectly crossed lateral foot placements
become0. Only65 pelvis-descendant matrices change;228 other joint matrices
are byte-identical to v46. Maximum hip-width error0.0000058 model units.
22 source checks preserve286 other tracked files. No new native hooks,
addresses or Cargo/runtime dependencies. The original solver is unchanged.
Offline matrix checks do not prove live mesh clearance or in-game timing.
Actual v47 game/GPU validation requires this fresh-process test.

README_MAPPING.txt describes the current calibration and timing. The v46
secondary repair and v44 native solver proofs are retained as labelled history.
Source patch47 commits, licences, credits and validation receipts included.
ZIP CRC, extraction and every packaged file hash checked before delivery.
No original game assets, executables, decompiler output or pose streams ship.
