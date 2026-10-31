KH1FM SIX STYLES -- PROTOTYPE v29 (s368)

INSTALL
1. Fully close KH1FM. Disable v28 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v29, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s368 / PROTOTYPE v29 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not Lua. Keep the full KH2 Combat
overhaul, older offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied. Your existing INI is preserved.

WHY DUAL C STILL USED KH1 MOVES
The supplied s367/v28 log successfully reads playable P_EX110_BTLF:
229 bones, 32 motions, 10 rows, real weapon joints 172 and 63.
Sora's equivalent hand joints are 178 and 86. v28 still measured Sora's
numbered landmarks directly on Roxas, rejected landmark 4 and left
playable dual Roxas=false / attack_adapter=false. The ability equipped,
but no imported Roxas moveset ran.

V29 CHANGE
Build a separate correspondence from the actual loaded hand attachments,
ordered arm/leg ancestor paths, branch ancestry and normalized bind positions.
Use the map and Roxas's own bind to calibrate body-part retargeting.
Keep the raw motion channels, weapon joints/tracks and collision bones intact.
Do not apply Sora's numbered hair/hood map to Roxas: C uses weapon-chain-only
secondary motion, with KH1's existing native rest for hair/hood.

Require finite valid hierarchy/bind, plausible limb/foot geometry and 17
nondegenerate core frames. Unmeasured helpers/wardrobe need no exact match;
missing finger-detail branches inherit the hand. The matching tolerances
are our implementation choices, not native game constants. This is an
inferred correspondence, so actual installed rig/rendering still needs a test.

CONFIRMED GLIDE AND WORKING STYLES
The complete Glide attachment/color file, ability/combo policy, controllers,
A's actual Superglide finisher, B's Quick Run/Guard/Fire/effects and C's
filename/profile resolver are unchanged from v28. Original retarget pose,
secondary and inverse implementations are also unchanged; only C selects
the new mapped source calibration and weapon-only secondary construction.

FIRST TEST
1. Start a fresh game process and equip Style: Dual C.
2. Check idle/run/jump, then a basic ground and aerial combo.
3. Startup should show:
   DUAL C ASSETS READ ... weapon_joints=[Some(172), Some(63)]
   DUAL C RIG MAP ADMITTED ... hands=... core_parts=17 ...
   DUAL C DONOR LOADED ...
   DUAL C DATA ... playable dual Roxas=true attack_adapter=true
Equipping the menu entry alone does not prove donor admission.

If it is still native, or a pose is wrong, return the FULL fresh log including
startup. It now reports the inferred body roles and exact map failure.
Native KH1 attack ability lanes deliberately retain priority; missing donor
slots, spells, Guard and Roll keep native behavior. C's held native Glide/
Superglide remain separate from its imported base ground/air attack rows.

RETAINED
Six exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed),
Dual C 121 (playable dual Roxas). Equipping any style cancels the others.
Only A/B/C duplicate the currently equipped weapon. No second weapon
selection, costume, Drive state/gauge, stat reward, extra ability or
party removal. C uses real authored base ground/air two-blade contacts
and matching poses when the installed donor is admitted. Existing native
Combo Plus/Air Combo Plus policy remains. Single B Run .75/Guard, Anti's
weaponless moves/aura and magic/item/summon restrictions remain.

Your existing kh1-dual-wield.ini is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Offhand-only testing affects Dual weapon contacts, not spells or party.
To remove custom entries: set remove_dual_wield on; launch/load/save with
v29; close; disable the mod and Build again. Only the six custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
477 tests pass across 31 suites (151 style tests), including five new map
regressions: reordered branches/different indices/counts, inserted/omitted
helpers, missing finger detail, proportions, moving limbs/head/root, inverse,
weapon-only secondary and invalid/degenerate sources. Production retargeted
KH1 matrix outputs are compared across differently indexed animated rigs.
Windows x64 release, PE interface, 164 source/preservation checks, 11 native
anchors and 7 protected-model metadata checks pass. ZIP CRC, independent
extraction and saved-copy entry hashes are verified.

No live v29 game/GPU test or actual installed Roxas asset execution was
performed here. Synthetic fixtures do not prove that every inferred joint
matches the installed rig or every motion renders correctly. This is a test
build. Source patch, pinned upstream, credits/licences and validation receipts
are included. No game executable, recording, extracted asset or disassembly
is distributed. Source behavior/confidence: docs/combat-model.md Stage 368.
