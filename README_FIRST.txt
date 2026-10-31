KH1FM SIX STYLES -- PROTOTYPE v26 (s365)

INSTALL
1. Fully close KH1FM. Disable v25 and all older Dual Wield prototypes.
2. Import this ZIP into OpenKH, enable ONLY v26, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s365 / PROTOTYPE v26 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not Lua. Keep the full KH2 Combat
overhaul, older offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied.

DUAL A STANDARD GLIDE COLOR
Your recording shows the v25 offhand attachment is stable but pale. This
build keeps that palm attachment and removes the private forced-white
weapon color. The duplicate copies the current primary's native draw
colors. If the native draw omits its weapon, it uses only this binding's
previously visible held weapon color plus current body lighting. No
constant white palette or previous map/model/weapon colors are reused.
The visual result still requires your fresh in-game test.

A'S WORKING SUPERGLIDE ATTACK FINISHER AND B'S FIX ARE PRESERVED.
No change to the actual A finisher start, donor attack, movement or
contacts. B keeps its working Quick Run, both weapon models, Guard and
Fire recovery. The shared attack controller adds only C's donor choice.

NEW: STYLE: DUAL C (0 AP, initially disabled)
Uses the PLAYABLE dual-wield Roxas profile from KH2's prologue: object
803/P_EX110_BTLF. Its real installed object entry supplies the motion
filename and moveset id, including both weapon motion tracks.

- Authored base ground/air combos, with both blades' real hit windows.
- Matching idle, walk/run, jump/fall/landing, item, damage, ledge and
  interaction poses where that Roxas motion bank has them.
- Missing visual slots, magic, Guard and Dodge Roll retain KH1 behavior.
- Native KH1 Glide/Superglide with held blades; no special C glide attack.
- Current equipped weapon duplicated. No fixed Oathkeeper/Oblivion models.
- Normal KH1 Sora model. No costume, Drive state/gauge, stats or extra
  ability grant. No boss Roxas AI, reaction command or spell package.
- Native KH1 attack abilities keep their existing combo lane. Native
  Combo Plus/Air Combo Plus modifiers carry into the imported base combo.

C is exclusive with all other custom styles. Equipping any one disables
the other five; unequipping returns native behavior and removes the
extra blade. Existing styles keep their IDs and save entries.

FRESH-PROCESS TEST
1. A: regular Glide straight and turning; compare offhand color to the
   primary, then check its already-working Superglide attack finisher.
2. B: briefly check its already-working Quick Run with both blades.
3. C: check idle/run, ground and air combos on one enemy, then magic,
   items, normal ability attacks and map changes. Unequip C and switch
   to another style to check exclusivity and normal restoration.

Look for DUAL C DONOR LOADED and DUAL C DATA with attack_adapter=true in
kh1-dual-wield.log beside KINGDOM HEARTS FINAL MIX.exe. The loader validates
its actual body/weapon rig. If its assets/layout are missing or rejected,
it logs DUAL C DONOR UNAVAILABLE and retains native action behavior.
It never substitutes Valor's combos and calls them Roxas.

If C is rejected or anything still looks wrong, return the FULL fresh
log including startup, before restarting. Glide diagnostics now begin
HELD GLIDE DRAW and HELD GLIDE COLORS. A short recording helps match it.

RETAINED
Six exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed),
Dual C 121 (playable dual Roxas). Only A/B/C duplicate the equipped weapon.
Single B Run at .75 and KH2 Guard, Anti's weaponless movement/combat/aura
and magic/item/summon restrictions remain. No party removal.

Both B styles retain existing KH2 Fire/Blizzard/Thunder/Cure effects at
native levels and the native visual filter. Gravity/Stop/Aero retain
native effects; Single A retains KH2 cast poses with KH1 effects.
C uses native KH1 spells and costs. Native damage/healing and levels
remain. KH2 multi-stage spell combos are not added in this build.

Your existing kh1-dual-wield.ini is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Offhand-only testing affects Dual weapon contacts, not spells or party.
To remove custom entries: set remove_dual_wield on; launch/load/save with
v26; close; disable the mod and Build again. Only the six custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
467 tests pass across 31 suites (151 style tests), including object-profile
resolution/rejection, C's two-weapon ground/air controller, six-way equip
and native-color/binding fixtures. Existing Fire, Quick Run, finisher
and actual Win64 Guard bridge tests remain. Windows x64 release, PE
interface, 11 native anchors, seven model metadata checks and 127 scope/
preservation checks pass. ZIP CRC/extraction and saved-copy entry hashes
are verified.

No live v26 game/GPU test or installed Roxas asset execution was performed
here. Offline fixtures do not prove that the installed bank is admitted,
that all C animations render correctly or that the pale color resolved.
Source patch, pinned upstream, credits, licences and validation receipts
are included. No game executable, recording, extracted asset or
disassembly is distributed.
