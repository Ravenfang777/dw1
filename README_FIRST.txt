KH1FM DUAL WIELD -- PROTOTYPE v6 (s345)

Install this ZIP as one OpenKH mod, replacing v5. It reads animation data
from your own KH2FM installation. No game assets are included.

NEW IN v6
- KH1 Glide uses Master Form's GLIDE animation.
- KH1 Superglide uses Final Form's GLIDE animation, including its sampled
  two-weapon placement. These are visual donors; movement remains KH1.
  The actual native glide subtype selects the donor, not merely having
  Superglide equipped. Existing Glide/Superglide ability requirements apply.
- Recognized cutscene standing idle now uses Valor's COMBAT idle, replacing
  the previous field idle. Dedicated scripted event animations stay native.
- Combat and supported cutscene idle loop continuously at 75% of authored
  speed by default. Their clock no longer squeezes the donor into KH1's
  shorter idle duration or stops when the native clip reaches its end.
- Glide/Superglide visuals also use continuous authored time. Repeated
  render passes do not advance the animation repeatedly. Native time
  scaling/zero steps apply. Action changes, rebinds and discontinuities
  retire old phases. Body and both weapon samples use the same donor time.
- Master/Final are loaded only as visual data. KH1 magic remains default
  on the ground and in the air. No Master/Final controller, donor scripts,
  glide hitboxes/trails, spell changes or Drive state are enabled.

ADJUST IDLE SPEED
Fully close KH1FM. In kh1-dual-wield.ini beside the game executable, add
or edit this line (an existing INI is preserved):

  idle_speed = 0.75

0.75 = 75% of the donor's authored speed; 0.50 = half speed; 1.0 = authored
speed. Accepted finite range is 0.10..2.00; missing/invalid values use 0.75.
Restart KH1FM to read changes. This applies to the combat and supported
cutscene idle only. It does not change attack timing or glide speed.
The reduction may look larger than 25% relative to v5, because v5 mapped
the whole donor into the shorter native clip instead of authored time.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable v1/v2/v3/v4/v5 and enable only v6 in OpenKH. All versions target
   the same DLL. F1 cannot reload or replace this native DLL.
2. Keep older integrated/offhand Lua, Synch/moveset routers, v6 embedded
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
1. Stand idle through several full cycles, both before and during battle.
   Try a regular standing-idle cutscene and check that it keeps looping.
2. Test native Glide and Superglide separately, with the required ability
   equipped. Check the body/weapon placement when starting, turning,
   falling, landing and resuming another action. Movement stays native.
3. Pause/resume, change maps and equipped weapons, and unequip/re-equip
   Dual Wield. Check that old poses/trails retire and native poses restore.
4. Confirm ground/air spells remain default and native attack abilities
   still trigger. Check the imported Valor combos with those abilities off.

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

Interactions are limited to recognized standing idles: LINK_IDLE remains
for scripted interaction idle; Valor combat idle is used for supported
regular cutscene idle. Chest opening, lifting/carrying/throwing objects,
pushing and the Trinities remain native. Dedicated EVM/event-bank poses,
separate scripted actors/copies, movie cinematics and unknown gestures
stay native. No blanket cutscene replacement is claimed.
Missing/invalid donor data leaves the current KH1 animation intact.

OPTIONAL OFFHAND CONTACT ISOLATION
After fully closing KH1FM, set in kh1-dual-wield.ini:
  offhand_only_test = on
This isolates LEFT IMPORTED VALOR MELEE ONLY. It does not block native
attack-ability combos, spells, items or other characters' damage.
Unequip native action abilities for imported offhand-only tests. Set off
again to restore both imported blades.

LOG
kh1-dual-wield.log is beside KINGDOM HEARTS FINAL MIX.exe and the INI.
The earlier supplied log identifies this installation folder:
  C:\Steam\steamapps\common\KINGDOM HEARTS -HD 1.5+2.5 ReMIX-\
Look for s345 / PROTOTYPE v6, DUAL WIELD GLIDE DONOR, DUAL WIELD VISUAL DATA,
DUAL WIELD VISUAL ACTIVE and DUAL WIELD COMBO ROUTES. DATA lists donor
availability; ACTIVE reports the first accepted action sample and speed.
Return the NEW log with a matching short recording for a bad transition.

REMOVAL
Unequip Dual Wield for normal play. To remove its saved ability entry:
close the game, set remove_dual_wield = on in the INI, launch with v6,
load and save, close, disable this mod and Build again. Only that entry
is removed; every other ability/save entry is retained.

VALIDATION / LIMITS
280 local tests passed, including 51 Dual Wield tests, across 18 suites.
Windows x64 release cross-build passed; PE exports/imports checked.
ZIP CRC and all extracted file hashes checked. Source patch and original
credits/licences are included.

The DLL has NOT been run inside KH1FM here. No local KH2 install is present,
so optional real-game-data tests used their no-install paths. Actual donor
availability/appearance, looping, menu-pause timing, glide weapon placement,
map/scene transitions and native action triggers need your fresh-process
game test. Keep the v5 ZIP to revert if needed.
