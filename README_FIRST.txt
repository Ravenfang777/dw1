KH1FM NINE STYLES -- PROTOTYPE v45 (s384)

FIRST DARK RIKU TO SORA MAPPING TEST
Single D now draws Dark Riku's solved body poses on Sora for idle, walking,
running, takeoff, rise/apex, falling and landing. This is the first movement
mapping test. Attacks, magic, items, damage, Guard, Roll, ledges and glides
still use native KH1 execution/poses for Single D. Attack timing/contact mapping
is the next stage after body alignment. Every other style is preserved.

INSTALL
1. Fully close KH1FM. Disable v44 and every older Dual Wield prototype.
2. Import THIS ZIP in OpenKH, enable only v45, then Build and Run.
   OpenKH Panacea and the installed KH2FM resources are required.
   Keep the full KH2 Combat overhaul, older moveset/offhand Lua and duplicate
   Sora model mods disabled. F1 cannot reload a native DLL.
3. Confirm s384 / PROTOTYPE v45 in kh1-dual-wield.log beside the game EXE.
   Normal Sora; existing INI and save settings remain in use.

TEST
1. Equip Style: Single D (exclusive, one equipped weapon, no extra abilities).
2. Stand idle, then walk, run and turn. Inspect both arms, knees, fingers and
   the primary Keyblade grip from several camera angles.
3. Jump and land several times. No enemy is needed.
4. Change map and enter/leave battle; check the stance and movement return.
   Native attacks/casts are expected during this first mapping test.
5. Unequip Single D and check normal movement returns. Other styles retain
   their existing behavior, including the confirmed 2x Aerial Dodge changes.
Return the complete fresh kh1-dual-wield.log and describe any twist, stretching,
weapon offset, body drift or movement action that stayed native.
The source bank is already received: no additional source ZIP is needed.

EXPECTED LOG
SINGLE D SOLVER READY -- installed main bank admitted as in v44 (1829 poses).
SINGLE D MAP READY -- current Sora rig admitted: mapped=103 source_joints=101.
SINGLE D MOVEMENT ACTIVE -- once per movement kind, with source slot/frame.
SINGLE D MAPPING WAIT -- bounded diagnostic when an action stays native;
  a transient line during a scene, input lock or handoff can be expected.
MAP UNAVAILABLE / MAPPING POSE REJECTED leaves the current native pose in place.

WHAT THE MAP DOES
101 active Dark Riku source joints turn 103 of Sora's 293 joints. Sora keeps
his own body proportions, secondary local motion and one equipped weapon.
The primary/free hand correspondence is explicit; no second blade is created.
Dark Riku's root travel is removed; KH1 owns actor movement and collision.
The live Sora bone table supplies calibration each instance; it is not a raw
boss skeleton or animation-pointer swap. No boss AI, scripts or source sword.

First main-bank assignments (movement labels inferred from solved sequences):
Native action       | Dark Riku source slot
Idle                | 0
Walk                | 1
Run                 | 2
Takeoff             | 3
Rise/apex           | 4 then 5 on the same native phase
Fall                | 6
Landing             | 7
Idle uses idle_speed (default 0.75) on the pause-aware game clock.
Other movement follows the native clip phase. One-shots hold their end.

PRESERVED
Single A/B/C/D, Dual A/B/C/D, Anti: nine exclusive entries, all 0 AP.
Single A/C and Dual C/D keep the confirmed 2x-distance, original-speed Master
Aerial Dodge in regular Glide. All existing Superglide routes, Dual A's real
finisher, Quick Run, Guard, spell effects, attack abilities and contacts remain.
No gauge, outfit, party, stats, weapon-selection menu or other ability grant.
INI defaults remain dual_b_spell_fx=on, idle_speed=0.75,
offhand_only_test=off, remove_dual_wield=off. Restart after DLL/INI changes.
To remove the entries: set remove_dual_wield on; launch/load/save with v45;
close, disable the mod and Build again.

VALIDATION
578 tests / 31 suites pass: 173 existing style tests, 7 new body-map tests,
5 new movement-route tests. Windows x64 release passes, same 4 exports and
8 runtime imports. No new game hook, address or runtime/Cargo dependency.
25 source checks preserve 282 other tracked files, the existing KH2 retarget,
the v44 authored solver and all prior gameplay policies/controllers.
All 31 clips map offline over 2139 sampled poses (10,027,632 float components).
Independent matrix-reference maximum position difference: 0.0001121 units.
Maximum limb-length error: 0.0000191 units; native bind-grip error: 0.0000263.
The separate skeleton GIF illustrates source and Sora proportions. It is an
offline numeric preview, not game video or proof of final skin/grip alignment.
Actual v45 game/GPU validation remains pending.

Source patch (45 commits), licences, credits and validation receipts included.
README_MAPPING.txt explains the calibration, limits and reproduction.
README_SOLVER.txt retains the v44 native-source comparison method. Its
native parity/anchor receipts are inherited evidence: no new native CPU
comparison was required because the source solver and hook sites are unchanged.
Installer CRC, extraction and every file hash are verified before delivery.
No original game executables, model/animation files, raw skeleton dumps,
decompiler output or pose streams ship in this installer.
