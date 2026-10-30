KH1FM DUAL WIELD -- PROTOTYPE v2 (s341)

This replaces v1. It is one OpenKH mod with a native DLL that reads motion
and combo data from your own KH2 Final Mix installation. Keep only this
weapon/moveset system enabled for the test.

CHANGES IN v2
- Custom trails stop when their swing window closes, and retire on native
  control, magic, damage, unequip, weapon changes and map changes.
- The left emitter requires that attack tick's actual weapon pose. Old
  poses and emitters are discarded after a discontinuity or missing render.
- Only Sora's active model instance supplies/receives the custom field pose.
  Placement stays at his current actor position; old output bones cannot
  feed back into it. Native and imported weapon poses use one world snapshot.
- Adds Valor's standing battle idle, used over KH1's standing-idle slots.
- Adds Valor's base aerial combos, including each blade's own contacts and
  swing trails. Native jump/fall velocity seeds entry; native fall resumes
  at the current height when the combo ends.
- Ground/aerial casting keep KH1's normal animations, timing and effects.

THE ABILITY
Dual Wield remains 0 AP, initially unequipped. Equipped: the current KH1
weapon is duplicated into the left hand, with Valor's base ground/aerial
combos and standing idle. No second weapon selection or inventory copy is
required. Unequipped: the duplicate disappears and KH1's moveset returns.
No Drive gauge, timer, drain, transformation, outfit/model recolour, partner
removal, other ability grants, AP/stat bonuses, camera or HUD changes.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable Dual Wield v1 in OpenKH. Enable only v2; both packages use the
   same DLL destination. Do not use F1 to reload this native mod.
2. Keep older integrated/offhand Lua, Synch/moveset routers, the v6 embedded
   duplicate-model replacement, and the full KH2 Combat / kh1-kh2.dll mod
   disabled. Restore normal Sora model assets if the old duplicate was
   manually copied into another mod.
3. In OpenKH Mods Manager (Kingdom Hearts Final Mix), install this ZIP as
   a Mod Archive, enable it, then Build and Run. Panacea is required.
4. Load your save, wait briefly, then equip Dual Wield in Sora's Abilities.
   An entry already saved by v1 is reused; another copy is not added.

KH1FM and KH2FM must be in the same PC 1.5+2.5 install folder. No game
assets are included. Do not install this DLL as dinput8.dll in the shared
game folder; OpenKH/Panacea loads it as dll/kh1-dual-wield.dll.

QUICK TEST
1. Stand idle, walk and turn. Check the new idle, attached duplicate and
   absence of a continuously emitting ribbon.
2. Swing on empty ground, then do ground and aerial combos near an enemy.
   Trails should follow the swings even on whiffs. Impact sounds/effects
   should occur only on contacts. Both blades are enabled by default.
3. Stop attacking. Cast ground and aerial magic, and allow an enemy to hit
   Sora. Watch for lingering ribbons, a ground snap or a displaced model.
4. Change maps and repeat. Switch the equipped weapon; the left copy should
   follow it. Unequip/re-equip Dual Wield to check restoration.

RETURN kh1-dual-wield.log FROM THE GAME EXECUTABLE'S FOLDER
Include matching video. The native log is separate from the Lua console.
Look for the s341/v2 startup and DUAL WIELD READY. The DATA line reports
separate ground/aerial row counts and confirms the Valor idle is present.
Missing hooks or incomplete Valor data leave the custom profile unavailable.

OPTIONAL OFFHAND CONTACT ISOLATION
The generated kh1-dual-wield.ini remains beside the game executable.
After fully closing the game, set:
  offhand_only_test = on
Only the left weapon's imported ground/aerial contacts are then allowed.
This does not suppress native spell damage or other characters' damage.
Set it back to off for both blades. Existing v1 INI settings are retained;
no reset is needed for the new aerial and idle behavior.

SAVE / REMOVAL
Only Dual Wield is appended to an empty ability entry, and is not equipped
automatically. No existing entry is evicted or changed. Saving can retain
it. To remove it: close the game, set remove_dual_wield = on in the INI,
launch with v2, load and save, close, then disable this mod and Build again.
That option removes only Dual Wield entries.

VALIDATION AND LIMITS
247 local tests passed, including 18 Dual Wield policy/controller tests.
Coverage includes native ability preservation, ground/aerial row admission,
separate contact windows, the real Character controller's aerial entry/exit,
actor-anchored placement, rejected stale/menu/private-owner/room/weapon
poses and same-tick trail intent. The Windows x64 DLL cross-build and
exports/imports were checked; the final ZIP was fully extracted locally.

This build has not been run inside KH1FM here. No local KH2 install was
available: optional real-game-data tests did not exercise their data paths.
The runtime air handoff, actual native rendering/effect retirement, loaded
Valor rows, contacts, different weapon lengths and map transitions require
your fresh-process game test. The changes address confirmed code defects;
this package does not claim that every visual issue is already game-verified.

Source patch, exact build identity, test transcript and original credits /
licences are included. Keep v1's ZIP if you need to revert.
