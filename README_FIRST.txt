KH1FM STYLES v76 / s415 - TRIANGLE OVERDRIVE ACTIVATION

INSTALL
Close KH1. Disable v75 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v76, Build and launch with Panacea. Keep the existing
KH2FM installation/resources/settings. Restart after changing the DLL.
Confirm s415 / STANCES v76 in kh1-dual-wield.log. Target: supplied Steam Global.

ACTIVATE
Choose one Overdrive in Customize -> Overdrives, then return to the field.
Selection now arms it; the aura stays off until transformation is complete.
When the native Triangle box above the command menu says Overdrive, tap
Triangle. All12 stances and base Sora use the full KH2 Drive transformation
animation52, once. Infinity Tip Charge and Counterguard Hand Flash play
centered on Sora, filtered to the selected Overdrive's configured color.
The aura turns on only after the final transformation pose is submitted.

Holding Triangle does not repeat it. Once complete, another fresh tap can play
one new sequence and re-enable that aura afterward. Selection persists; active
state is runtime only. Changing/re-equipping an Overdrive or loading a new actor
requires activation again. Same-owner stance changes retain a completed aura.

Talk/Open and other occupied native context prompts keep Triangle priority.
Return to normal Attack root before activating; not during submenus, L1 magic
shortcuts, attacks/casts, special air actions, events, pause or removal mode.
Native collision, gravity and damage remain live during the animation; field/
action interruption cancels it without granting an aura. No invincibility or
other planned Overdrive bonus/Drain deduction is implemented yet.

SOURCE EFFECTS
Infinity Tip Charge: obj/P_EX100_KH1F.a.us element20.
Counterguard Hand Flash: obj/P_EX100.a.us element41.
Each starts once, not in a repeated preview cycle. Short flashes expire;
remaining handles end with the transform. Both roots use Sora's body center,
not the Keyblade tip/hands. Existing preview/stance textures are not recolored.

The same KH2 resources used for existing styles/previews must be available.
OVERDRIVE ACTIVATION READY and ACTIVATION FX READY show admission; ACTIVATION
START, TRANSFORM POSE READY, ACTIVATION FX START and OVERDRIVE ACTIVE show the
sequence. Missing assets/conflicting reserved record prevent the prompt.
Existing particle interpreter limitations/skipped programs still apply.

RETAINED
All main stances and combat, intrinsic passives/native AP, nine Overdrives and
palette3 colors/Drain/help, Customize/Appearance, muted footsteps, and39 KH2
effect previews in Passives66..104. Both generated animation headers are exact
to v75. WEAPON_EFFECT_TESTS.csv/.txt remain the gallery guide. No KH1/BBS demos.

VALIDATION
674 Rust checks/30 nonempty suites and9 focused final-PE C/menu checks pass.
Nine new activation checks cover fresh/held input, final-pose gate, scope,
stance generations, prompt priority/conflicts, masks and interruptions.
Native adapter engine dependencies, rendering and package availability are
mocked; the PE harness executes the real C menu adapter using the Steam image.
Steam hook/name/getter anchors, Windows x64 release, exports/imports, source
reconstruction, bundle, ZIP CRC and file hashes are checked.
No actual Windows/game/GPU run was performed here. Please check the Triangle
box, full transform, center/scale/colors and delayed aura with base Sora and
your usual stances. source/STYLES-V76.MD records scope and remaining live checks.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v76, close KH1,
disable the package and Build. Existing restoration/capacity rules remain.
Previously requested saved partner-ability removal cannot be reversed
automatically; that existing behavior is unchanged.
