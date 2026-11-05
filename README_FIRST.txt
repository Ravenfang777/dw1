KH1FM STYLES v75 / s414 - KH2 WEAPON EFFECT PREVIEWS

INSTALL
Close KH1. Disable v74 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v75, Build and launch with Panacea. Keep the existing
KH2FM installation/resources and settings. Restart after changing the DLL.
Confirm s414 / STANCES v75 in kh1-dual-wield.log. Target: supplied Steam Global.

USE
Customize -> Passives. Slots66..104 now select39 individual KH2 weapon-effect
elements, replacing the Ventus and Dark Riku animation previews. Numeric names
and AP0 remain. Each description shows its effect name, source package family
and element number, with runtime readiness. Full paths/IDs are also listed in
WEAPON_EFFECT_TESTS.csv and WEAPON_EFFECT_TESTS.txt.

Equip one preview and return to the field. It repeats every three seconds at
normal game speed. Short flashes finish naturally; looping effects have a
finite two-second window and one-second clear gap. Choose another slot to
replace it, or select the active slot again to turn it off. Walk and attack to
check attachment. The preview changes no moveset and keeps the equipped stance.

Old animation-test selections reset on upgrade, preventing unexpected effects.
Reserved105..114/127 flags remain. Selection uses the existing mod-wide settings
file, with weapon_effects=kh2-v1; no native ability/save/AP slots are consumed.

WHAT TO EXPECT
Kingdom Key flash; Limit Form glows/ribbon/catch/charge and Sonic Rave effects;
Valor finisher bursts; Final weapon bursts/first swings; base Sora attack effects.
One PAX element plays per slot, rather than an attack's entire combined effect.
Original colors are retained. Effects are visual only; no attack, script,
damage, sound or resource behavior is added. Overdrives remain independent.
Only KH2 is included in this iteration.

Descriptions report loading, partial rendering/skipped programs, missing KH2
archive/element, unavailable particle data or a retired geometry budget.
Ready means parsed/admitted, not a verified full original visual. Limit36 has
known unsupported lightning programs. Missing assets are not substituted.
Weapon codes use the current primary blade, including left-only source codes.
Other authored body/object anchors remain. A ribbon preview does not throw the
Keyblade. Exact blade fit/scale and original effect appearance need game tests.

RETAINED
All main stances including Type G and Type D, intrinsic passives, native AP,
movement/damage/contact rules, nine Overdrives/palette3/Drain/help metadata,
Customize/Appearance and muted footsteps. Both generated headers remain exact.
No planned Overdrive buffs or Drain deduction mechanics are implemented.

VALIDATION
665 Rust checks/30 nonempty suites pass, plus9 focused final-PE C/menu checks.
The PE checks cover39 descriptions, all12 stance coexistence paths, exclusive
selection, full-capacity zero-AP lists and readiness/footer bounds. They run
the actual C adapter/menu against the supplied Steam EXE with Win64 ABI mocks.
Rust particle dispatch/GPU and KH2 payload availability are not executed there.
Windows x64 release, exports/imports, source reconstruction, ZIP CRC and file
hashes are verified. No actual Windows/game/GPU session was performed here.
Check each selected effect's appearance and transitions in game.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v75, close KH1,
disable the package and Build. Existing restoration/capacity rules remain.
The previously requested saved removal of partner abilities cannot be reversed
automatically; that existing behavior is unchanged.
