KH1FM STYLES v66 / s405 - TYPE G ACTIONS AND DARK RIKU PREVIEWS

INSTALL
Close KH1 and disable v65 or any older main Styles package. Import this ZIP
into OpenKH Mod Manager, enable v66, Build and launch with Panacea. Keep the
existing KH2FM resources/settings required by earlier stances. Standalone
Aqua/Terra tests and the full KH2 Combat DLL remain disabled.
Confirm s405 / STANCES v66 in kh1-dual-wield.log. The new native adapter is
for the supplied Steam Global build.

TYPE G
Ground combo:300,379,411. Air combo:305,306,482.
Item, ground and air:395. Held Glide:038.
Ground Cure/Aero/Thunder/Stop:390. Air:508.
Ground Fire/Blizzard/Gravity:416. Air:417.
Casting/recovery spans and native record durations are in VENTUS_ANIMATIONS.csv.

Square in the air starts330 in the initial stick/facing direction. It replaces
Superglide, travels half Type F's unobstructed distance (312 vs624 native units),
and keeps the original direction through release/steering. Native collision
can shorten either dash. Each enemy directly touched by the actual Keyblade
can take one native physical hit during the dash; there is no area hitbox.

A fresh airborne Circle plays410 with a small lift. Ground Jump must be released
before that aerial tap. Holding Circle can use Glide038 after410 finishes.
Square dash and Circle dodge each have one use per actual airtime; landing
resets them. L1/shortcut spells, casts, damage and scripts do not start them.

379,411 and482 get an additional direct-blade contact on the second pass.
Their native first-contact/action timing allows that pass before ending.
The first finisher pass flinches; the last can apply native finisher knockback.
Actual damage, enemy defenses, effects and sounds use the native pipeline.
A second hit requires an enemy to remain in contact with the blade.
Watch TYPE G BLADE CONTACT in the log for native contact damage records.

Reverse grip is refreshed after the full native actor blend/update as well as
the skeleton/IK passes. Missing unskinned grip/palm matrices use immutable
fallback. This targets the brief normal-grip transitions; verify appearance
in game. Body, fingers, hair and native local matrices are not edited by it.

DARK RIKU TESTS - CUSTOMIZE -> PASSIVES
101: ground3,4,5; air8,9,10.
102: ground11,12,13; air14,15,16.
103: ground17,18,19; air20,21,22.
104: ground23,24,25; air26,27,27 (last27 is filler).

These cover all23 unused clips of the available main1160 bank. They are visual
previews using native Sora combo behavior, without guessed move names or donor
AI/events. Main Type D's assignments remain. DARK_RIKU_TESTS.csv adds durations.
The separate1580 bank is not part of this gallery.

Passives66..100 retain the existing187-clip Ventus gallery and its guide.
Every test costs0 AP. Equipping any test unequips all stances/other tests;
equipping a stance clears the test. Normal passives keep normal AP behavior.
After closing the menu, stand idle for a safe native-data handoff.
Selecting the current test again disables it, without auto-equipping a stance.
Enable Combo Master if you want to preview complete chains without a target.

Old no-effect101..104 flags cannot autoactivate a new preview. Existing Ventus
selections and unused105..114/127 flags retain their meaning. The mod-wide
kh1-numbered-abilities.ini stores test selections. A saved equipped stance wins
a conflict when another save loads. Stance IDs and native48-byte capacity stay.

RETAINED BEHAVIOR
All35 Ventus previews, previous Terra payload parts and Single E payload remain
exact. Type F retains its existing dash. Other stance mappings, native passive
AP costs, the readable footer and larger white spent/max AP stay.
Scan, Dodge Roll, Guard, Glide, Superglide, High Jump and Mermaid Kick remain
built-in without AP/slots, subject to native gates and stance replacements.
As requested previously, non-Sora ability lists are cleared; saving persists
that removal, and uninstall does not recreate those partner abilities.

VALIDATION / TEST
644 Rust tests in30 nonempty suites;160 final-PE checks (112 shared,48 E).
Type G's38 records/4 variants meet the established curve bounds, including
zero scale error and zero native root-helper error. All2139 original Dark Riku
mapped pose samples pass. Exact source reconstruction and package hashes are
included with validation.json and source/STYLES-V66.MD.

The PE harness substitutes Windows APIs, rendering and shared Rust dispatch.
No actual Windows/game/GPU session or live new enemy contact was run here.
Test both banks, grip transitions, casts/items, both combos, dash damage,
shortcuts, landing resets, held Glide and stance/test switching. Contact-window
alignment and combat feel remain provisional until your game test.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v66, close KH1,
disable the package and Build. The hidden stance token is removed. Built-in
normal entries restore where capacity permits without eviction (Sora entries
off, shared movement on). Partner ability lists stay removed; numbered flags
stop applying when the mod is removed.
