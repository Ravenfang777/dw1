KH1FM NINE STYLES -- PROTOTYPE v46 (s385)

SINGLE D STABILITY FIX
Targets v45's intermittent Dark Riku movement and stretched model/blob.
The log admits the solver and map, but rejects secondary helper joints and
returns to KH1. v45 also allowed oversized finite skin bases through its final
origin-only check. This version removes live secondary-cache inputs from Single
D, uses checked immutable Sora rest/bind transforms, preserves their bind scale
and validates the final bone bases before drawing. Invalid rest helpers recover
individually instead of dropping the whole valid mapped body.

INSTALL
1. Fully close KH1FM. Disable v45 and every older Dual Wield prototype.
2. Import THIS ZIP into OpenKH, enable only v46, then Build and Run.
   Panacea and installed KH2FM resources are required. F1 cannot reload a DLL.
   Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
   Sora model mods disabled. Existing INI/save settings remain in use.
3. Confirm s385 / PROTOTYPE v46 in kh1-dual-wield.log beside the game EXE.
A fresh game process is required to clear the old DLL and pose/simulation state.

TEST
Use normal Sora and equip Style: Single D.
Stand idle, walk, run, turn, jump, fall and land repeatedly. Then change map,
enter/leave battle and repeat. Check that the Dark Riku movement keeps appearing
and the model, fingers and equipped Keyblade stay intact. No enemy is needed
for the movement test. Unequip Single D to check normal movement returns.
Return the complete fresh kh1-dual-wield.log and describe any remaining dropout,
stretch, blob or grip offset. Source files are already received; no new capture.

EXPECTED LOG
SINGLE D SOLVER READY -- original main bank checked (as in v44/v45).
SINGLE D MAP READY -- mapped=103 source_joints=101; secondary_rest=N/190;
  checked immutable Sora rest; live secondary cache disabled; final skin-basis
  guard; one equipped weapon. Unseeded rest entries use their own bind.
SINGLE D MOVEMENT ACTIVE -- once per movement kind.
MAPPING WAIT during a scene/control lock/handoff can be normal. The script and
native action guards are preserved. MAP UNAVAILABLE, MAPPING POSE REJECTED or
FINAL POSE REJECTED should be returned in the complete log.

MAPPING TEST SCOPE
Same movement assignments as v45: idle 0, walk 1, run 2, takeoff 3,
rise/apex 4 then 5, fall 6, landing 7. Idle uses idle_speed (default 0.75),
other movement uses native phase; one-shots hold their end.
Hair, cloth and keychain use the checked rest while mapped Single D movement
is active. The shared secondary simulation is paused there to isolate this
repair. Other styles retain their existing secondary motion.
Single D attacks, magic, items, Guard, Roll, damage, ledges and glides still
use native KH1 execution/poses during this first body-mapping test.
Sora retains his own proportions and one equipped weapon. No extra blade.

PRESERVED
The solver, anatomical correspondence, field/script/hold guards and movement
sampling are unchanged. All other styles, attacks, spell effects, contacts,
Quick Run, Superglide/finishers and the confirmed 2x Aerial Dodge routes remain.
Nine exclusive style entries, all 0 AP; no other ability, stat, outfit, party,
gauge or weapon-selection change. INI defaults remain dual_b_spell_fx=on,
idle_speed=0.75, offhand_only_test=off, remove_dual_wield=off.
Restart after DLL/INI changes. Removal: set remove_dual_wield on, launch/load/
save with v46, close, disable the mod and Build again.

VALIDATION
584 tests / 31 suites pass, including 173 existing style tests and 13 body-map
tests (six new). Windows x64 release: same 4 exports and 8 runtime imports.
25 source checks preserve 287 other tracked files. No new native hook/address,
Cargo or runtime dependency. The original solver and action policies are exact.
All 2139 mapped poses / 31 clips are byte-identical to v45's clean offline output.
A same-rig comparison reproduces v45 pose drops and 100x finite skin scales;
all 12 injected secondary faults recover with normal scale in v46.
These tests reproduce code defects. The user's failing live matrix values were
not captured. Actual v46 game/GPU/skin validation remains pending.

README_SECONDARY_FIX.txt explains the repair. Source patch (46 commits),
licences, credits and validation receipts included. Original source-solver and
v45 mapping comparisons are retained as labelled historical evidence.
Installer CRC, extraction and every file hash are verified before delivery.
No original game executables, model/animation files, decompiler output,
raw live caches or pose streams ship in this installer.
