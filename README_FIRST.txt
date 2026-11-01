KH1FM NINE STYLES -- PROTOTYPE v51 (s390)

SINGLE D: REPLACE THE WRONG COMBO ANIMATIONS
The prior18/19/20/21 choices were misidentified from body-only thumbnails.
v51 uses main Dark Riku clips29 ->30 ->28 for both basic combo lanes.
The captured original battle script links these to native weapon attacks;
the main MSET request table independently resolves231/232/230 to those clips.
This establishes attack association, not a live test of the adapted player.
The playable order is our choice; named boss techniques/order remain unverified.

INSTALL
1. Fully close KH1FM. Disable v50 and every older Dual Wield prototype.
2. Import THIS ZIP through OpenKH, enable only v51, then Build and Run.
   Panacea and installed KH2FM resources are required. F1 cannot reload a DLL.
   Keep the full KH2 Combat overhaul, old offhand/moveset Lua and duplicate
   Sora model mods disabled. Existing INI/save settings remain.
3. Confirm s390 / PROTOTYPE v51 in kh1-dual-wield.log beside the game EXE.

TEST
Equip Style: Single D. Check the first swing, second swing and finisher on
the ground, then all three in the air. Start with whiffs, then one enemy.
Recheck the working Single C jump, landing, interruptions and a map change.
Native attack abilities retain priority; unequip their replacements only if
you want to isolate the basic mapped combo. Return the fresh log if a selected
clip still looks wrong or fails. No additional source capture is needed.

EXPECTED LOG
SINGLE D MELEE SOURCE VERIFIED: source requests231/232/230 -> clips29/30/28.
SINGLE D BASIC COMBO ACTIVE: current native request/decoded bank/signature,
source_slot, source_frame, native_phase and source_request, once per action kind.
Ground/air first29, second30, finisher28. SINGLE D SINGLE C JUMP READY confirms
the preserved jump route. Report unexpected source/map/final-pose rejection.
An absent/changed/unreadable source request mapping safely retains native moves.

SCOPE
Both lanes reuse the same three boss weapon attacks. This is a pose adapter,
not a full boss combat/event importer or a distinct authored player air combo.
KH1 keeps combo progression/count/repeats, Combo Plus, attack ability priority,
actor movement, hit timing, contacts, damage, sounds/trails and native feedback.
Original boss hit windows/projectiles/AI/scripts/damage values are not imported.
Adapted animation-to-native-contact timing still needs the game test.

v50's request-to-bank fix remains. Single C jump/calibration/paired timeline,
D idle/walk/run/fall/landing, hip alignment, checked rest and skin guards remain.
Other D actions retain native KH1 animation pending later mapping. One equipped
weapon. Every other style, contact/FX route, Quick Run, Superglide/finishers and
confirmed2x Aerial Dodge routes remain. Nine exclusive0-AP abilities; no ability
grants, gauge, stats, outfit or party change.

VALIDATION
597 tests/31 suites pass (174 style,16 body-map,14 D policy). Windows x64
release succeeds with the existing4 exports/8 imports.23 scope checks protect
286 other tracked files and exact working jump/publication/controller routes.
New source admission checks require the actual source request mappings;
the captured main bank passes. Source script findings are in validation;
no bytecode/table dump ships. Solver/body-map metrics retained from earlier
versions are historical geometry evidence, not a new game/GPU appearance test.
The51-commit source patch, ZIP CRC/extraction and file hashes are checked.
Restart after DLL/INI changes. Removal: set remove_dual_wield on, launch/load/
save with v51, close, disable the mod and Build again.
