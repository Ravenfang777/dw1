KH1FM STYLES v71 / s410 - SHARED OVERDRIVE COLORS AND TYPE E TUNING

INSTALL
Close KH1. Disable v70 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v71, Build and launch with Panacea. Keep the existing
KH2FM resources/settings required by the other stances. Standalone Aqua/Terra
and full KH2 Combat DLLs remain disabled. Confirm s410 / STANCES v71 in
kh1-dual-wield.log. This native adapter targets the supplied Steam Global build.

OVERDRIVES
Power (formerly Strength) - Red #FF0000
Will - Blue #0000FF
Resistance - Yellow #FFFF00
Prowess - White #FFFFFF
Rage - Black #000000

All five use the SAME combined Valor + Wisdom + Anti body-effect set.
Master/Final effect archives are no longer required for Overdrives. Existing
KH2 resources still provide the three shared layers. Watch for OVERDRIVE
SHARED LAYER READY or unavailable in the log and OVERDRIVE COMBINED SET
when selected. No Overdrive stat boost is assigned. One free choice remains
independent of Stance; selecting its equipped row again turns it off.
Saved Strength selections become Power without a reset.

Effect poses now come from witnessed animation passes. Wrist/palm anchors
track actual native joints, and only Overdrive particles receive finite and
distance guards against room-spanning Rage streaks. Original stance/spell
textures stay intact. Black effects use alpha blending to remain visible.
Type M?'s idle aura is suspended while the Overdrive supplies its Anti layer;
attack-specific visuals remain. Live hand tracking and blending need testing.

TYPE E
Normal/High Jump launch-height factor1.5 versus1.25 in v70:20% higher, with
the original native gravity. Held Circle is preserved during takeoff/rise;
the ordinary Glide constructor remains suppressed and Superglide remains usable.
Ground combo2 is another15% slower than v70 (72.25% of the pre-v70 rate),
with its event clock following the animation and no new held recovery pause.
Cure318 ground/427 air, Circle dodge distance/lift/timing and other controls stay.

COLOR EDITING
See OVERDRIVES.txt. Optional colors use #RRGGBB keys in kh1-overdrive.ini;
restart after manual changes. Menu choices preserve custom colors/other keys.
This package does not overwrite the user's existing settings file.

RETAINED
F ground/air body-contact dashes, G reverse grip/two-pass contacts, all stance
and numbered preview mappings, menu/AP display and built-in abilities remain.
Both private animation headers are byte exact to v70. Previously requested
non-Sora ability removal remains; saving persists it and uninstall does not
reconstruct partner ability lists. Stand idle for safe stance body handoffs.

VALIDATION / LIVE CHECK
655 Rust tests/30 suites and171 final-PE checks pass (122 shared,49 E).
Windows x64 release, full source reconstruction, ZIP CRC and all file hashes
are verified. Source, build inputs and current/historical receipts are included.
No Windows/game/GPU session was run here. Cycle all five Overdrives through
native/imported stances and transitions, check both hands/Rage, switch/off
and confirm old particles retire. Compare E held jumps and ground2 to v70.
Cross-stance jump parity and final visual appearance are not measured here.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v71, close KH1,
disable the package and Build. Overdrives are inactive in removal mode; existing
native-entry restoration/capacity and numbered-flag rules remain.
