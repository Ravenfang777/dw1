KH1FM DUAL STYLES -- PROTOTYPE v11 (s350)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v10 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v11, then Build and Run.
   Panacea is required. F1 does not reload a native DLL.
3. Load your save and equip Style: Dual Close or Style: Dual Ranged.
   Equipping one automatically unequips the other. Existing entries,
   AP and other abilities are preserved. No new ability is added by v11.

Keep older offhand/integrated Lua, Synch/moveset routers, duplicate
Sora-model mods and the full KH2 Combat overhaul disabled. KH1FM and
KH2FM must be in the same PC 1.5+2.5 installation; normal Sora is required.
Animation data is read from your own KH2FM files. No game assets ship.
Do not install the DLL as the shared dinput8.dll; use the included manifest.

CHANGES IN v11

Style: Dual Close -- both glides hold the weapons
- Glide and Superglide use KH1's native body animation and primary grip.
- The duplicate follows the left hand, with the existing palm alignment.
- Both weapons remain visible. There is no floating/spinning glide
  animation, passive glide damage or glide swing-trail emitter in Close.
- Existing Valor attacks, native attack-ability priority, rising Guard
  attack, slowed idle and default KH1 casting remain.

Style: Dual Ranged -- regular Glide hovers near the floor
- Start regular Glide normally in the air, with Glide already equipped.
- It descends normally until just above the floor, then stays level
  while you keep holding the normal Glide button. Releasing ends Glide.
- This changes regular Glide only. Superglide keeps its prior behavior.
  To test regular Glide, unequip Superglide: KH1 normally selects the
  Superglide variant when that ability is also equipped.
- One native unit of clearance prevents an ordinary level-floor landing.
  Movement, turning, collisions and ability gates still belong to KH1.
  Damage, water, scenes, map exits and genuine terrain collisions can
  still interrupt it. This does not start Glide from the ground or fly up.

Style: Dual Ranged -- the basic combo repeats the Aero pose
- Attack is enabled again. Every ground combo slot uses the same Final
  body/two-Keyblade animation currently shown when casting Aero.
- Every air combo slot uses its aerial version. The final combo slot
  looks like the others, then ends normally; it is not an endless loop.
- The normal three-slot base, equipped Combo Plus/Air Combo Plus,
  Combo Master and actual-hit/whiff rules still control progression.
  A new Attack press in the last quarter of the pose can advance the
  combo. Without further input the current attack finishes and stops.
- This is a physical attack adapter, not an Aero cast. It spends no MP,
  creates no Aero barrier/projectile/spell effect, and runs no donor
  spell event. Sora and the two spinning equipped weapons are animated.
- Actual authored blade-hit windows use the displayed weapon length,
  native hurtparts and native impact/damage feedback. Body/spell hitboxes
  are excluded. Missing/stale poses cannot keep dealing damage.
- Native melee/attack-ability/counter rows cannot run underneath the
  adapter. Physical limits and their follow-ups remain disabled in Ranged.
- Native Guard/Dodge Roll remain if equipped. Ranged Guard does not
  become Close's rising attack. Casting a spell does not auto-start Attack.

RETAINED
Both styles duplicate the currently equipped KH1 weapon, with no second
weapon selection or inventory copy. They remain mutually exclusive.
Unequipping the active style restores KH1 behavior and removes the copy.
There is no Drive gauge, timer/drain, transformation, costume/recolour,
partner removal, bonus stats/AP, or additional native ability.

Ranged's other supported Final movement, damage/item and scene-idle
visuals remain. Floating passive contacts still require real per-weapon
hit windows; recognized scene idles cause no damage. Native KH1 spells
retain MP, levels, spell effects/projectiles and damage, with Final ground
and air model/weapon casting visuals. The v10 Fire crash-path fix remains.

FIRST TEST
1. Close: try Glide and Superglide near an enemy. Both weapons should
   stay in the hands and gliding alone should cause no damage.
2. Ranged: equip Glide and unequip Superglide. Hold regular Glide toward
   a flat floor, continue holding near the floor, then release. It should
   stay in Glide without descending into the floor, then exit on release.
3. Ranged: tap Attack once in empty space, then try a complete combo near
   one enemy. Check each slot repeats the Aero pose, the final slot ends,
   MP does not change, and no Aero spell effect appears. Repeat in air.
4. Check actual Fire/Aero casting, Guard/items, style and weapon switching,
   then change maps. Return to Close for an ordinary combat check.
   Exclude party damage when checking which blade caused an HP change.

SETTINGS -- EXISTING FILE PRESERVED
kh1-dual-wield.ini is beside KINGDOM HEARTS FINAL MIX.exe.
  idle_speed = 0.75
Controls combat/supported scene-idle speed; 1.0 is original. Range .10..2.00.
  offhand_only_test = off
Use off to test both blades. Existing on still isolates left imported
attack/Guard/floating contacts; native spells/items/party damage remain.
  remove_dual_wield = off
Uninstall only: set on, launch/load/save with v11, close, then disable
the mod and Build again. It removes only both custom style entries.
Restart the game after changing settings.

LOG / FEEDBACK
kh1-dual-wield.log is beside the game executable and INI. Look for s350,
PROTOTYPE v11, DUAL RANGED GLIDE HOVER READY and DUAL RANGED AERO ATTACK.
If the hover anchors do not match, it logs that native Glide was retained.
For a problem, return the NEW log and a short recording of the transition.

VALIDATION
316 local tests passed across 18 suites, including 87 Dual Wield tests.
Windows x64 release cross-build and PE imports/exports passed. New hook
instructions, subtype/height/input operands and callback registrations
match the supplied Steam executable. Runtime checks fail closed.
ZIP CRC and full-extraction hashes verified; cumulative source patch,
original credits and licenses included. This DLL has not been run in
KH1FM here; animation appearance, near-floor collision and live contacts
still need your fresh-process game test. Keep v10 to revert if needed.
