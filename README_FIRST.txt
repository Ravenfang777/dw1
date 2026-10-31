KH1FM SEVEN STYLES -- PROTOTYPE v37 (s376)

INSTALL
1. Fully close KH1FM. Disable v36 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v37, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s376 / PROTOTYPE v37 in kh1-dual-wield.log beside the game EXE.

Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save entries are preserved.

SINGLE C -- END RIKU 182 ON THE MIDDLE SLASH
You confirmed v36 works and clarified that the desired endpoint is the large
downward slash near the middle of 182. The proposed 50-frame additional cut
would end at 88, crossing a source hit window. This test ends at frame 92,
after that complete hit window, removing the later follow-up.

Original source: 148 frames.
v36: 138 frames.
v37: 92 frames (56 removed from original; 46 more than v36).
Playback speed, root prefix and original body/weapon poses are preserved.
Only the Single C air-finisher alias changes; raw installed assets do not.

Four complete source contacts remain: 17..34, 45..55, 69..77 and 82..92.
The final 108..122 contact is removed. All hit/trail/hold windows end with the
visible clip; removed damage is not shifted or amplified into earlier hits.
This boundary is inferred from the source contact timing near your suggested
cutoff. The actual downward-slash pose was not viewed here, so please check
that 92 is the exact visual endpoint you mean in the fresh game test.

COMBOS AND OTHER FEATURES PRESERVED FROM WORKING v36
Ground: Riku 152 -> Riku 151 -> KH2 Vicinity Break.
Air: KH2 Sora first air hit -> Horizontal Slash -> shortened Riku 182.
Ground/air Combo Plus retain their normal input-driven continuation rules.
Native KH1 attack abilities retain priority; temporarily unequip relevant
attack modifiers if needed to isolate this listed base sequence.

Keep the confirmed named-Sora source validation and independent ground/air
admission. Triangle commands remain removed; no custom aerial Square action.
Aerial Cure/Stop/Aero/Gravity keep Riku 193 and the existing scoped native
casting guard/parry; ground versions keep item-use pose 9. Quick Run, Sora
fallback poses, matching KH2 spell effects and native KH1 spell behavior remain.
The other six styles, equipment/appearance, Glide attachment/colors and Dual A
Superglide finisher are unchanged. No new ability, gauge or command is added.
Only Dual A/B/C duplicate the equipped weapon; Single C keeps one weapon.

FIRST TEST
Equip Style: Single C and perform the three-hit air combo. Confirm Riku 182
ends after the intended downward slash, without the later follow-up or extra
late trail/damage. The log should show ground_ready=true, air_ready=true,
Riku182_length=92 and trimmed_tail=56 in SINGLE C COMBO MAP.
If the cutoff is still off, a short recording of 182 will help identify the
precise pose boundary. If admission fails, return the full fresh log including
SINGLE C SORA SOURCE, SINGLE C COMBO MAP and any LANE UNAVAILABLE messages.

IDs (exclusive, 0 AP): Dual A126, Dual B125, Single A124, Single B123,
Anti122, Dual C121, Single C120. Unequipping restores native behavior.
INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full game restart.
To remove our entries, set remove_dual_wield on; launch/load/save with v37;
close; disable the mod and Build again.

VALIDATION AND LIMITS
510 tests / 31 suites / 161 style tests pass. Windows x64 release, the existing
four exports/eight imports, 109 source checks, 11 native anchors and seven
protected model metadata checks pass. Builds use -C codegen-units=1.
Existing controller tests verify the 92-frame root prefix, four exact hits,
omission of the fifth hit and bounded trail/hold/contact windows. Source
checks preserve the complete working v36 policy and native runtime paths.
ZIP CRC, independent extraction, every entry hash and saved-copy checks pass.
No actual v37 game/GPU or installed animation playback was run here.

Source patch (37 derivative commits), pinned upstream, credits/licences and
validation receipts are included. Rules/confidence: docs/combat-model.md
Stage 376. No game executable, extracted asset, recording or disassembly ships.
