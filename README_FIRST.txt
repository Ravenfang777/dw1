KH1FM NINE STYLES -- PROTOTYPE v41 (s380)

INSTALL
1. Fully close KH1FM. Disable v40 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v41, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s380 / PROTOTYPE v41 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save settings are retained.

DUAL D -- AERIAL DODGE LASTS THREE TIMES AS LONG
Jump normally. Release Jump/Circle, then press it again in free air.
The Master Aerial Dodge now lasts three times its v40 duration when allowed to
finish. Its original rise height and movement path remain; the whole action
takes longer, with smooth body and both weapon sampling every game frame.
Landing, damage or a native command can still interrupt it normally.
One use per airtime; land to rearm. Requires the existing native Glide ability.
Circle is the default; KH1's confirm/jump swap remains respected.
The source defensive window follows the longer animation, with no added
offensive hit, invulnerability, spell effect or growth ability.
Only this action uses the slower clock. Other animation/movement speeds remain.

DUAL D -- DODGE ROLL BECOMES WISDOM QUICK RUN
Use your normal Dodge Roll input. Native Dodge Roll selection/ability gates
start the existing Wisdom Quick Run controller/body (203 and end204), with both
Master weapon tracks and both equipped-weapon copies visible.
Holding/releasing the dodge input uses the existing Quick Run duration/end rules.
Master's own attacks, movement, magic and Aerial Dodge stay on Master data.
Quick Run retains the existing controller's normal startup protection.
No shot, spell, extra attack, stat or growth ability is granted.

DUAL D -- KH2 SORA GUARD
Use your normal Guard input with the native Guard ability available.
The visual now uses KH2 Sora's actual Guard press correctly. The previous
Master path selected that donor but failed its separate retarget lookup,
which had only been initialized for the C styles. This version uses Master's
normal base-Sora correspondence for the Guard body.
Native blocking, ability checks, command/row selection and sounds remain.
Moving Dodge Roll selection goes to Quick Run through the normal native rules.
No raw Square attack/spin or new guard ability is added.

FIRST TEST
- Dual D: compare the longer airborne Circle dodge with v40. Test neutral and
  directional input, a tap and a held press, then landing and another jump.
- Check both weapons remain aligned throughout the complete slower dodge.
- Test Quick Run with a held and released dodge input; confirm it reaches its
  end animation and returns control without leaving an invisible/green blade.
- Guard with the normal native ability/input. Confirm the KH2 Sora pose appears
  and incoming hits are blocked normally. Then move/dodge, attack and cast.
- Check Superglide, map changes and switching/unequipping styles.
Return the full fresh log if a source/controller fails or a pose is wrong.

Useful log markers:
DUAL D AERIAL DODGE DATA / START: duration=3x
DUAL D QUICK RUN DATA: adapter=true movement_snapshot=true
DUAL D QUICK RUN REQUEST / START
STYLE NATIVE GUARD WITNESS
DUAL WIELD VISUAL ACTIVE: action=guard source=KH2 Sora

PRESERVED
Master's original base combos/hops/body3 finisher, casts and separate trails.
Superglide retains its native movement and held duplicate; Dual A Superglide
remains its actual attack finisher. All other style input/control routes remain.
Menu order: Single A/B/C/D, Dual A/B/C/D, Anti. All9 entries are exclusive,0 AP.
IDs: Singles A124/B123/C120/D119; Duals A126/B125/C121/D118; Anti122.
Only Dual styles duplicate the currently equipped weapon. No second selection,
gauge, outfit, party, stat or extra ability changes.
Single C keeps its77-frame Riku182 endpoint, ground/air sequence, Quick Run,
193 air cast/parry, native Square/Triangle and KH1 attack-ability priority.
Other B Quick Run/Guard/Fire and Anti restrictions/effects are retained.

DARK RIKU
DARK_RIKU_ANIMATION_LIST.txt retains the captured74-slot metadata list.
Dark Riku's main bank has31 clips plus1 alternate; separate Ansem/Riku banks
have41/1. Action names remain unverified. Single D still retains native moves:
full source/rig data and playable mapping are pending. No game assets ship.

INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full restart.
To remove entries: set remove_dual_wield on; launch/load/save with v41;
close; disable the mod and Build again.

VALIDATION AND LIMITS
526 tests across31 suites, including172 style tests, pass. Windows x64 release,
existing4 exports/8 imports,93 source-scope checks,15 native anchors and7 model
checks pass. Builds use -C codegen-units=1. No new native hook/address in v41.
New tests compare original/slow neutral/directional and tapped/held trajectories,
3x duration/guard time and slowed exit velocity; verify pose-cache retirement,
finite Master Quick Run and fractional body/root/two-weapon phase sampling.
The original RigAnim update path and normal character controller are preserved.
ZIP CRC, independent extraction, every entry hash and saved-copy checks pass.
No actual v41 game/GPU or installed animation playback has run here; please
test the new duration, Quick Run blades and Sora Guard in a fresh game process.

Source patch (41 derivative commits), upstream, credits/licences and validation
receipts are included. Rules/confidence: docs/combat-model.md Stage380.
No game executables, animation/model assets, dumps or recordings ship.
