KH1FM DUAL WIELD -- PROTOTYPE v7 (s346)

Install this ZIP as one OpenKH mod, replacing v6. It reads animation data
from your own KH2FM installation. No game assets are included.

NEW IN v7
- Both native Glide and Superglide now use Final Form GLIDE. Master donor
  loading is removed. KH1 retains ability requirements, input and movement.
- Both spinning blades can hit enemies while gliding. Each uses the actual
  equipped KH1 weapon's sampled start-to-tip range at its displayed grip,
  filled with overlapping spheres and swept between fresh samples.
- Final's loaded glide weapon windows (ATKP 1281 right / 1282 left) supply
  power and repeat-hit intervals. Expected donor data is 100% power and
  one re-hit per blade/target every 30 native 60-Hz frames. The donor loop
  does not reset the cooldown. Both glides share one window lifetime.
- Native enemy hurtparts/contact processing handles damage, impact visuals,
  sound and reactions. No direct HP writes or broad body-centered damage
  sphere. No new glide swing trail, donor spell, voice or extra ability.
- Contacts run once after native physics, from a current displayed pose.
  Old/missing/invalid poses cannot hit. Native movement since the last draw
  is accounted for, with up to one frame of pose latency. Missing draws
  clear sweeps while preserving cooldowns; landing, another action, unequip
  or changed actor/map/weapon binding retires the session.
- Corrects the second standing-idle route: v6 still used LINK_IDLE 6 for
  regular scripted standing idles without the global event flag. Both that
  route and the event idle now use the SAME Valor combat IDLE 0, continuous
  clock and idle_speed as the slower gameplay idle. Unknown/dedicated event
  gestures remain native. New bounded scene-route logs identify any scene
  that does not reach the recognized standing-idle route.

ADJUST IDLE SPEED
Fully close KH1FM. In kh1-dual-wield.ini beside the game executable, add
or edit this line (an existing INI is preserved):

  idle_speed = 0.75

0.75 = 75% of the donor's authored speed; 0.50 = half speed; 1.0 = authored
speed. Accepted finite range is 0.10..2.00; missing/invalid values use 0.75.
Restart KH1FM to read changes. This applies to the combat and supported
cutscene idle only. It does not change attack timing or glide speed.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable v1/v2/v3/v4/v5/v6 and enable only v7 in OpenKH. All versions target
   the same DLL. F1 cannot reload or replace this native DLL.
2. Keep older integrated/offhand Lua, Synch/moveset routers, v7 embedded
   duplicate-model assets and the full KH2 Combat / kh1-kh2.dll mod disabled.
   If an old embedded duplicate was copied into another mod, restore its
   normal Sora model assets.
3. OpenKH Mods Manager -> Kingdom Hearts Final Mix -> install this ZIP as
   a Mod Archive -> enable it -> Build and Run. Panacea is required.
4. Load your save, equip Dual Wield, and stand idle briefly for the held
   duplicate calibration. Existing ability and INI entries are reused.

Normal Sora is required. KH1FM and KH2FM must be in the same PC 1.5+2.5
install folder. Do not install/rename this DLL as the shared dinput8.dll;
OpenKH/Panacea loads dll/kh1-dual-wield.dll from the mod manifest.

TEST THIS VERSION
1. Revisit the cutscene that used the wrong idle. Compare its regular
   standing idle with the slowed combat idle, through several loop cycles.
   If it is still different, return the new log and identify the scene;
   a dedicated event-bank pose may need a separate verified mapping.
2. With Dual Wield and native Glide equipped, brush an enemy with the blade
   tips while Sora stays clear. Test Superglide separately. Exclude party,
   spells and unrelated damage for attribution. Both blades can hit; holding
   contact should use the donor interval rather than damage every frame.
3. Pause/resume, leave glide, land, change maps/weapons and unequip/re-equip
   Dual Wield. Check that contacts stop immediately and old sweeps retire.
4. Check normal spells and native attack abilities. Optional offhand-only
   testing now isolates imported glide contacts too (see below).

RETAINED BEHAVIOR
Dual Wield is ability 126, zero AP, initially unequipped. It duplicates the
currently equipped KH1 weapon without another selection or inventory copy.
Unequipping restores KH1 routing/poses and removes the duplicate. No gauge,
drain, timer, transformation, costume/recolour, partner removal, stat/AP
bonus, camera/HUD/shortcut change or extra ability grant is installed.

Equipped native attack abilities keep their ENTIRE affected combo lane
under KH1, including native selection, prerequisites, timing and contacts.
  Ground: Vortex, Counterattack, Blitz, Slapshot, Sliding Dash, Ripple Drive,
          Stun Impact, Gravity Break, Zantetsuken.
  Air: Aerial Sweep, Hurricane Blast.
The duplicate is cosmetic on native combo lanes. Other lanes use existing
Valor base ground/aerial rows and per-hand contacts/trails. Combo Plus,
Air Combo Plus and Combo Master alone do not force a native lane.
Native fallback actions retain a cosmetic hand-following duplicate, even
when KH1 stows/hides the primary weapon, while the current actor pose is valid.
Swing trails require an imported attack window, not an enemy; impact
effects and sound require contact. Non-attack donors add no contact/trails.

Available Valor movement, item-use/throw and common front/back, high/low,
heavy and aerial damage reactions remain visual overlays. KH1 retains
controls, movement, damage, item quantity/targets, effects, sounds and events.
The new Glide/Superglide donor choice supersedes v5's Valor glide candidate.

Both recognized scripted and event standing idles now use Valor combat
IDLE 0 at idle_speed, including the previously separate LINK_IDLE route.
Chest opening, lifting/carrying/throwing objects, pushing and the Trinities
remain native. Dedicated EVM/event-bank poses, separate actors/copies,
movie cinematics and unknown gestures stay native. No blanket cutscene
replacement is claimed. Missing/invalid donor data stays native.

OPTIONAL OFFHAND CONTACT ISOLATION
After fully closing KH1FM, set in kh1-dual-wield.ini:
  offhand_only_test = on
This isolates LEFT IMPORTED MELEE, INCLUDING GLIDE CONTACTS. It does not block native
attack-ability combos, spells, items or other characters' damage.
Unequip native action abilities for imported offhand-only tests. Set off
again to restore both imported blades.

LOG
kh1-dual-wield.log is beside KINGDOM HEARTS FINAL MIX.exe and the INI.
The earlier supplied log identifies this installation folder:
  C:\Steam\steamapps\common\KINGDOM HEARTS -HD 1.5+2.5 ReMIX-\
Look for s346 / PROTOTYPE v7, DUAL WIELD GLIDE DONOR, DUAL WIELD VISUAL DATA,
DUAL WIELD VISUAL ACTIVE, DUAL WIELD GLIDE CONTACT READY,
DUAL WIELD SCENE IDLE ROUTE and DUAL WIELD COMBO ROUTES. DATA lists donor
availability; ACTIVE reports the first accepted action sample and speed.
Return the NEW log with a matching short recording for a bad transition.

REMOVAL
Unequip Dual Wield for normal play. To remove its saved ability entry:
close the game, set remove_dual_wield = on in the INI, launch with v7,
load and save, close, disable this mod and Build again. Only that entry
is removed; every other ability/save entry is retained.

VALIDATION / LIMITS
289 local tests passed, including 60 Dual Wield tests, across 18 suites.
Windows x64 release cross-build passed; PE exports/imports checked.
ZIP CRC and all extracted file hashes checked. Source patch and original
credits/licences are included.

The DLL has NOT been run inside KH1FM here. No local KH2 install is present,
so optional real-game-data tests used their no-install paths. Actual donor
availability/appearance, the specific cutscene, menu-pause timing, glide
contact alignment/re-hit behavior, guard response, impact sound/effects,
map/scene transitions and native action triggers need your fresh-process
game test. Keep the v6 ZIP to revert if needed.
