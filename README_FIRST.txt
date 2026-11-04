KH1FM STYLES v65 / s404 - EXCLUSIVE VENTUS ANIMATION TESTS

INSTALL
1. Close KH1. Disable v64 or any older main Styles/Dual Wield package.
   Keep standalone Aqua/Terra tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v65, Build and launch
   with Panacea. Keep existing KH2FM resources/settings for older stances.
3. Confirm s404 / STANCES v65 in kh1-dual-wield.log beside the executable.
   The native UI/body adapter targets the supplied Steam Global build.

ANIMATION TESTS: CUSTOMIZE -> PASSIVES -> 66..100
All187 distinct unused Ventus clips are available across35 numbered tests.
Each passive replaces three ground hits and three air hits and costs0 AP.
The alternate native second ground hit shares the listed second animation.

Equipping a test UNEQUIPS ALL STANCES and the previously selected test.
Equipping ANY STANCE clears the animation test. Only one test can be active.
Normal passives remain available with their normal AP behavior.
Selecting the current test again disables it; no stance is auto-equipped.
After closing the menu, stand idle for the body data to switch safely.

VENTUS_TESTS.txt lists the ground/air set for every numbered test.
VENTUS_TESTS.csv adds source frames/ranges, native durations/slots/requests
and duplicate source archive aliases. VENTUS_ANIMATIONS.csv remains the
main Type G mapping. Numeric animations are source labels, not move names.

Some complex clips are split into labeled inclusive frame ranges across
several test hits. Every source frame is covered; shared boundary frames
keep the ranges continuous. Exact duplicate archive copies are shown once.
Tests retain KH1 hitboxes, events, action rules, combo timing and movement.
These are visual previews, not full BBS commands or guaranteed suitable moves.

TYPE G REVERSE KEYBLADE
Main Type G and its numbered tests now hold the Keyblade reversed at the
same hilt. The weapon is rebuilt from Sora's native wrist/local matrices
for each pose pass; body, fingers and native local data are unchanged.
Wooden/dream weapons are excluded. Verify blade and keychain appearance in
game, especially during combos, casts, Guard and Glide/Superglide.

SETTINGS / SAVE BEHAVIOR
Tests use kh1-numbered-abilities.ini beside the executable and are mod-wide.
Old no-effect flags66..100 are cleared on upgrade to avoid autoactivating
previews. Flags101..114/127 remain visible, free, and unassigned. Former115
is Type G; its retired test bit cannot activate it. ID127 remains bit50.
When another save loads with an equipped stance, that stance wins the
conflict and clears the test; select a test again for that save if desired.

All12 stance IDs, main G combos (300/301/302;305/306/307), E/F actions,
normal/High Jump behavior, native Glide/Superglide and AP footer remain.
Stances still require one hidden native learned-list token; tests need no
native ability slot. No new game buffer capacity is claimed.

Scan, Dodge Roll, Guard, Glide, Superglide, High Jump and Mermaid Kick retain
their built-in no-AP/no-slot behavior with native action/room gates and stance
replacements. As requested previously, non-Sora member1..9 ability arrays
are removed; saving retains that removal. Uninstall does not recreate them.

VALIDATION
636 Rust tests/30 nonempty suites and150 final-PE checks pass (103 shared
F/G/tests/menu and47 E). All35 tests apply/restore in normal and Olympus
banks; checks cover all12 stances in both equip directions, one test at a
time, full native lists, zero AP, ordinary AP costs and old flag migration.
Reverse-grip geometry tests cover hilt preservation, axis reversal, segment
lengths, invalid input and repeated skeleton/IK-pass idempotence.

All245 test records meet existing fitting bounds across52,185 sampled poses:
max position error4.688 model units, basis0.105, segment below3.9e-11,
zero scale error and zero native root-helper error. All190 old original/
Terra/G/variant payload parts and both E/F action controllers are retained.
Windows x64 DLL builds with the existing4 exports/8 imported DLLs.

Windows APIs, rendering and shared Rust dispatch are substituted in the
harness. Actual game/Windows/GPU execution and final appearance/contact feel
remain for your test. See validation.json and source/STYLES-V65.MD for the
current receipts. Historical reports describe earlier builds. The full65-
commit source patch and exact private payload headers support rebuilding.

UNINSTALL / ROLLBACK
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with v65, close KH1,
disable the package and Build again. The hidden stance token is removed.
Built-in normal entries are restored where capacity permits, without evicting
another ability: Sora Scan/Guard/Roll off, shared movement on. Partner ability
lists remain removed. Numbered flags stop applying when the mod is removed.
