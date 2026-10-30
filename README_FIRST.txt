KH1FM DUAL WIELD -- PROTOTYPE v3 (s342)

This replaces v1/v2. Install this ZIP as one OpenKH mod. It reads animation
and combo data from your own KH2 Final Mix installation; no game assets
are included.

CHANGES IN v3
- Corrects the offhand grip calculation: attachment uses each current
  hand's local axes and the native right-hand grip calibration. Skeleton
  bind-position differences no longer shift the duplicate behind the palm.
  The actual weapon-relative motion is retained.
- Adds Valor's run animation over native KH1 running. Native speed, actor
  movement, input and footsteps remain in control. Slow walking stays KH1.
- Adds Master casting poses to existing ground and aerial KH1 spells.
  A pose starts only after a native spell motion request is observed.
  Native motion changes, interruptions, weapon/map changes and unequipping
  retire it. Repeated casts wait for the new native request to be consumed.
  Master root travel is removed from the visual pose; it cannot move the
  native actor. Master weapon movement may float during the casting pose.

CASTING POSE MAPPINGS
  KH1 Fire     -> Master Fire
  KH1 Blizzard -> Master Blizzard
  KH1 Thunder  -> Master Thunder
  KH1 Cure     -> Master Cure
  KH1 Gravity  -> Master Thunder
  KH1 Stop     -> Master Cure
  KH1 Aero     -> Master Cure
These apply to existing spell levels, on the ground and in the air.
Only the body/weapon poses are sampled. KH1 still executes the spell,
including MP costs, effects, damage, native release events, movement and
cancels. The donor pose follows the native animation clock, without running
KH2 attack/spell scripts. Exact visual release alignment needs a game test.
Missing or incomplete Master data falls back to native casting.

THE ABILITY
Dual Wield is 0 AP, initially unequipped. Equipped: the current KH1 weapon
is duplicated into the left hand, with Valor's base ground/aerial combos,
standing idle and run, plus the Master casting visuals above. No second
weapon selection or inventory copy is required. Unequipped: the duplicate
disappears and KH1's moveset returns.
No Drive gauge, timer, drain, transformation, outfit/model recolour, partner
removal, other ability grants, AP/stat bonuses, camera or HUD changes.
v2's per-hand attack windows, trail retirement and actor-bound placement
are retained. Swing trails do not need an enemy; impact sounds/effects
require an actual contact. Both imported blades are enabled by default.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable Dual Wield v1/v2 in OpenKH. Enable only v3; these versions use
   the same DLL destination. Do not use F1 to reload this native mod.
2. Keep older integrated/offhand Lua, Synch/moveset routers, the v6 embedded
   duplicate-model replacement, and the full KH2 Combat / kh1-kh2.dll mod
   disabled. Restore normal Sora model assets if the old duplicate was
   manually copied into another mod.
3. In OpenKH Mods Manager (Kingdom Hearts Final Mix), install this ZIP as
   a Mod Archive, enable it, then Build and Run. Panacea is required.
4. Load your save, wait briefly, then equip Dual Wield in Sora's Abilities.
   An existing Dual Wield entry is reused; another copy is not added.
   Existing v1/v2 INI settings are retained; no reset is needed.

KH1FM and KH2FM must be in the same PC 1.5+2.5 install folder. Normal Sora
is required for this prototype. Do not install the DLL as dinput8.dll in
the shared game folder; OpenKH/Panacea loads dll/kh1-dual-wield.dll.

QUICK TEST
1. Stand idle, turn and view both hands close up. Check the grip position.
   Run in several directions, then slow-walk and stop. Check for unwanted
   body displacement or a continuously emitting ribbon.
2. Swing on empty ground, then do ground and aerial combos near an enemy.
   Trails should follow swings even on whiffs; impacts require contacts.
3. Cast the seven KH1 spells on the ground and in the air, where KH1 allows
   them. Try repeated Fire casts and spell levels available in your save.
   Check the pose against the native release effect, MP cost and recovery.
4. Let an enemy interrupt a cast; land during an aerial cast. Then change
   maps and weapons, and unequip/re-equip Dual Wield. Check that stale poses
   and trails retire and that the duplicate follows the current weapon.

LOG LOCATION
kh1-dual-wield.log is beside KINGDOM HEARTS FINAL MIX.exe and
kh1-dual-wield.ini, not in OpenKH's scripts folder.
Your supplied log identifies the game folder as:
  C:\Steam\steamapps\common\KINGDOM HEARTS -HD 1.5+2.5 ReMIX-\
Return the new log with a matching short video if anything is misaligned.
Look for s342 and PROTOTYPE v3, DUAL WIELD READY, the DATA idle/run flags,
DUAL WIELD MASTER VISUAL DATA READY, DUAL WIELD PALM BASIS,
DUAL WIELD VALOR RUN ACTIVE and DUAL WIELD MASTER CAST.
Missing hooks or incomplete Valor data leave the custom profile unavailable.

OPTIONAL OFFHAND CONTACT ISOLATION
After fully closing the game, set in kh1-dual-wield.ini:
  offhand_only_test = on
Only left imported ground/aerial melee contacts are then allowed. This
does not suppress native spell damage or other characters' damage.
Set it back to off for both blades.

SAVE / REMOVAL
Only Dual Wield is appended to an empty ability entry, and is not equipped
automatically. No existing entry is evicted or changed. Saving can retain
it. To remove it: close the game, set remove_dual_wield = on in the INI,
launch with v3, load and save, close, then disable this mod and Build again.
That option removes only Dual Wield entries.

VALIDATION AND LIMITS
259 local tests passed, including 30 Dual Wield policy/controller tests.
The 12 new tests cover hand-local calibration, native run/cast clocks,
all seven spell mappings, repeated and interrupted casts, stale binding
rejection, root-travel removal and explicit floating-weapon admission.
The Windows x64 release cross-build and PE exports/imports passed checks.
The ZIP was fully extracted and its DLL hash checked before delivery.

This build has not been run inside KH1FM here. No local KH2 installation
was available: optional real-game-data tests did not exercise their data
paths. Palm placement, loaded donor data, pose/event visual alignment,
runtime rendering, contacts and map transitions need your fresh game test.
The tests do not establish finalized HP loss or left-hand attribution.

Source patch, exact build identity, test transcript and original credits /
licences are included. Keep v2's ZIP if you need to revert.
