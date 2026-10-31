KH1FM FIVE STYLES -- PROTOTYPE v25 (s364)

INSTALL
1. Fully close KH1FM. Disable v24 and all older Dual Wield prototypes.
2. Import this ZIP into OpenKH, enable ONLY v25, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s364 / PROTOTYPE v25 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not a script. Keep the full KH2 Combat
overhaul, older offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied.

STANDARD GLIDE ONLY
This update addresses Dual A's disappearing/teleporting offhand during
regular Glide. The duplicate now follows the current rendered palm joint
instead of an unskinned helper or a reconstructed native root/local chain.
Its held calibration is local to the palm and current model/weapon binding.
If Glide is the first action after loading, a fallback calibrates from
verified skinned primary weapon/palm data. Stale and invalid samples are
rejected. Only the standard-Glide duplicate ignores native weapon stow/fade;
Sora's body, primary draw state and Glide movement remain native.

SUPERGLIDE'S WORKING ATTACK FINISHER IS PRESERVED. The new attachment path
explicitly excludes native Superglide's subtype and every owned action.
The finisher start/controller and donor attack logic match v24 exactly.
No attack, damage, trail window or timing has been changed.

DUAL B IS PRESERVED. Your confirmed Quick Run/weapon appearance fix remains
as in v24, including the shared visibility for both blades. No changes to
its controller, donor rig, movement, Fire, Guard or spell effects.

FIRST TEST -- FRESH GAME PROCESS, NO ENEMIES NEEDED
1. Equip Style: Dual A and use STANDARD Glide straight, then turn left
   and right repeatedly. Check the offhand stays in his palm and visible.
2. Land, repeat and change map. Try gliding soon after loading as well.
3. Check that Superglide still performs the working Valor attack finisher.
4. Switch to Dual B and check its already-working Quick Run briefly.

If regular Glide still fails, send the FULL fresh kh1-dual-wield.log from
beside KINGDOM HEARTS FINAL MIX.exe, including startup, before restarting.
The new bounded notes begin DUAL A STANDARD GLIDE and report either the
palm calibration source or the exact rejected prerequisite. A recording
of the same Glide turn helps match the visual sample. The previously
supplied numbered (3) log is s362/v23; it is not a v24 or v25 test log.

RETAINED
Five exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed).
Only Dual styles duplicate the currently equipped weapon. Native attack
abilities retain their native combo lane. No second weapon selection,
Drive gauge/state, costume, stat bonus, extra ability or party removal.
Single B Run at .75 and KH2 Guard, Anti's weaponless movement/combat/aura
and magic/item/summon restrictions remain. Native ability gates remain.

Both B styles retain their KH2 Fire/Blizzard/Thunder/Cure effects at
native levels and the existing native visual filter. Gravity/Stop/Aero
retain native effects; Single A retains KH2 cast poses with KH1 effects.
Native KH1 damage/healing, levels, acceptance and costs are unchanged.
The working Fire recovery handoff is retained. KH2 multi-stage spell
combos are still not part of the native-cast overlay.

Your existing kh1-dual-wield.ini beside the EXE is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Offhand-only testing affects Dual weapon contacts, not spells or party.
To remove custom entries: set remove_dual_wield on; launch/load/save with
v25; close; disable the mod and Build again. Only the five entries are
removed. DLL/INI changes require a full restart.

VALIDATION
450 tests pass across 27 suites (148 style tests), including current-palm
turning fixtures, first-Glide calibration without helper matrices, subtype
and scene/binding rejection, and the retained real Win64 Guard bridge and
Quick Run lifecycle tests. Windows x64 release, PE interface, eight native
appearance anchors, seven model metadata checks and 102 scope/preservation
checks pass. ZIP CRC, extraction and saved-copy entry hashes are verified.

No live v25 game/GPU rendering test was performed. Offline checks do not
prove the visual symptom resolved; use the standard Glide checks above.
Source patch, pinned upstream, credits, licences and validation receipts
are included. No game executable, recording, extracted asset or
disassembly is distributed.
