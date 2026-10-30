KH1FM DUAL STYLES -- PROTOTYPE v12 (s351)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v11 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v12, then Build and Run.
   Panacea is required. F1 does not reload a native DLL.
3. Load your save and equip Style: Dual Close or Style: Dual Ranged.
   Equipping one automatically unequips the other. Existing entries,
   AP and other abilities are preserved. No new ability is added by v12.

Keep older offhand/integrated Lua, Synch/moveset routers, duplicate
Sora-model mods and the full KH2 Combat overhaul disabled. KH1FM and
KH2FM must be in the same PC 1.5+2.5 installation; normal Sora is required.
Animation data is read from your own KH2FM files. No game assets ship.
Do not install the DLL as the shared dinput8.dll; use the included manifest.

CHANGES IN v12

Style: Dual Close -- held Glide/Superglide duplicate refresh
- Both glides retain KH1's native body/primary grip and a held offhand.
- The duplicate is rebuilt from the current native left hand at draw
  time, even if the static body animation did not rebuild that frame.
- Exact field-body draws keep the normal-body admission current too.
  Hidden/unused native weapon bones no longer reject a valid hand pose.
- This addresses the source paths that could let the duplicate expire
  and blink in v11. It retains actor/model/weapon/map and hand bounds.
- Both glides remain cosmetic: no passive glide damage or trail emitter.

Style: Dual Ranged -- Final idle body with spinning weapons
- Attack keeps Sora's model in Final Form's looping combat idle.
- Both weapons keep the existing ground Aero-family spin. Body and
  weapon animation tracks are sampled independently.
- Ground and aerial attacks use the SAME idle body and weapon spin.
  The aerial combo holds Sora at his current height while it runs.
- No Aero spell, barrier, projectile or donor spell effect is created;
  Attack spends no MP. Actual weapon contacts retain native hit feedback.
- Up to three spins make the basic combo. Valid Attack presses count
  even on whiffs; an enemy and Combo Master are not required to repeat.
- Ground Combo Plus extends the ground string; Air Combo Plus extends
  the aerial string. No Combo Master or other ability is granted.
- Press Attack again in the last quarter of a spin to continue. The
  final slot ends normally. Without another valid press, it finishes
  and stops. Holding alone does not force an endless animation loop.
- When the aerial combo ends, native falling resumes from the current
  height. Native damage/scenes/commands, unequip, map or weapon changes
  can interrupt it; this is not permanent flight or invulnerability.

RETAINED
Both styles duplicate the currently equipped KH1 weapon with no second
selection or inventory copy. They remain mutually exclusive. Unequipping
the active style restores normal KH1 behavior and removes the duplicate.
No Drive gauge, timer/drain, transformation, costume/recolour, partner
removal, bonus stats/AP or additional native ability is added.

Close keeps Valor ground/air combat, native attack-ability priority,
its rising Guard attack, slowed idle and default KH1 casting.

Ranged keeps the regular-Glide floor hover from v11 and its existing
Final non-melee visuals/native spell overlays. Superglide retains its
previous Ranged behavior. To test regular Glide, unequip Superglide:
KH1 normally selects Superglide when that ability is also equipped.
Ranged native Guard/Dodge Roll remain if equipped; physical limits and
native melee/counter rows remain blocked beneath the spinning adapter.

Actual KH1 spells still use native MP, levels, projectiles/effects and
damage with Final body/weapon casting visuals. Casting a spell does not
automatically start a spin. The v10 Fire crash-path fix remains.

FIRST TEST
1. Close: keep Glide running while moving and turning, then repeat with
   Superglide. Check that the duplicate stays held and does not blink.
2. Ranged: Attack once in empty space. Sora should keep Final's idle pose
   while the two weapons spin; there should be no Aero spell or MP loss.
3. Repeat Attack through three slots in empty space, then near one enemy.
   Check Combo Plus extends the ground string. Test both blade contacts.
4. Jump and start a three-spin combo while rising, then while falling.
   Sora should stay in idle at the starting height during the combo,
   use the same spin as on the ground, then resume falling. Test Air Combo Plus.
5. Check actual magic/items/Guard, style and weapon switching, and map
   transitions. Exclude party damage when attributing enemy HP loss.

SETTINGS -- EXISTING FILE PRESERVED
kh1-dual-wield.ini is beside KINGDOM HEARTS FINAL MIX.exe.
  idle_speed = 0.75
Controls combat/supported scene-idle speed, including the idle body during
Ranged attacks. The weapon spin retains its existing rate. 1.0 is the
original idle rate; accepted range .10..2.00. Restart after changing it.
  offhand_only_test = off
Use off to test both blades. Existing on still isolates left imported
attack/Guard/floating contacts; native spells/items/party damage remain.
  remove_dual_wield = off
Uninstall only: set on, launch/load/save with v12, close, then disable
the mod and Build again. It removes only both custom style entries.

LOG / FEEDBACK
kh1-dual-wield.log is beside the game executable and INI. Look for s351,
PROTOTYPE v12, DUAL RANGED IDLE SPIN DATA and DUAL RANGED IDLE SPIN.
The first Close glide draws log that the held attachment was refreshed.
If blinking or another problem remains, return the NEW log and a short
recording showing the transition. No new user log/recording was supplied
for the original v11 flicker; this fix is based on the identified code paths.

VALIDATION
321 local tests passed across 18 suites, including 92 Dual Wield tests.
They cover independent body/weapon tracks, finite combos with modifiers,
whiff counting without ability grants, held air height, native/default
whiff policy and cosmetic hand refresh through body-update gaps.
Windows x64 release cross-build and PE imports/exports passed. No new
native hook/address is introduced; the v11 Steam anchor receipt is retained.
ZIP CRC and full-extraction hashes verified. Cumulative source patch,
original credits and licenses included. This DLL has not been run in
KH1FM here; actual visual stability and contacts need a fresh game test.
Keep v11 to revert if needed.
