KH1FM DUAL WIELD -- PROTOTYPE v8 (s347)

Install this ZIP as one OpenKH mod, replacing v7. It reads animation data
from your own KH2FM installation. No game assets are included.

NEW IN v8
- While Dual Wield and native Guard are equipped, the selected Guard action
  becomes Valor's action-button attack: its rising double slash and hop.
  This is the actual loaded Valor row 11, not a guessed animation swap.
- The donor's own timing, launch, weapon-hit windows, impact feedback and
  per-hand attack trails use the existing imported melee controller.
  It is an attack; it has no defensive Guard window.
- Guard remains a requirement. No Guard, growth, action or other ability is
  granted, renamed or switched on by this replacement. Unequipping Dual
  Wield restores the normal KH1 Guard behavior.
- KH1's Guard versus Dodge Roll selection is preserved. With Dodge Roll
  equipped, moving Square still selects native Roll under KH1's threshold
  rule. If Guard alone is equipped, native Guard selection can work while
  moving, and becomes the Valor attack. Air Glide and spell shortcuts stay
  native. A missing/invalid donor keeps the native Guard route.
- This explicit Guard attack works even when an ordinary combo lane stays
  native due to equipped attack abilities. A native ability follow-up waits
  for the imported cancel window and selects from the proper native air
  state. Other combo-lane ability priority remains unchanged.
- Retains v7's Final Glide/Superglide with blade contacts and shared slowed
  Valor combat/scripted/cutscene idle. Default KH1 ground/air casting stays.

ADJUST IDLE SPEED
Fully close KH1FM. In kh1-dual-wield.ini beside the game executable, add
or edit this line (an existing INI is preserved):

  idle_speed = 0.75

0.75 = 75% of the donor's authored speed; 0.50 = half speed; 1.0 = authored
speed. Accepted finite range is 0.10..2.00; missing/invalid values use 0.75.
Restart KH1FM to read changes. This applies to the combat and supported
cutscene idle only. It does not change attack timing or glide speed.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable v1/v2/v3/v4/v5/v6/v7 and enable only v8 in OpenKH. All versions target
   the same DLL. F1 cannot reload or replace this native DLL.
2. Keep older integrated/offhand Lua, Synch/moveset routers, v8 embedded
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
1. Equip native Guard and Dual Wield, stand still and press the Guard button
   once. Check Valor's rising attack, launch, both blade contacts and trails,
   then the return to native falling/landing. Repeat while changing targets.
2. With Guard and Dodge Roll equipped, compare stationary Square (new attack)
   and moving Square (native Roll). Unequip Guard and verify no new attack is
   available; unequip Dual Wield and verify the normal KH1 Guard returns.
3. Equip a native combo ability, then try the new Guard attack and valid
   attack/magic follow-ups. Check proper native aerial actions and casting.
   Existing imported melee offhand isolation applies to this attack too.
4. Interrupt the attack, change maps/weapons and unequip/re-equip Dual Wield.
   Check that old trails and poses retire. Also check both Final glides and
   revisit the prior cutscene idle as regression checks.

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
Look for s347 / PROTOTYPE v8, DUAL WIELD GLIDE DONOR, DUAL WIELD VISUAL DATA,
DUAL WIELD GUARD DONOR READY, DUAL WIELD GUARD ATTACK REQUEST,
DUAL WIELD VISUAL ACTIVE, DUAL WIELD GLIDE CONTACT READY,
DUAL WIELD SCENE IDLE ROUTE and DUAL WIELD COMBO ROUTES. DATA lists donor
availability; ACTIVE reports the first accepted action sample and speed.
Return the NEW log with a matching short recording for a bad transition.

REMOVAL
Unequip Dual Wield for normal play. To remove its saved ability entry:
close the game, set remove_dual_wield = on in the INI, launch with v8,
load and save, close, disable this mod and Build again. Only that entry
is removed; every other ability/save entry is retained.

VALIDATION / LIMITS
296 local tests passed, including 67 Dual Wield tests, across 18 suites.
Windows x64 release cross-build passed; PE exports/imports checked.
ZIP CRC and all extracted file hashes checked. Source patch and original
credits/licences are included.

The DLL has NOT been run inside KH1FM here. No local KH2 install is present,
so optional real-game-data tests used their no-install paths. Actual donor
availability/appearance, Guard input/launch/cancels and restoration, the
specific cutscene, menu-pause timing, glide
contact alignment/re-hit behavior, guard response, impact sound/effects,
map/scene transitions and native action triggers need your fresh-process
game test. Keep the v7 ZIP to revert if needed.
