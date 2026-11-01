KH1FM NINE STYLES -- PROTOTYPE v50 (s389)

SINGLE D COMBO LOOKUP FIX
Your s388 log confirms the jump works, native basic attacks/hits run, and the
Dark Riku solver/map admit. No new combo pose was admitted. v49 confused native
attack request IDs200..206 (C8..CE) with animation-bank records98..104.

v50 uses decoded regular MSET records for combo admission. It selects the
requested basic record before checking the actual current native header,
avoiding ambiguous counts-only signature guesses. Exact request/header,
state/lane, actor/binding, scene/script and hold checks remain mandatory.
The working Single C jump route/calibration and its paired timeline are exact.

INSTALL
1. Fully close KH1FM. Disable v49 and every older Dual Wield prototype.
2. Import THIS ZIP through OpenKH, enable only v50, then Build and Run.
   Requires Panacea and installed KH2FM resources. F1 cannot reload a DLL.
   Keep full KH2 Combat overhaul, old offhand/moveset Lua and duplicate Sora
   model mods disabled. Existing INI/save settings remain.
3. Confirm s389 / PROTOTYPE v50 in kh1-dual-wield.log beside the game EXE.

TEST
Equip Style: Single D and test basic ground and aerial combos on one enemy.
Check each swing and finisher, weapon grip, effects and normal idle/fall return.
Recheck the working jump, interruptions and a map change. Native attack ability
replacements still take priority; temporarily unequip those only if you want
to isolate basic mapped motions. Return the fresh log if a combo still fails.
No additional source capture is needed.

EXPECTED LOG
SINGLE D BASIC COMBO ACTIVE reports request, decoded bank_slot, signature_slot,
source_slot/frame and native phase. Ground bank98/100,99,101 uses18,19,20;
air bank102,103,104 uses18,19,21. Each action kind logs once, not every hit.
SINGLE D SINGLE C JUMP READY confirms the existing jump calibration.
MAPPING WAIT now reports decoded bank and signature guess separately. Scene/
control/landing handoffs can be normal. Report unexpected MAP UNAVAILABLE,
MAPPING POSE REJECTED or FINAL POSE REJECTED with the complete log.

UNCHANGED GAMEPLAY/SCOPE
Same candidate Dark Riku swings: ground18->19->20; air18->19->21. Their native
boss script names/order/contact windows remain unverified. KH1 owns combo
selection/repeats/modifiers, ability priority, hit timing, damage, movement,
swing/impact sounds and feedback. No donor hit windows, HP writes, private
attack controller, script, voice or AI is introduced by this fix.
Single C jump, D idle/walk/run/fall/landing, leg alignment, own lengths/scales,
checked secondary rest and skin guards remain. One equipped weapon. Other D
actions remain native pending later mapping. All other styles, contacts/FX,
Quick Run, Superglide/finishers and confirmed2x Aerial Dodge routes remain.
Nine exclusive0-AP entries; no ability grants, gauge, stats, outfit or party change.

VALIDATION
596 tests/31 suites pass (174 style,16 body map,13 D policy). New regressions
exercise request-descriptor decode -> bank resolution -> combo selection ->
source sampler for all7 basic requests, control flags and signature aliases.
Windows x64 release: same4 exports/8 imports.26 scope checks protect287 other
tracked files and exact working jump/publication/controller/contact code.
Source solver/body map/swings are unchanged; prior geometry proofs are retained
as labelled history. No new native hook/address or dependency. The50-commit
source patch, ZIP CRC/extraction and every file hash are checked before delivery.
Fresh-process v50 in-game combo admission and hit alignment still need testing.
No raw user log, original game assets/executables or pose streams ship.
Restart after DLL/INI changes. Removal: set remove_dual_wield on, launch/load/
save with v50, close, disable the mod and Build again.
