KH1FM STYLES v78 / s417 - GITHUB RUNTIME PACKAGE
Same gameplay DLL as the full v78 release; short-path packaging only.

INSTALL
Close KH1. Disable v77 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v78, Build and restart with Panacea. Keep the existing
KH2FM resources/settings. Confirm s417 / STANCES v78 in kh1-dual-wield.log.
Target: supplied Steam Global build.

CHANGES
Type G attacking aerial dash (Square): Sonic Rave effect27 from KH2 Limit Form,
plus exact KH2 sound SE999027 once at committed dash entry.
Type F attacking aerial dash (Square): Sonic Rave Finish effect30 from the same
package, plus exact KH2 sound SE999027 once at committed dash entry.

Dash visuals retain original colors and use the actual primary blade, including
G's reverse grip. G's Circle dodge and F's ground dash keep their existing
behavior. Dash animation, distance, speed, fixed facing, collision, damage and
once-per-airtime rules are unchanged. Magic shortcuts are not dash triggers.
A held dash or pause/resume does not replay feedback. A finite source tail can
finish; one visual handle is capped at two game seconds to avoid accumulation.

Overdrive: select it in Customize, return to the field and tap Triangle when
the native Overdrive prompt appears. The accepted press now plays the sound
referenced by Infinity Tip Charge (KH2 Limit20, same source as audition66).
The transformation uses only the first60 game frames of KH2 motion52 at its
normal speed: one second of game time. The complete clip is not sped up.
Its final pose still must be drawn before the aura starts. Remaining activation
effects retire with the transform. The sound plays once at its normal length.
All stances and stock Sora share this path. Native interactions keep Triangle
priority; rejected/held presses do not play the activation sound.

RESOURCES / LOGS
Visual archive: obj/P_EX100_KH1F.a.us, elements27 and30.
Dash sound: se/se999.win32.scd, ID27 = SE999027.
Activation sound: actual PAX sound field of Limit20, resolved from your KH2 files.
The background sound loader already includes these sources. No original audio
is distributed and no decoding/I/O occurs on the action frame. Existing
kh2_volume and native master/SFX sliders apply. Missing/not-ready audio or
unsupported particle programs are logged without changing movement/animation.

AIR DASH FX SOURCE reports particle admission and skipped programs.
AIR DASH FX START and ACTION SOUND PLAY identify the accepted action.
OVERDRIVE ACTIVATION START reports length60; OVERDRIVE ACTIVE follows its pose.
Exact weapon fit, particles and audio need your installed-game check.

RETAINED
Passives66..110 still audition45 KH2 sound choices at ground-combo entry;
SOUND_TESTS.csv/.txt retain the list. These auditions are separate from the
new normal dash/activation sounds. All12 stances, intrinsic abilities/native AP,
nine Overdrives/palette3/Drain/help, Customize/Appearance and footsteps mute
remain. No buffs or Drain deduction. C movement sources and both generated
animation headers are byte exact to v77.

VALIDATION
688 Rust checks/30 nonempty suites and10 focused final-PE menu checks pass.
New checks cover exact F/G element routing, one session per dash, Circle and
scene exclusions, actual sampler with inert action/audio leaves, and pause
where the native getter temporarily reports0. Updated Triangle checks count
one audio request per accepted press and the60-frame pose window. PE checks
retain all45 auditions, source IDs/statuses, all12 stances, native AP/help and
capacity; Rust rendering/audio callbacks are mocked. Windows x64 release,
exports/imports, source reconstruction, bundle, ZIP CRC and hashes are checked.
No actual Windows/game/audio/GPU session ran here. STYLES_V78.md contains
the exact scope, sources and live checks.

REMOVAL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save with v78, close KH1,
disable the package and Build. Existing restoration rules remain, including the
previously requested saved removal of partner abilities.
