KH1FM STYLES v72 / s411 - LIGHTER OVERDRIVES AND CUSTOMIZE MENU

INSTALL
Close KH1. Disable v71 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v72, Build and launch with Panacea. Keep existing
KH2FM resources/settings. Standalone Aqua/Terra and full KH2 Combat DLLs stay
disabled. Confirm s411 / STANCES v72 in kh1-dual-wield.log. The native adapter
targets the supplied Steam Global build. Restart to clear old cached headers.

OVERDRIVE EFFECTS
Keep Valor and Wisdom's wind effect. Remove Wisdom foot sparkles11/12 and
the shared Anti darkness layer from all five Overdrives. Each still uses
the same reduced effect set in its own color:
Power - red; Will - blue; Resistance - yellow; Brilliance - white; Rage - black.
Brilliance replaces Prowess without changing selection ID4 or the saved choice.
Existing prowess_color settings remain supported; brilliance_color is preferred.
Check OVERDRIVE SHARED LAYER READY: Wisdom body_elements=[100] in the log.
The ordinary Anti/Wisdom stance and attack effects remain independent.

CUSTOMIZE MENU
The red header stays Customize in every category and in Passives selection.
Category order: Stance / Passives / Overdrives / Appearance.
Appearance replaces Outfits and remains reserved for later customization.
Overdrives no longer shows AP Used/current/max. Every row now has two equal
native boxes: Drain and a centered5. This is display-only; no drain mechanic
or resource cost is assigned. Passives keeps its normal AP display and costs.

RETAINED
One free Overdrive at a time, independent of Stance. Confirm its active row
again to disable it. Menu selection changes preserve custom hex colors and
other config keys. See OVERDRIVES.txt. Existing settings are not overwritten.
v71 E jump/GC2 tuning, Cure/dodge controls, F ground/air body-contact dashes,
G reverse grip/two-pass contacts, all stance and numbered preview mappings,
built-in abilities, pose anchors and particle bounds remain.
Both private animation headers are byte exact to v71.
Previously requested non-Sora ability removal remains permanent when saved;
uninstall does not reconstruct partner lists. Stand idle for safe stance handoffs.

VALIDATION / LIVE CHECK
656 Rust tests/30 suites and171 final-PE checks pass (122 shared,49 E).
Header lookups are checked through Passives, Stance, Overdrives, Appearance
and Passives again. Tests verify ten matching Drain/5 panels, centered5 glyphs,
absent Overdrive AP Used and unchanged Passives AP. Windows x64 release,
full source reconstruction, ZIP CRC and file hashes are verified.
Source/build inputs and current/historical receipts are included.
No Windows/game/GPU session ran here. Check that Wisdom wind remains with no
foot sparkles or shared Anti darkness, the header stays Customize, and the
new labels/panels fit. Effect identification is based on the admitted Wisdom
element list; final appearance still needs your in-game check.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v72, close KH1,
disable the package and Build. Existing restoration/capacity rules remain.
