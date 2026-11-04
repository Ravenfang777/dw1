KH1FM STYLES v57 / s396

INSTALL
1. Close KH1. Disable v56 (or any older main Styles/Dual Wield package).
   Keep standalone Terra/Aqua tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v57, Build, and launch
   with Panacea. Keep existing KH2FM resources/settings for older styles.
3. Confirm s396 / v57 in kh1-dual-wield.log beside the executable.

STYLES MENU
Styles now appears directly below Customize. Its windows use KH1's native
GREEN palette, including borders/shadows. Other screens retain their normal
palette. Names, saved style IDs, the AP-free Styles view and normal native
Abilities behavior are retained.

SINGLE F AIR DASH
The log confirms a landing reset followed by rejected animation admission.
V57 retains the verified native Superglide binding across uses and checks its
identity/layout instead of comparing playback/cache data with the unplayed file
on every tap. The source animation is never written by this adapter.
The finite movement timer runs for39 ticks at speed16 (distance624), even if
Sora's falling animation already has a running clock. Native collision remains.
Fresh airborne Square starts one dash. Landing alone rearms it. Releasing the
button, completion, damage or changing styles cannot grant another use midair.
Normal Glide remains usable. Native state/request changes still cancel a dash.

TEST / REPORT
Check that Styles is below Customize and green, then return to the party menu
and normal Abilities to check their usual colors/AP display.
For Single F: jump, tap Square, try another tap before landing, land, jump and
tap Square again. Repeat several times; try a tap later during a long fall too.
If the dash still fails, return the new kh1-dual-wield.log. Bounded messages now
identify start, native commit, first movement and end.

RETAINED SETUP
All other confirmed v55/v56 changes remain: short style names, Styles-only AP
removal, Anti items with combat idle,75% aerial-dodge visual rate in A/C/E and
Dual C/D, Single E's smoother second ground hit, existing combos/magic/Guard
and jump settings. Both generated animation payload headers are unchanged.

VALIDATION
627 Rust tests in30 nonempty suites and94 final-PE checks pass:47 F/menu and47 E.
The original native palette-selection block is executed for green and normal
fallback. Tests cover source-cache changes between dashes, inherited/looping
animation clocks, repeated landings, exact distance and native cursor IDs.
The delivered v56 DLL fails the two new dash reproduction cases.
Native rendering, Windows startup and final in-game behavior are not run here.
Source, rebuild inputs, incremental bundle, licenses and receipts are included.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Never run two versions of the Styles DLL together.
