KH1FM NINE STYLES -- PROTOTYPE v40 (s379)

INSTALL
1. Fully close KH1FM. Disable v39 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v40, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s379 / PROTOTYPE v40 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save settings are retained.

DUAL D -- OFFHAND IN SUPERGLIDE AND DODGE ROLL
The held-weapon drawing gates now include Master. Both native actions attach
the duplicate to Sora's actual skinned palm on each body draw, with current
weapon colors and binding/freshness guards. Their native body, primary weapon,
movement, input and ability checks remain. No new hitbox/trail is added here.
Master has no Roll donor, so Dodge Roll keeps its native KH1 animation.

DUAL D -- MASTER AERIAL DODGE IN PLACE OF REGULAR GLIDE
Jump normally. Release Jump/Circle, then press it again in free air to start
Master's actual Aerial Dodge (motion202, body and both weapon tracks).
Circle is the default; this respects KH1's confirm/jump button swap.
Neutral stick rises vertically; tilt the stick for directional movement.
Holding Jump affects the rise through the existing KH2 variable-jump rules.
One use per airtime; land to rearm. Holding the takeoff button does not dodge.
It requires the existing native Glide shared ability and ready donor data.

Ordinary Glide is replaced only for Dual D. Holding Circle will not enter old
Glide or repeat the dodge. Superglide retains its separate native action.
The dodge keeps Master's authored defensive window. It adds no attack hitbox,
invulnerability, gauge, stats, growth ability, outfit or other menu skill.
Completion/interruption returns native control/fall at the current position.
If the checked Glide hook or required donor data is unavailable, native Glide
remains as the fallback. Other styles keep their existing air controls.

FIRST TEST
- Equip Dual D. Jump, release Circle, then tap Circle in air with neutral stick.
- Repeat with a direction. Try holding the second press, then releasing early.
- Try another airborne press: it should not dodge again until you land.
- Check both weapons through the dodge, Superglide and moving Dodge Roll.
- Check turning, landing, damage interruption, native spells, map transitions
  and switching/unequipping styles. Confirm the duplicate retires correctly.
- Dual A Superglide remains the real attack finisher; check it independently.

Useful log markers:
DUAL D AERIAL DODGE DATA: body_and_both_weapon_tracks=true movement_snapshot=true
DUAL D AERIAL DODGE HOOK: installed=true
DUAL D AERIAL DODGE START
HELD GLIDE DRAW / HELD GLIDE COLORS (also used for Master's held Roll fallback)
Return the full fresh log if admission, movement or weapon visibility fails.

DARK RIKU ANIMATION INVENTORY
The supplied CSV/log successfully captured74 readable slots across4 banks.
Dark Riku's main xa_ex_1160 bank has31 clips; its alternate1168 bank has1.
DARK_RIKU_ANIMATION_LIST.txt lists every captured slot, duration and metadata,
including the separately labeled Ansem/Riku banks1580/1588 (41/1).
Action names are unverified. Durations do not identify attacks or movement.
Single D still retains native moves: full boss source/rig data and mapping are
needed for its playable adapter. Metadata alone is not the animation payload.
The read-only original-package inventory capture remains available at startup.

PRESERVED
Menu order: Single A/B/C/D, Dual A/B/C/D, Anti. All9 entries are exclusive,0 AP.
IDs: Singles A124/B123/C120/D119; Duals A126/B125/C121/D118; Anti122.
Only Dual styles duplicate the currently equipped weapon. No second selection.
Master's base combos, intrinsic hops, body3 finisher, native-priority attack
ability lanes, matching casting, shared spell effects and separate trails remain.
Single C ground Riku152 -> Riku151 -> Vicinity Break; air Sora181 -> Horizontal
Slash ->77-frame Riku182; Quick Run,193 air cast/parry, native Square/Triangle.
All existing B Quick Run/guard/fire, native spell ownership, Anti restrictions,
Glide attachment/colors and Dual A's actual Superglide finisher remain.

INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full restart.
To remove entries: set remove_dual_wield on; launch/load/save with v40;
close; disable the mod and Build again.

VALIDATION AND LIMITS
521 tests across31 suites, including169 style tests, pass. Windows x64 release,
existing4 exports/8 imports,93 source-scope checks,15 native anchors and7 model
checks pass. Builds use -C codegen-units=1. One new native hook: regular Glide
constructor, checked against its prologue/subtype and shared initializer.
Regression tests exercise finite neutral/directional motion and guarding,
no damage/events/ability grants, rejected invalid inputs, one-use input lease,
binding retirement and native Master held-action selection.
ZIP CRC, independent extraction, every entry hash and saved-copy checks pass.
No actual v40 game/GPU or installed animation playback has run here. This build
needs a fresh game test for input timing, dodge travel and weapon visibility.

Source patch (40 derivative commits), upstream, credits/licences and validation
receipts are included. Rules/confidence: docs/combat-model.md Stage379.
No game executables, extracted animation/model assets, dumps or recordings ship.
