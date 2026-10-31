KH1FM SEVEN STYLES -- PROTOTYPE v38 (s377)

INSTALL
1. Fully close KH1FM. Disable v37 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v38, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s377 / PROTOTYPE v38 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save entries are preserved.

SINGLE C -- REMOVE THE REMAINING 182 FOLLOW-UP
v37 ended at frame 92 and still showed a brief unwanted horizontal swing.
v38 ends 182 at frame 77, fifteen frames earlier, after the preceding hit.
Original source: 148 frames. Total tail removed: 71. Playback speed, original
pose/weapon data and root prefix are preserved. Only this host finisher changes.

Keep contact windows 17..34, 45..55 and 69..77. Remove both 82..92 and108..122.
All hit/trail/hold windows end with the visible clip. Discarded damage is not
shifted or amplified into earlier hits. The original installed bank is unchanged.

Your s376 log confirms both combo lanes load and records 182 through84/85 then
normal fall, without a sampled Horizontal Slash restart. The remaining82..92
source portion is the candidate unwanted follow-up. Periodic logging does not
identify every visual frame, so please check the new endpoint in game.

The added real-controller test repeatedly presses Attack through the full air
combo and20 recovery frames. It verifies Sora first hit -> Horizontal Slash ->
Riku182 and no extra attack afterward. No engine/input/blend/native hook change.

PRESERVED
Ground: Riku152 -> Riku151 -> Vicinity Break.
Air: KH2 Sora first air hit -> Horizontal Slash -> shortened Riku182.
Horizontal Slash remains the normal second air-combo step. Combo Plus and
Air Combo Plus keep input-driven continuation. Native KH1 attack abilities
retain priority; unequip relevant modifiers to isolate this base sequence.
Keep confirmed v36 source validation and independent ground/air admission,
separate Riku/Sora rigs/battle/retargets, native Square/Triangle, Quick Run,
aerial193 Cure/Stop/Aero/Gravity casting/parry, grounded item casts and spell FX.
All other six styles, equipment/appearance, Glide attachment/colors and Dual A
Superglide finisher are preserved. Only Dual A/B/C duplicate the equipped weapon.

FIRST TEST
Equip Style: Single C and perform the complete air combo. Confirm182 ends on
the intended downward slash and no unwanted extra horizontal swing appears.
The log should show ground_ready=true, air_ready=true, Riku182_length=77 and
trimmed_tail=71 in SINGLE C COMBO MAP. If the endpoint remains off, a short
recording will help identify the exact last pose. Return the fresh full log
if admission or input behavior fails.

IDs (exclusive,0 AP): Dual A126, Dual B125, Single A124, Single B123,
Anti122, Dual C121, Single C120. Unequipping restores native behavior.
INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full game restart.
To remove entries: set remove_dual_wield on; launch/load/save with v38;
close; disable the mod and Build again.

VALIDATION AND LIMITS
511 tests /31 suites /161 style tests pass. Windows x64 release, existing
four exports/eight imports,109 source checks,11 native anchors and seven
protected model checks pass. Builds use -C codegen-units=1. Existing tests
verify the77-frame root prefix, three exact hits, no late contact/trail/hold,
source identity and native ability rules; the added test covers repeated input.
ZIP CRC, independent extraction, every entry hash and saved-copy checks pass.
No actual v38 game/GPU or installed animation playback was run here. The exact
visual downward-slash endpoint still needs the fresh game test.

Source patch (38 derivative commits), pinned upstream, credits/licences and
validation receipts are included. Rules/confidence: docs/combat-model.md
Stage377. No game executable, extracted asset, recording or disassembly ships.
