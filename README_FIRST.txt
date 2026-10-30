KH1FM DUAL STYLES -- PROTOTYPE v15 (s354)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v14 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v15, then Build and Run.
   Panacea is required. F1 does not reload a native DLL.
3. Equip Style: Dual A or Style: Dual B. IDs 126/125, AP, existing
   learned/equipped state and mutual exclusion are preserved.

Keep older integrated/offhand Lua, Synch/moveset routers, duplicate
Sora-model mods and the full KH2 Combat overhaul disabled. Normal Sora
and KH1FM/KH2FM in the same PC 1.5+2.5 installation are required.
Use the included manifest; do not replace the shared dinput8.dll.
All KH2 animations/effects are read from your own install. No game assets ship.

WHAT CHANGED

DUAL A -- REAL FINISHER IN PLACE OF SUPERGLIDE
- The native Superglide start proves the ability/input is allowed.
  Instead of continuing glide movement, it exits that native state
  and starts the actual Valor base aerial finisher attack.
- The real row keeps its authored root/hop movement and per-blade
  contact timing. It can hit enemies and produce native impact/audio.
- No native glide speed is inherited. This is not v14's looping pose.
- One activation plays one finisher. Release Square and press again
  to rearm; holding alone does not make an endless attack loop.
- The action ends into native falling/landing at the resulting position.
  Regular Glide is unchanged. No new ability or Combo Master is granted.
- Missing donor data leaves the native held Superglide fallback.

DUAL B -- NATIVE DODGE ROLL REPLACEMENT
- Intercepts the actual committed native Dodge Roll start before its
  roll motion/flags/voice. The native selector still proves the earned
  ability, directional input and Guard-versus-Roll decision.
- Performs one moving Final idle-body/Keyblade spin, with the same
  blade contacts as Guard. Use the stick to move/steer during its cycle.
- If Final has no valid standalone movement speeds, use the loaded
  base Sora movement data. If its casting clip has no melee triggers,
  use actual ability-free base-attack metadata for each missing blade.
- Guard remains the stationary version. Both omit the extra attack
  voice, retaining weapon/trail and native hit sounds. No invulnerability,
  Master dodge, spell/MP cost or extra ability is added.
- Native Roll is retained only if its hook/data/model cannot be admitted;
  a specific admission-failure log now explains that fallback.

DUAL B -- ACTUAL KH2 SPELL EFFECTS
- Adds the real MAG/BDX/PAX effect resources for Fire, Blizzard, Thunder
  and Cure, at their actual native levels, using Final's magic subs.
- This is a separate effect renderer. It goes beyond casting animations.
  Wait for DUAL B KH2 SPELL EFFECTS READY before the first test.
- Native KH1 still handles MP, healing, damage, status, projectiles and
  collision. KH2 visual-script attacks/heals are ignored completely.
- IMPORTANT: native spell effects remain visible in this first effect
  test. You may see both native and KH2 visuals. This build adds genuine
  KH2 resources without replacing native spell behavior/effects.
- Gravity, Stop and Aero keep their native effects. Their existing Final
  casting overlays remain. All seven spells retain native levels/MP.
- A and unequipped styles keep native spells. New visuals retire on
  unequip, map/actor/weapon changes and scenes; menus/pauses hide/freeze.
- No Reflect, Drive, menu, gauge, stat or full-overhaul spell hooks are
  enabled. The earlier uninitialized spell-level lookup is not reused.
- Native spell audio remains. This test does not replace audio with KH2 audio.

FIRST TEST
1. A: equip Superglide, jump/fall and activate it in empty space. Sora
   should execute ONE actual Valor finisher and then fall, rather than
   keeping Superglide movement. Release/repress to repeat. Test one enemy
   for real blade contact and landing. Regular Glide should stay normal.
2. B: equip Dodge Roll. With directional input, activate it and look for
   DUAL B NATIVE ROLL REPLACED and DUAL B MOVING SPIN REQUEST. It should
   move with the spinning blades and stop after one cycle. Guard should
   still spin in place, without the added vocal line.
3. Wait for SPELL EFFECTS READY. Cast Fire, Blizzard, Thunder and Cure
   on the ground, then in the air. Look for DUAL B REAL KH2 SPELL FX.
   Confirm visible KH2 effects and unchanged native MP/healing/damage.
   Existing native effects may overlap; do not count them as added damage.
4. Check weapon/style changes, native damage interruption, map transitions,
   pause/menus and unequipping. Exclude party damage when attributing hits.

RETAINED
Both styles duplicate the currently equipped KH1 weapon with no second
selection/inventory copy. Equipping one cancels the other. Unequipping
removes the duplicate/restores native behavior. No Drive gauge, drain,
timer, transformation, costume, bonus stats/AP or extra ability is added.
A retains Valor combat; B retains Final's three-slot base ground/air
combos plus Combo Plus/Air Combo Plus. Native attack-ability lane priority
still applies to ordinary combos. B's regular-Glide floor hover and prior
Superglide remain. Guard and Dodge Roll still require their native abilities.

SETTINGS / LOG -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
Existing kh1-dual-wield.ini is preserved. Missing keys use defaults.
  dual_b_spell_fx = on
New setting, on by default: actual KH2 spell visual layer. Off disables
only the new effect renderer; actions and native spells stay enabled.
  idle_speed = 0.75
Combat/supported scene-idle rate, including B spin body tracks; .10..2.00.
  offhand_only_test = off
On isolates left imported contacts. Native spells/items/party remain.
  remove_dual_wield = off
Uninstall only: set on, launch/load/save with v15, close, disable mod,
then Build again. It removes only both custom style entries.
Restart the game after INI edits.

kh1-dual-wield.log: check s354 and PROTOTYPE v15. New markers:
  DUAL A SUPERGLIDE REPLACED / DUAL A REAL FINISHER START
  DUAL B NATIVE ROLL REPLACED / DUAL B ROLL ADMISSION FAILED
  DUAL B KH2 SPELL EFFECTS READY / DUAL B REAL KH2 SPELL FX
If Roll remains native or a new effect is absent, return this NEW log
with a short recording of one activation/cast. The log distinguishes
missing packages/data/hooks from an accepted action/effect script.

VALIDATION / LIMITS
404 local tests passed across 27 suites, including 103 Dual Wield tests
and the magic-script/effect/BDX suites. Tests cover real finisher root
movement/contacts/end, input/ability policy, spin movement and fallback,
cast/style/level routing and retained geometry/ownership behavior.
Windows x64 release cross-build and PE imports/exports passed. New hook
prologues/operands match the supplied Steam executable; runtime guards
retain native fallback on mismatch. Native FX scope/anchor receipts,
source patch, original credits and licenses are included. ZIP CRC,
extraction and all-entry hashes checked. No live game/GPU execution or
installed donor appearance validation here. Keep v14 if you need to revert.
