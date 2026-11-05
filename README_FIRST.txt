KH1FM STYLES v77 / s416 - CHARGE TIMING AND KH2 SOUND AUDITIONS

INSTALL
Close KH1. Disable v76 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v77, Build and restart with Panacea. Keep your KH2FM
installation/resources/settings. Check s416 / STANCES v77 in the log.
Target remains the supplied Steam Global build.

OVERDRIVE
Select an Overdrive in Customize, return to the field and tap the native
Triangle Overdrive prompt. The KH2 transformation now ends with Infinity Tip
Charge, rather than waiting for the full animation tail. Its centered Infinity
and Counterguard effects retain the selected color. Only a matching pose at
the stopping point enables the aura. A looping source plays one checked authored
pass. Native interactions keep priority; holding Triangle does not retrigger.
The duration comes from the actual effect, not a new fixed number of seconds.

SOUND AUDITIONS
Customize -> Passives66..110 replaces the weapon-effect gallery with45 sound
choices. Choose one, return to the field, and start a normal ground combo.
The sound plays once at combo entry; continuing hits do not cut/restart it.
Finish the combo, then start another to listen again. Confirm the active passive
again to switch it off. All preview choices cost0 AP and keep your stance.

66: sound referenced by Infinity Tip Charge, KH2 Limit Form element20.
67: sound referenced by Counterguard Hand Flash, KH2 Sora element41.
68..110: SE999000..999042 from se/se999.win32.scd, in numeric order.

The first two show their actual resolved SE ID when one is assigned. Some
package elements or bank IDs may have no playable sound. Help explicitly shows
loading, missing/empty, decode failure or audio budget, with the source ID.
Numeric bank entries have source identifiers, not guessed semantic names.
SOUND_TESTS.csv and SOUND_TESTS.txt list all45 choices. Package references can
alias numeric IDs;45 choices need not mean45 different recordings.

Old animation/weapon-preview selections reset on upgrade. New selections use
sound_previews=kh2-v1 in kh1-numbered-abilities.ini. Reserved111..114/127 remain.
No native ability/save/AP slots are consumed. The old visual demo stops.

Playback uses the existing KH2 mixer, kh2_volume setting and native master/SFX
sliders. The KH2 files must be present. Loading/decoding stays off the game
thread. Clips play once, at most15 seconds each, with a64MiB total cache bound.
Changing selection/scope, opening pause, removal or a new audition retires only
preview audio; queued audio can take roughly80ms to drain. Ground basic combos
work with stock Sora/native E/F/G/D and imported style attacks. Air combos,
guard, roll, casts, events and Overdrive transformation do not start previews.
Native ability-only attacks outside the basic ground range are not triggers.

Sounds are being auditioned for later assignment to the transformation. Send
the preferred passive numbers or SE IDs after listening. No sound is newly
attached to the Overdrive activation itself in this build.

LOGS AND VALIDATION
SOUND PREVIEW READY/CATALOGUE READY/PLAY identify loaded and played IDs.
OVERDRIVE CHARGE TIMING READY/CHARGE END report actual expiry/cut frames.
683 Rust checks/30 nonempty suites and10 final-PE C/menu checks pass. These
cover policy and actual sampler with inert engine/audio leaves, all45 menu
rows, resolved IDs/statuses, all12 stance coexistence paths, capacity and AP.
The actual C menu adapter runs against the supplied Steam image. Rust audio
callbacks and playback are mocked there. Windows release/exports/imports,
headers, full source reconstruction, bundle, ZIP CRC and hashes are checked.
No actual Windows/game/audio/GPU session ran here; verify listening and the
transformation cut in game. source/STYLES-V77.MD records evidence and limits.

RETAINED / REMOVAL
Main stance combat/movement, intrinsic passives/native AP, nine Overdrives,
palette3/Drain/help, Customize/Appearance and footstep mute remain. Both private
animation headers are unchanged. No gameplay Overdrive buffs or Drain deduction.
For uninstall, set remove_dual_wield=on in kh1-dual-wield.ini; load/save with
v77, close KH1, disable this package and Build. Existing saved partner-ability
removal cannot be reversed automatically; existing restoration rules remain.
