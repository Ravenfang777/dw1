KH1FM STYLES v70 / s409 - BODY DASHES, TUNING AND OVERDRIVES

INSTALL
Close KH1. Disable v69 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v70, Build and launch with Panacea. Keep the existing
KH2FM resources/settings required by the other stances. Standalone Aqua/Terra
and full KH2 Combat DLLs remain disabled. Confirm s409 / STANCES v70 in
kh1-dual-wield.log. This native adapter targets the supplied Steam Global build.

TYPE F
Ground dash/Dodge Roll009 and air dash330 now hit through a swept body-sized
area around Sora instead of blade reach. The actual contact-update caller now
includes F, fixing v69's moving-but-not-hitting route. One successful native
contact per enemy per dash; normal enemy defenses remain. Air travel stays702
units/29.25 native ticks, locked facing, once per airtime and no magic shortcuts.

TYPE E
Ground combo2 animation plays15% slower. Ground Cure uses318, air Cure427.
The Circle dodge has15% less horizontal reach:464.1 vs546 units at full stick.
Its26-tick movement duration,29.25 lift and animation timing are retained.

OTHER AERIAL DODGES
A/C/L? Circle dodge visual plays15% slower than v69. Their movement speed,
distance and controller timing stay unchanged. K? no longer has aerial dodge.
The user did not specify the A/C/L? reduction amount;15% is used for this test.

OVERDRIVES
Customize is now Stance / Passives / Overdrives / Outfits. Overdrives replaces
Limits with five exclusive zero-AP rows. Select one, or confirm it again to
turn it off. It does not replace your Stance or consume an ability slot.
Strength = Valor effects; Will = Wisdom; Resistance = Master; Prowess = Final;
Rage = Anti darkness. These are visual only; no stat boosts are assigned.
Selection persists separately in kh1-overdrive.ini. Existing KH2 resources are
used; check OVERDRIVE EFFECTS READY/unavailable messages if a donor is missing.

RETAINED
G's reverse grip, body/action mapping, air travel and blade contacts remain.
Other stance assignments, working numbered Passives, white AP Used/max and
built-in abilities remain. Previously requested non-Sora ability removal remains;
saving persists it and uninstall does not reconstruct partner ability lists.

CHECK IN GAME
Check F ground and air dash damage against enemies, E Cure poses/GC2/dodge,
A/C/L? slower dodge visuals and K?'s ordinary air controls. Cycle every Overdrive
on F/G/E and imported stances, then switch/off and check that old particles stop.
Stand idle after a stance change for the safe body handoff.

650 Rust tests/30 suites and170 final-PE checks pass (122 shared,48 E).
Source, generated build inputs, hashes and validation are included. The actual
registered F/G callback is exercised with native mocks. Full source tree and
archive hashes are verified. See source/STYLES-V70.MD for exact limitations.
No Windows/game/GPU session was run here; actual HP damage and form-effect
appearance still need an in-game check.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v70, close KH1,
disable the package and Build. Overdrives are inactive in removal mode; existing
native-entry restoration/capacity and numbered-flag rules remain.
