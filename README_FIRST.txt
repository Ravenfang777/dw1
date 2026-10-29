KH1FM DUAL WIELD -- GROUND PROTOTYPE v1

This is one OpenKH mod, with a native DLL that reads KH2's motion data from
your own installed KH2 Final Mix. It replaces the earlier Lua test for this
run. It does not require the full KH2 Combat for KH1 mod to be enabled.

WHAT THIS FIRST TEST DOES
- Adds exactly one ability: Dual Wield, zero AP, initially UNEQUIPPED.
- Equipped: draws a copy of Sora's currently equipped KH1 weapon in his left
  hand and uses KH2 Valor's basic ground combo. No second weapon selection.
- Unequipped: hides the duplicate and gives ground attacks back to KH1.
- A weapon change loads the new equipped weapon's own model and effects.
- Sora retains his normal model, textures and colours.
- No Drive gauge, timer, drain, transformation, partner removal, extra
  abilities, AP/stat boosts, camera, HUD or shortcut changes.

INSTALL -- FRESH PROCESS, ONLY THIS WEAPON/MOVESET SYSTEM
1. Fully close KH1FM. Do not use F1 reload.
2. Disable the v22/older integrated offhand Lua, Synch and other moveset
   routers. Keep the original KH2 Combat for KH1 mod / kh1-kh2.dll disabled.
3. Disable the previous v6 offhand Sora model replacement in OpenKH for this
   test. This DLL draws its own weapon copy; the old embedded duplicate is
   not used. Restore the normal Sora model assets if those were copied into
   another mod manually. This package does not overwrite your model files.
4. In OpenKH Mods Manager (Kingdom Hearts Final Mix), install this ZIP with
   Mods > Install a New Mod > Select and install Mod Archive. Enable it,
   then Build and Run. Panacea is required, as for the reference mod.
5. Load your save, wait briefly, then open Sora's Abilities menu and equip
   Dual Wield (0 AP). Start with Kingdom Key, then test another weapon.

KH1FM and KH2FM must be installed in the same 1.5+2.5 game folder. The DLL
reads KH2's data there. No game assets are included in this package.

TEST
1. With Dual Wield off, check that Sora has his normal appearance and attacks.
2. Equip it and test a few ground swings/combos near one enemy. Both blades'
   ground contacts are enabled in this build. Include a few clear whiffs.
3. Change Sora's equipped weapon. The left-hand copy should change with it,
   without changing inventory counts or requiring another selection.
4. Unequip Dual Wield. The extra weapon should disappear and native ground
   attacks should return. Check that the other ability entries/states match.
5. Re-equip it, change maps and repeat a short test. Also check that aerial
   attacks and ground/aerial casting still use their normal KH1 animations.

The extra imported offhand contacts/trails are GROUND-ONLY in this prototype.
Native aerial attacks and magic keep KH1's existing contacts and effects.
Expansion of the imported moveset to aerial attacks comes after this test.

RETURN THE LOG
Send kh1-dual-wield.log from the game executable's folder, with matching
video. It records DUAL WIELD LEARNED, DUAL WIELD EQUIPPED and DUAL WIELD READY,
the selected weapon resource, loaded Valor rows, native hits and any failed
hook/data admission. It is separate from the old Lua log.

OPTIONAL CONTACT ISOLATION
The first launch creates kh1-dual-wield.ini beside the game executable.
After the initial moveset test, you may fully close the game and change:
  offhand_only_test = on
That permits only the left weapon's imported ground contacts. Native aerial
and spell contacts remain native. Set it back to off for both ground blades.
It is off by default so the initial full combo can connect normally.

ABILITY / SAVE DETAILS
Only Dual Wield is appended to an empty ability entry; it is not equipped
automatically. Nothing is evicted to make room. A full or non-contiguous
ability list is left untouched. Saving in-game can retain the new entry.
For removal: close the game, set remove_dual_wield = on in the generated INI,
start with this mod, load your save, save it, then close the game and disable
this mod / Build again. The removal option changes only Dual Wield entries.

VALIDATION AND LIMITS
239 local tests passed, including ten new Dual Wield policy/controller checks.
The Windows x64 DLL was cross-compiled and its required exports/imports were
checked. Tests cover preserving native ability records and states, bounded
insertion/removal, ground-row admission and separate weapon contact windows,
plus existing animation, retargeting, rig, controller and combat regressions.

This build has NOT run in KH1FM here. Optional tests needing local game data
did not exercise their real-data paths. Actual menu behavior, loaded Valor
rows, attachment, contact/feedback, transitions and performance need the
fresh-process game test. Weapon contact geometry originates in Valor's data;
different weapon lengths and unusual Sora models still need verification.

The source patch, build identity, hashes and test transcript are included for
review. Existing upstream credits/licences are retained. Do not enable the
older offhand system or the full combat overhaul alongside this prototype.
