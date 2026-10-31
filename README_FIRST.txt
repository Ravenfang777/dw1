KH1FM NINE STYLES -- PROTOTYPE v39 (s378)

INSTALL
1. Fully close KH1FM. Disable v38 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v39, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s378 / PROTOTYPE v39 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save settings are retained.

STATUS: EIGHT PLAYABLE STYLES + ONE SOURCE-INVENTORY ENTRY
Menu: Single A, Single B, Single C, Single D, Dual A, Dual B, Dual C, Dual D, Anti.
All are exclusive, 0 AP, initially disabled. Enabling one disables the other.
Old IDs do not change: A124/B123/C120 singles, A126/B125/C121 duals, Anti122.
New IDs: Single D119, Dual D118. Native abilities/save entries are not evicted.
No gauge, outfit changes, bonus stats, party changes or extra abilities.
Only Dual styles duplicate the current equipped weapon; no second selection.

DUAL D -- MASTER FORM BASE
Master's original ability-free ground/aerial combos, built-in hops and spinning
body-contact finisher use existing native KH1 contacts/feedback. Matching idle,
movement, jump/fall/land, damage, item and interaction poses use Master when
available. Both weapon tracks, held/floating attachment and separate source
trail windows are used. No donor object/AI/spell/voice/effect scripts run during
melee combos. Existing native attack abilities retain priority.

Guard uses base KH2 Sora's Guard pose on the normal KH1 Guard action. Glide and
Superglide retain native held-blade movement/pose with visual duplication.
This does not change Dual A's actual Superglide attack finisher.

Master casts use matching KH2 body/weapon poses with native KH1 costs, damage,
healing and targeting. Existing shared KH2 effects cover Fire, Blizzard, Thunder
and Cure (Master form sub20); Gravity, Stop and Aero retain native effects.
Only admitted same-level replacement visuals hide owned native drawing.
The existing dual_b_spell_fx=on setting also enables these replacements.

SINGLE D -- DARK RIKU SOURCE CAPTURE, NOT A PLAYABLE MOVESET YET
The original KH1 Dark Riku assets are not available in this workspace. Assigning
unknown boss animation numbers would be guessing. The new exclusive entry
therefore retains normal KH1 moves and one weapon during this capture stage.
Its menu help and equip log explicitly say mapping is pending.

On startup this build automatically reads the original installed Dark Riku banks
and attempts to write kh1-dual-wield-dark-riku-animations.csv beside the game EXE,
in the same folder as kh1-dual-wield.log. No enemy/fight/attack is needed.
Wait for SINGLE D INVENTORY COMPLETE in the log. Return the generated CSV and
fresh full log so the actual numbered list can be provided and attacks mapped.
If capture fails or no CSV appears, return the log's SINGLE D INVENTORY UNAVAILABLE
or BANK NOT READ messages. Other styles remain independently usable.
More source/format notes: DARK_RIKU_AND_BBS.txt.

FIRST TEST
- Equip Dual D. Check idle/movement, ground and aerial combos, turning, native
  Guard, ordinary Glide/Superglide, both blades, trails and impacts on one enemy.
- Unequip native attack modifiers while isolating Master base combos; re-equip
  them to check native priority. Try map changes and switching among styles.
- Cast Fire/Blizzard/Thunder/Cure on ground/in air, then attack and move. Check
  costs/damage/healing stay native and no stale animation or trail remains.
- Confirm equipping a different style removes the old duplicate/controller.
Return the full fresh log if a donor or attack adapter fails to admit.

PRESERVED
Single C's complete data adapter remains unchanged: ground Riku152 -> Riku151 ->
Vicinity Break; air Sora181 -> Horizontal Slash -> Riku182 shortened to77 frames.
Its Quick Run, 193 aerial Cure/Stop/Aero/Gravity/parry, normal Square/Triangle,
grounded item casts and native ability priority remain. All other existing style
controllers, native combat backend, B dodges/guard/fire and standard Glide
attachment/colors are preserved. Dual A Superglide remains the real finisher.

INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full game restart.
To remove entries: set remove_dual_wield on; launch/load/save with v39;
close; disable the mod and Build again.

VALIDATION AND LIMITS
517 tests across31 suites, including165 style tests, pass. Windows x64 release,
existing4 exports/8 imports,88 source-scope checks,11 native anchors and7 model
checks pass. Builds use -C codegen-units=1. ZIP CRC, independent extraction,
every entry hash and exact saved-copy verification accompany delivery.
No actual v39 game/GPU playback or original Dark Riku bank parsing was run here.
Master's visual timing/attachment/gameplay still need a fresh game test.
Single D's source inventory is the prerequisite to implementing its moveset.

Source patch (39 derivative commits), pinned upstream, credits/licences and
validation receipts are included. Rules/confidence: docs/combat-model.md
Stage378. No game executables, extracted assets, dumps or recordings ship.
