KH1FM DUAL STYLES -- PROTOTYPE v10 (s349)

Install this ZIP as one OpenKH mod, replacing v9. The animation data is
read from your own KH2FM installation; no game assets are included.

FIX IN v10
The Ranged cast observer no longer reads spell levels through the disabled
Reflect/overhaul module. Its private game base was never initialized in
this isolated mod, producing an invalid memory-read path when a real cast
started. The level value was not needed to select Final's cast animation.

Final ground/air casting remains enabled. Native KH1 spell levels, MP,
effects/damage and recovery remain native. Both exclusive styles, Attack
restrictions and floating weapon contacts are retained.

FIRST TEST
1. Fully restart with v10 and equip Style: Dual Ranged.
2. Cast Fire once on the ground, away from enemies; then try aerial Fire.
3. Repeat near one enemy, then check the other six spells and style
   switching. Revisit Style: Dual Close as a regression check.
4. If it still crashes, return the NEW kh1-dual-wield.log from beside the
   game executable. The exact user exception was not available here;
   v10 removes the concrete invalid-read path found by source inspection.

THE TWO ABILITIES
Style: Dual Close (existing ability 126, renamed)
- Retains v8's Valor ground/aerial combat, native attack-ability lane
  priority, rising Guard attack, shared slower idle and Final glides.
- Ground and aerial casting remain the default KH1 animations.
- Its existing equipped/disabled state is preserved on update.

Style: Dual Ranged (new ability 125, zero AP, initially unequipped)
- Uses matching Final Form visuals for the same admitted movement, idle,
  item, common damage and recognized interaction/cutscene-idle actions.
- Both copies of the currently equipped KH1 weapon follow Final's
  floating weapon poses, including their authored blade spin.
- Uses Final's ground/aerial casting visuals for all seven KH1 spells.
  KH1 still supplies MP costs, spell levels, rate/recovery, targets,
  projectiles, effects, sounds and spell damage.
- Attack is disabled. Normal combos, native attack-ability rows,
  counterattack routes, and physical special commands/follow-ups are
  blocked. Sonic Blade, Ars Arcanum, Strike Raid, Ragnarok and Trinity
  Limit are not offered while Ranged is active.
- It never runs a Final combo controller or a spell-to-attack follow-up.
  Native Guard and Dodge Roll remain available if already equipped;
  Guard does NOT become the Close style's rising attack in Ranged.
- The floating weapons can hurt enemies during their actual Final
  non-melee weapon-hit windows, including jumping, falling/landing and
  gliding where those windows exist. Damage is not an always-on aura.
  Both blades use the displayed equipped weapon's length and native
  contact/impact sound/effects. Only real weapon-hit windows are used;
  Final body/spell hitboxes and scripts do not create additional spells.
  Scene idles are visual only. No continuous swing-trail emitter is added.

MUTUALLY EXCLUSIVE
Equipping either style automatically unequips the previous style. Both
ability entries remain learned. Only those two equipped flags change;
other abilities, their order and AP are retained. Old poses, casts,
contacts and emitters are retired when the style changes. Unequipping
the active style restores normal KH1 behavior and removes the duplicate.

Both styles duplicate whichever KH1 weapon is currently equipped. There
is no second weapon selection or inventory copy, Drive gauge/drain/timer,
costume/recolour, partner removal, stat/AP bonus or extra native ability.

FINAL CASTING DONORS
Fire: Final Fire ground/air.
Blizzard: Final Blizzard ground/air.
Thunder: Final Thunder ground/air.
Cure: Final Cure ground/air.
Gravity: Final Thunder ground/air.
Stop and Aero: Final Cure ground/air.
Gravity/Stop/Aero keep their actual KH1 spell behavior. Their donor choice
is visual. The cast follows its verified native motion clock and stops on
interruption or a style/map/weapon change. Exact release sync needs a
fresh-process game test.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable v9 and every earlier Dual Wield prototype; enable only v10.
   Keep old integrated/offhand Lua, Synch/moveset routers, embedded
   duplicate Sora-model assets and the full KH2 Combat overhaul disabled.
2. Install this ZIP in OpenKH Mods Manager for Kingdom Hearts Final Mix,
   enable it, then Build and Run. Panacea is required.
3. Load your save. The old Dual Wield entry is now Style: Dual Close.
   Existing style entries/equipped states are reused. New entries start
   unequipped. Equip either style.
4. Stand idle briefly for weapon/pose admission, then test. KH1FM and
   KH2FM must be in the same PC 1.5+2.5 installation folder. Normal Sora
   is required. F1 does not reload this native DLL; restart the game.

Do not rename/install this DLL as the shared dinput8.dll. The manifest
loads dll/kh1-dual-wield.dll through OpenKH/Panacea.

TEST v10
- Equip Close, then Ranged: verify Close becomes unequipped. Reverse
  the switch and verify Ranged becomes unequipped. Save/reload and repeat.
- In Ranged, verify Attack is greyed and cannot be triggered from the
  menu, casting, Guard/counterattack or equipped attack abilities.
  Talk/Open/Examine, magic shortcuts and normal items must still work.
- Check Final idle, walk/run, jumps, fall/landing, item/damage actions,
  both glides, and all seven ground/air spells. Check both weapon poses.
- Jump/fall/glide close to one enemy and check floating blade contacts.
  Compare a whiff. Exclude party damage when attributing enemy HP loss.
- Change maps and equipped weapons, then switch styles and unequip.
  Check that old poses/trails/hits stop and normal KH1 Attack returns.
- Return to Close as a regression check, including native combo abilities
  and its rising Guard attack with native Guard equipped.

SETTINGS -- EXISTING INI PRESERVED
kh1-dual-wield.ini is beside KINGDOM HEARTS FINAL MIX.exe.
  idle_speed = 0.75
Changes both styles' combat and supported scene-idle speed. 1.0 is the
original rate; 0.50 is half rate. Accepted range 0.10..2.00. Restart to read.

  offhand_only_test = off
Use off to test BOTH blades. An existing on value still isolates the
left imported contacts, including Close Guard/glide and Ranged floating
contacts. It does not block native spells, items or party damage.

  remove_dual_wield = off
For uninstall only: set on, launch with v10, load and save, close the game,
then disable the mod and Build again. This removes both custom style
entries and preserves the other abilities/save data.

LOG
kh1-dual-wield.log is beside the game executable/INI. Check s349 and
PROTOTYPE v10. Useful lines: DUAL STYLE CHANGED, DUAL STYLE READY,
DUAL CLOSE VISUAL DATA, DUAL RANGED VISUAL DATA, DUAL RANGED CAST DONOR,
DUAL RANGED FINAL CAST and DUAL STYLE FLOATING CONTACT READY.
Return the NEW log and a short recording for an incorrect transition.

COVERAGE AND VALIDATION
Supported regular-bank actions retain the prior strict request/header
checks. Missing Final clips and unmatched native gestures retain native
body poses and a cosmetic hand-following duplicate. Dedicated EVM/event
poses, chest opening, carrying/pushing/throwing objects and Trinities are
not blanket-replaced. There is no promise that every animation contains
a damaging weapon window. Stale/missing draws stop floating contacts.

308 local tests passed in 18 suites, including 79 Dual Wield tests.
Windows x64 release cross-build and PE exports/imports passed. New native
menu/offer anchors match the supplied Steam executable. ZIP CRC and full
extraction hashes checked. Cumulative source patch and credits included.

The DLL has NOT been run inside KH1FM here. Actual ability-menu refresh,
style exclusivity in game, Final donor appearance/availability, casting
release sync, weapon geometry/rehits/impact feedback and map transitions
still need your fresh-process test. Keep the v8 ZIP to revert if needed.
