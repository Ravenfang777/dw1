KH1FM DUAL WIELD -- PROTOTYPE v5 (s344)

Install this ZIP as one OpenKH mod, replacing v4. It reads Valor animation
data from your own KH2FM installation. No game assets are included.

CHANGES
- The duplicate can draw even when KH1 hides or stows the primary weapon.
  Default actions use a hold calibrated during the first held idle/walk/run,
  following the current native left hand independently of the primary's
  weapon bones. The native body/action is left intact on fallback routes.
- Equipped KH1 attack abilities take priority. Their entire affected ground
  or air combo uses KH1's original routing, timing, contacts and animations,
  so prerequisites, hit counters and finishers remain native. The second
  weapon on that native combo is VISUAL ONLY. This is not a per-swing hybrid.
- With those action abilities unequipped, that lane uses the existing Valor
  base combo and both imported blades' independent contacts as before.
  Combo Plus, Air Combo Plus and Combo Master alone still use Valor.
- Adds available Valor item-use/throw and common front/back, high/low,
  heavy and aerial damage reaction visuals over the corresponding native
  KH1 requests. KH1 still applies damage, item healing/quantity/targets,
  movement, effects, sounds, invulnerability, events and cancels.
- Adds available Valor LINK_IDLE for recognized scripted standing idles,
  and Valor's resolved field idle for recognized cutscene standing idles.
  Native local motion on unretargeted children, including facial bones,
  remains under the retargeted parent. Actor placement and scripts stay KH1.
- Keeps v4's movement visuals, v3's grip correction and existing trail /
  actor-identity guards. Default KH1 magic remains on the ground and in air.

ATTACK ABILITY PRIORITY
Ground lane stays native with any of these equipped:
  Vortex, Counterattack, Blitz, Slapshot, Sliding Dash, Ripple Drive,
  Stun Impact, Gravity Break, Zantetsuken.
Air lane stays native with either of these equipped:
  Aerial Sweep, Hurricane Blast.
Disabled/unequipped abilities do not select a native lane. A native selected
ability row is also allowed to run on its normal route. During an imported
air combo, KH1 is parked on its ground state; a placeholder ground row then
continues Valor air instead of starting a ground ability at height.
No abilities are added, renamed, switched on or removed by this routing.

ANIMATION SCOPE -- PLEASE READ
These are visual matches, not imported KH2 action controllers. New donors
must exist in Valor and the sampled native header must match its current
regular-bank request. Pending, missing, unknown or unsuitable data keeps
the current native KH1 animation. The log lists donor availability.

Interactions are currently LIMITED TO SUPPORTED STANDING IDLES. Chest
opening, lifting/carrying/throwing objects, pushing and the five Trinities
keep KH1 animations: no verified Valor donor is assigned to them here.
The cosmetic duplicate follows the native hand on these regular Sora routes.
Cutscene idle applies only where the active regular Sora actor actually uses
a recognized standing idle. Dedicated EVM/event poses, separate scripted
actors/copies, movie cinematics and unknown gestures remain native.
No blanket cutscene or interaction replacement is claimed.

Damage coverage is common light/heavy/aerial reactions, not every KO,
get-up, status or scripted damage pose. Those other poses remain native.
Items keep KH1's gameplay release events; normalized visual timing has not
been verified to align the hand-release gesture perfectly for every item.

THE PASSIVE ABILITY
Dual Wield: id 126, zero AP, initially unequipped. Duplicates the current KH1
weapon without a second selection or extra inventory copy. Unequipping
restores KH1 routing/poses and removes the duplicate. No Drive gauge,
timer, drain, transformation, costume/recolour, partner removal, stat/AP
bonus, camera/HUD/shortcut change or extra ability grant is installed.
Native fallback actions/combos have a cosmetic offhand: no extra offhand
damage, impact or swing-trail window is added. Imported Valor combos retain
their existing per-hand contacts and trails. Swing trails need no enemy;
contact impact effects/sounds require a hit.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable v1/v2/v3/v4 in OpenKH and enable only v5. All versions use the
   same DLL destination. F1 cannot reload or replace this native DLL.
2. Keep older integrated/offhand Lua, Synch/moveset routers, the v6 embedded
   duplicate-model assets and the full KH2 Combat / kh1-kh2.dll mod disabled.
   If you manually copied the embedded duplicate into another mod, restore
   normal Sora model assets there.
3. OpenKH Mods Manager -> Kingdom Hearts Final Mix -> install this ZIP as
   a Mod Archive -> enable it -> Build and Run. Panacea is required.
4. Load your save, equip Dual Wield, and stand idle briefly for the held
   duplicate calibration. Existing ability and INI entries are reused.

Normal Sora is required. KH1FM and KH2FM must be in the same PC 1.5+2.5
install folder. Do not rename/install this DLL as the shared dinput8.dll;
OpenKH/Panacea loads dll/kh1-dual-wield.dll through the mod manifest.

TEST
1. Equip a native attack ability, such as Slapshot. Compare its normal
   trigger with Dual Wield equipped/unequipped. Check native finishers too.
   The duplicate is cosmetic on the native ground/air combo lane.
2. Unequip native action abilities, then try Valor ground and aerial combos.
   Try a mixed loadout: a native ground ability with Valor air, and vice versa.
3. Cast ground/air magic, use a self/party-target item, take front/back hits,
   and check the duplicate during default actions and weapon stowing.
4. Talk, open a chest, carry/push an object and try a short scene. Known idle
   donors may apply; the listed gestures stay native. Check face/hand poses.
5. Change maps and weapons, then unequip/re-equip Dual Wield. Check correct
   duplication, retirement of old trails/poses and restoration of KH1.

LOG
kh1-dual-wield.log is beside KINGDOM HEARTS FINAL MIX.exe / the INI.
Your supplied earlier log identifies:
  C:\Steam\steamapps\common\KINGDOM HEARTS -HD 1.5+2.5 ReMIX-\
Look for s344 / PROTOTYPE v5, DUAL WIELD COMBO ROUTES, DUAL WIELD NATIVE
ATTACK, DUAL WIELD VALOR VISUAL DATA and VALOR VISUAL ACTIVE.
ROUTES reports native or Valor for each lane; DATA lists every candidate
or native fallback; ACTIVE is the first accepted sample for that action.
Return this NEW log with a short matching recording for a bad transition.

OPTIONAL OFFHAND CONTACT ISOLATION
After fully closing KH1FM, in kh1-dual-wield.ini:
  offhand_only_test = on
This isolates LEFT IMPORTED VALOR MELEE ONLY. It does not block native
attack-ability combos, spells, items or other characters' damage.
Unequip the native action abilities for an imported offhand-only test.
Set the option back to off for both imported blades.

REMOVAL
Unequip Dual Wield for normal play. To remove its saved ability entry:
close the game, set remove_dual_wield = on in the INI, launch with v5,
load and save, close, disable this mod and Build again. Only that entry
is removed; every other ability/save entry is retained.

VALIDATION / LIMITS
272 local tests passed, including 43 Dual Wield policy/controller tests,
across 18 suites. Windows x64 release cross-build passed; expected exports
and system-library imports checked. ZIP CRC and every extracted file hash
checked. Source patch and original credits/licences included.

The DLL has NOT been run inside KH1FM here. There is no local KH2 install,
so optional real-game-data tests used their no-install paths. Actual donor
availability, appearance, release gestures, mixed ability loadouts, native
ability triggers, offhand visibility and map/scene changes require your
fresh-process game test. Keep the v4 ZIP if you need to revert.
