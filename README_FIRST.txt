KH1FM DUAL STYLES -- PROTOTYPE v13 (s352)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v12 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v13, then Build and Run.
   Panacea is required. F1 does not reload a native DLL.
3. Load your save and equip Style: Dual A or Style: Dual B.
   Dual A was Close; Dual B was Ranged. Their existing IDs, AP and
   equipped/learned states are preserved. Equipping one cancels the other.

Keep older offhand/integrated Lua, Synch/moveset routers, duplicate
Sora-model mods and the full KH2 Combat overhaul disabled. KH1FM and
KH2FM must be in the same PC 1.5+2.5 installation; normal Sora is required.
Animation data comes from your own KH2FM files. No game assets ship.
Use the included OpenKH manifest; do not replace the shared dinput8.dll.

CHANGES IN v13

Style: Dual A -- formerly Style: Dual Close
- Retains Valor combat, rising Guard action and existing visual routes.
- Retains the v12 live-hand refresh during native Glide/Superglide.
  Both glides hold the blades and remain cosmetic.

Style: Dual B -- formerly Style: Dual Ranged
- Basic Attack now uses Final Form's actual base attack selector and
  body/weapon animations on ground and in the air, like Dual A's Valor
  adapter. The standard string has three slots and an ending finisher.
- Combo Plus and Air Combo Plus extend their respective strings. Valid
  presses count through whiffs without granting Combo Master. Donor
  combo windows control chaining; the old last-quarter spin window is
  no longer the basic-attack timing.
- The old idle-body override and aerial height hold are removed from
  basic Attack. Final's authored melee movement/timing now apply.
- Guard performs ONE cycle of the former basic Keyblade spin, with Sora
  in Final's looping idle pose. There is no Aero spell, projectile,
  barrier, spell effect or MP cost, and no automatic combo follow-up.
- Dodge Roll is replaced by Master Form's aerial dodge: a ground-started
  hop using motion 202 and Master's base movement parameters. It ends
  normally and hands remaining air movement back to KH1.
- Guard and Dodge Roll must still be equipped to use their replacements.
  Native tilt decides Guard versus Dodge Roll when both are equipped.
  No new airborne dodge input or extra ability is granted.
- Master is loaded as data only for this dodge. No Master casting,
  script, spell or effect archive is enabled.

NATIVE ATTACK ABILITIES
Both styles give equipped KH1 attack abilities priority for the ENTIRE
affected combo lane, retaining their native timing/selection and a visual
offhand. For a clean Final base-combo test, disable ground action attacks
(Vortex, Counterattack, Blitz, Slapshot, Sliding Dash, Ripple Drive,
Stun Impact, Gravity Break, Zantetsuken) and aerial action attacks
(Aerial Sweep, Hurricane Blast). Combo Plus/Air Combo Plus alone do not
force a native lane. Dual B physical limits remain blocked.

RETAINED
Both styles duplicate the currently equipped KH1 weapon, with no second
weapon selection or inventory copy. Unequipping the active style restores
normal KH1 behavior and removes the duplicate. No Drive gauge, timer,
drain, transformation, costume/recolour, bonus stats/AP or extra native
ability is added. Your existing INI is preserved.

Dual A keeps native KH1 casting. Dual B keeps Final native-spell overlays,
the regular-Glide floor hover and its prior Superglide behavior. To test
regular Glide, unequip Superglide, which normally has native priority.
Actual KH1 spells keep native MP, levels, projectiles/effects and damage.
The v10 Fire observer fix remains. Blade contacts use the actual displayed
equipped-weapon geometry and the existing native hit/impact/audio path.

FIRST TEST
1. Check the renamed entries and automatic mutual exclusion.
2. Dual B: disable action-attack abilities as above. Attack in empty
   space through a three-slot ground combo, then near a single enemy.
   Repeat in the air. Check Final's actual body/weapon animations.
3. Add Combo Plus/Air Combo Plus and confirm the appropriate extra slot.
   Re-enable native attack abilities and check their priority.
4. Equip Guard. With neutral stick, Guard should play one idle-body
   blade spin without Aero effects or MP loss, then stop.
5. Equip Dodge Roll. With directional input, Dodge Roll should launch
   Master's aerial dodge instead of KH1's roll. Check landing, incoming
   damage, collision, turning, magic/item interruptions and map changes.
6. Switch to Dual A and check Valor attacks, rising Guard and held
   Glide/Superglide. Switch weapons/styles and confirm stale poses vanish.
Exclude party damage when attributing enemy HP loss.

SETTINGS -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
kh1-dual-wield.ini:
  idle_speed = 0.75
Combat/supported scene-idle speed, including Dual B Guard's idle body.
1.0 is authored idle speed; accepted range .10..2.00. Restart after edits.
  offhand_only_test = off
Use off to test both blades. Existing on isolates left imported contacts
from attacks/Guard/floating blades; native spells/items/party stay native.
  remove_dual_wield = off
Uninstall only: set on, launch/load/save with v13, close, disable the mod
and Build again. It removes only both custom style entries.

LOG / FEEDBACK
kh1-dual-wield.log is beside the executable and INI. Look for s352,
PROTOTYPE v13, DUAL B ACTION DATA, DUAL B ACTION, DUAL B GUARD SPIN
REQUEST and DUAL B MASTER DODGE START. ACTION DATA reports the actual
admitted donor rows and whether Guard/dodge data is ready. Missing dodge
data retains native Dodge Roll. Return this NEW log and a short recording
if an action fails, has poor timing or misses visible contact.

VALIDATION
327 local tests passed across 18 suites, including 98 Dual Wield tests.
New tests use synthetic donors for Final ground/air combos and modifiers,
one-shot Guard, filtering/root retention, native Guard/Roll selection,
damage classification and Master launch/end with no ability grants.
Windows x64 release cross-build and PE imports/exports passed. No new
native hook/address; the existing Steam anchor receipt is retained.
ZIP CRC, extraction and all-entry hashes checked. Source patch, original
credits and licenses included. No game execution or installed Final/Master
donor validation was performed here; confirm behavior in a fresh game run.
Keep v12 if you need to revert.
