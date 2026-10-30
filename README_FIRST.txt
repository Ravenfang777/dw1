KH1FM DUAL WIELD -- PROTOTYPE v4 (s343)

This replaces v1/v2/v3. Install this ZIP as one OpenKH mod. It reads Valor
animation and combo data from your own KH2 Final Mix installation; no game
assets are included.

CHANGES IN v4
- Removes the Master casting override on both ground and air. Its observer,
  sampler and donor loading are removed. Existing KH1 magic keeps its default
  animation, effects, MP cost, damage, event timing, movement and cancels.
- Expands Valor's matching visuals from idle/run to walking, jumping/rising,
  falling, landing, ledge hanging/climbing, and glide when a donor exists.
  Existing base ground/aerial combos, grip correction and trails are retained.
- KH1 still performs movement and gates the actions. Drawing a matching pose
  does not grant High Jump, Glide, Dodge Roll, Guard or any other ability.
- Jump/rise pairs share one donor timeline, so switching from KH1 takeoff to
  rise does not restart Valor's jump. Fall loops; landing/climbing play once.
  Native clocks control playback, including pauses.
- Removes donor root travel from non-attack poses so KH1 alone moves Sora.
  Ledge poses use a bounded native hand midpoint; invalid/missing phase,
  donor or alignment data falls back to the current native pose.

ANIMATION MATCHES
  KH1 standing idle    -> Valor idle
  KH1 walk             -> Valor walk
  KH1 run              -> Valor run
  KH1 jump / rise      -> Valor jump, continued across the two native clips
  KH1 fall             -> Valor fall loop
  KH1 landing          -> Valor landing
  KH1 edge hang        -> Valor hang, if present
  KH1 edge climb       -> Valor climb, if present
  KH1 Glide/Superglide -> Valor's resolved glide clip, if present
  KH1 ground/air combo -> existing filtered base Valor combos
These are the verified action mappings in the source, not a blanket numeric
slot replacement. The readiness log lists each candidate and availability.
A resolved Valor clip can itself be shared with normal KH2 Sora. Missing
clips stay native. No spell, item, reaction or special is guessed from an
unrelated animation. Ladders, poles, bars, swimming and flight stay native.
Native movement speed, jump height, gravity, collisions, grabs, gameplay
windows and events are retained. The visual overlays run no donor contacts,
swing trails, spell scripts, particles, voices or footsteps.

VALOR AND MAGIC IN THE REFERENCE MOD
The pinned upstream source treats Valor as unable to cast: its
win/form.rs::Kind::magic_sub returns None for Valor, and its Drive docs
record magic being disabled. That restriction is not enabled for Dual Wield.
KH1 spells stay usable and use their normal KH1 ground/air animations.
No Master casting donor is loaded by this version.

THE ABILITY
Dual Wield is 0 AP, initially unequipped. Equipped: the current KH1 weapon
is duplicated into the left hand and the matching Valor profile is used.
No second weapon selection or inventory copy is required. Unequipped:
the duplicate disappears and KH1's normal moveset returns.
No Drive gauge, timer, drain, transformation, outfit/model recolour, partner
removal, other ability grants, AP/stat bonuses, camera or HUD changes.
Swing trails do not need an enemy; impact sounds/effects need a contact.
Both imported blades are enabled by default.

INSTALL / UPDATE -- FULLY CLOSE KH1FM FIRST
1. Disable earlier Dual Wield versions in OpenKH. Enable only v4; all
   versions use the same DLL destination. Do not use F1 to reload this DLL.
2. Keep older integrated/offhand Lua, Synch/moveset routers, the v6 embedded
   duplicate-model replacement, and the full KH2 Combat / kh1-kh2.dll mod
   disabled. Restore normal Sora model assets if the old duplicate was
   manually copied into another mod.
3. In OpenKH Mods Manager (Kingdom Hearts Final Mix), install this ZIP as
   a Mod Archive, enable it, then Build and Run. Panacea is required.
4. Load your save, wait briefly, then equip Dual Wield in Sora's Abilities.
   An existing Dual Wield entry is reused; another copy is not added.
   Existing INI settings are retained; no reset is needed.

KH1FM and KH2FM must be in the same PC 1.5+2.5 install folder. Normal Sora
is required for this prototype. Do not install the DLL as dinput8.dll in
the shared game folder; OpenKH/Panacea loads dll/kh1-dual-wield.dll.

QUICK TEST
1. With Dual Wield equipped, stand idle, turn, walk slowly and run. Check
   both weapon grips and absence of a continuously emitting ribbon.
2. Jump from a standstill and while moving. Hold/release jump, fall from
   a ledge, land, then repeat into a ground/aerial combo. Watch the switch
   from jump to rise, fall and landing for a restart, freeze or displacement.
3. Hang from and climb a normal ledge. If already learned, try Glide and
   Superglide. Check the log for donor availability and action admission.
4. Cast ground/aerial magic. Confirm normal KH1 casting, MP and effects.
   Try an item, take a hit and use any KH1-only special available in the save.
5. Change maps and weapons, then unequip/re-equip Dual Wield. Check that
   poses and trails retire, the copy follows the weapon, and KH1 restores.

LOG LOCATION
kh1-dual-wield.log is beside KINGDOM HEARTS FINAL MIX.exe and
kh1-dual-wield.ini, not in OpenKH's scripts folder.
Your supplied log identifies the folder as:
  C:\Steam\steamapps\common\KINGDOM HEARTS -HD 1.5+2.5 ReMIX-\
Return the new log with a short matching video if an action looks wrong.
Look for s343 / PROTOTYPE v4, DUAL WIELD READY,
DUAL WIELD VALOR VISUAL DATA and DUAL WIELD VALOR VISUAL ACTIVE.
The DATA line lists each donor or native fallback; ACTIVE reports the first
successful sample of each matched action. A missing hook or incomplete
required Valor combo data leaves the custom profile unavailable.

OPTIONAL OFFHAND CONTACT ISOLATION
After fully closing the game, set in kh1-dual-wield.ini:
  offhand_only_test = on
Only left imported ground/aerial melee contacts are then allowed. This
retains native spell damage and other characters' damage.
Set it back to off for both blades.

SAVE / REMOVAL
Only Dual Wield is appended to an empty ability entry, initially unequipped.
Existing entries are preserved. Saving can retain Dual Wield.
To remove it: close the game, set remove_dual_wield = on in the INI, launch
with v4, load and save, close, then disable this mod and Build again.
That option removes only Dual Wield entries.

VALIDATION AND LIMITS
260 local tests passed, including 31 Dual Wield policy/controller tests.
Coverage includes native action exclusions, both jump pairs across the rise
boundary, mixed clip rates, paused/one-shot clocks, bad metadata rejection,
root removal and bounded atomic ledge alignment. Existing ability/save,
contact, grip, placement and trail checks are retained.
The Windows x64 release cross-build and PE exports/imports passed checks.
The ZIP was fully extracted and its DLL hash checked before delivery.

This build has not been run inside KH1FM here. No local KH2 installation
was available: optional real-game-data tests did not exercise their data
paths. Actual donor availability, visible blends, hand placement, contacts,
ledge/glide transitions and map changes need your fresh game test.
The tests do not establish finalized HP loss or left-hand attribution.

Source patch, exact build identity, test transcript and original credits /
licences are included. Keep v3's ZIP if you need to revert.
