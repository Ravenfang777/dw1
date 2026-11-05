# Styles v78 / s417: F/G dash feedback and one-second Overdrive

| Accepted action | KH2 visual | KH2 sound |
| --- | --- | --- |
| Type G attacking aerial dash, Square | Sonic Rave effect27, Limit package | SE999027 |
| Type F attacking aerial dash, Square | Sonic Rave Finish effect30, Limit package | SE999027 |
| Overdrive Triangle activation | Existing centered, recolored Limit20 and Sora41 | Sound assigned to Infinity Tip Charge, Limit20 |

Both dash elements come from obj/P_EX100_KH1F.a.us. Dash effects keep their
original particle colors. Only the existing Overdrive activation elements use
the selected Overdrive's color filters. Type G's Circle dodge/spin and Type F's
ground dash do not receive this new dash feedback.

## Fixed transformation window

The user replaces v77's charge-driven duration with one second. Keep normal
animation speed and use only the first60 game frames of base KH2 motion52.
Do not accelerate its full160-frame clip. The same dedicated base-Sora retarget
applies to every stance and stock Sora. A matching pose at frame60 must still
be submitted before the aura starts. The next physics handoff resumes native/
stance animation, so there can be one normal frame of handoff latency.

The charge's natural/loop lifetime no longer controls this endpoint or admits
the command. Remaining activation effect handles retire with the transformation.
Pause/native time scaling freeze/scale its game clock as before. Interruption,
selection/scope change and missing final pose still cancel without granting an
aura. Native Triangle interactions retain priority and holding Triangle cannot
repeat activation. No Drive stats, gauge, invincibility or resource logic runs.

The accepted Triangle press immediately asks the existing decoded sound cache
for the sound referenced by PAX Limit20 (the same source as audition66). It
plays once as a normal SFX voice, independent of selected sound auditions and
their retirement. A rejected/held press makes no sound request. This resolves
the actual source sound ID rather than guessing a numeric substitute. Its PCM
plays once to its natural end; audio is not stretched to fit one second.

## Committed dash observation

Read the existing C adapter's SingleFAirAction result. Only committed action1
in Type F/Terra or Type G/Ventus starts feedback. Pending/rejected Square,
magic shortcuts and other styles are not raw-button triggers. Action2 is G's
Circle410 dodge and is excluded. Ground dash never reports this air action.
Require exact actor/instance/binding generation, loaded field, no script/event,
no removal and no Overdrive transform. The sampler does not write actor state.

A scoped serial starts one sound request and one visual attempt per real dash.
Repeated physics/held samples keep the serial. When the action ends, another
committed dash can start a new serial under the existing once-per-airtime rule.
Pause retains the session even when the C getter temporarily returns0 due to
menu flags, so resuming cannot replay sound/effect. Style/scope loss retires it.

Dash sounds use exact SE999027 from se/se999.win32.scd. v77's background sound
loader already includes that ID and the Limit20 source sound. No new bank I/O
or decoding runs on an action frame. Reuse the existing mixer and native master/
SFX sliders plus kh2_volume. Ordinary action voices do not use the preview tag,
so changing a preview cannot cancel a dash or activation sound. Missing/not-yet-
decoded audio logs ACTION SOUND UNAVAILABLE; movement and animation still work.
No unrelated audio is substituted or redistributed.

## Visual attachment and lifetime

The existing Limit library provides an original-color Effects instance, separate
from the two isolated/recolored Overdrive activation instances. Source admission
logs whether27/30 have particle data and lists skipped interpreter programs.
Start a dash element only from a witnessed finite bone/weapon anchor. If the
first native draw has not published a grip yet, defer the visual until it does;
the sound still belongs to accepted dash entry. Never use identity as a fallback.

For effect bone codes0x4003..0x4008, use the actual drawn primary Keyblade's
calibrated root/tip/midpoint, including G's reverse grip. Other source bone codes
retain their authored mapping. Native F/G effect-only poses now refresh from
parent-local joints at field submission while feedback is needed. Neither this
pose publication nor the dash sampler writes native body matrices or movement.

Bound roots refresh again at draw without advancing particle clocks. At dash
exit, call the source element's normal end behavior; finite tails can finish.
Retire at natural expiry or120 game frames after start, whichever comes first.
At most one dash handle exists. A new dash replaces an older tail; style/scope
loss, transform or budget clear retires it. Retain the seen serial across effect
clears so one held dash cannot repeatedly restart after a renderer budget failure.
The existing geometry cap remains. Missing effect data never changes movement,
contacts or the independently requested sound.

## Retained behavior and diagnosis

No C movement adapter or generated animation header changes. Preserve F/G dash
body animation, speeds/distances, fixed facing, native collision, hit contacts,
once-per-airtime budgets and shortcut exclusions. G's Circle dodge, other moves,
all12 stances, native AP/intrinsic abilities, menus, nine Overdrive selections/
palette/Drain metadata, footstep mute and45 sound auditions remain.

Check s417 / STANCES v78 after restarting the new DLL. Useful logs:
AIR DASH FX SOURCE, AIR DASH FX START, ACTION SOUND PLAY, OVERDRIVE ACTIVATION
START (length60) and OVERDRIVE ACTIVE. Missing source/anchor/audio reports its
actual boundary. Sound auditions in66..110 and SOUND_TESTS.csv remain available.

## Sources, confidence and validation

User explicitly supplies Limit27 for G, Limit30 for F, SE999027 for both,
Infinity charge sound on activation and a one-second animation. Existing v75
catalogue identifies the Sonic Rave/Finish package elements; actual PAX sound
fields and SCD ID lookup supply audio. SingleFAirAction in unchanged terra.c
defines committed action1 vs dodge2. Existing native-local pose, primary blade
calibration, Effects end/budget, mixer and scoped v76/v77 activation policies
provide the implementation. Original particle programs are not invented.

Normal-speed first60 frames,120-frame visual-tail cap and source end behavior
are adaptation choices. Confidence high for tested selection/serial/timing and
read-only observer boundaries; final weapon fit, particle appearance, loudness,
audio availability and the cut's appearance need actual game/audio/GPU testing.

688 Rust checks in30 nonempty suites and10 focused final-PE menu checks pass.
Five new checks exercise dash routing/serials and the actual committed sampler
with inert engine/audio leaves. Updated native Triangle tests assert one audio
request per accepted press and the60-frame endpoint; timing tests cover pause/
native slow time. PE checks retain45 audition descriptions, resolved IDs,
exclusive choices, all12 stance coexistence paths, native AP/help and capacity.
Rust audio/rendering is mocked in that PE harness. Both generated headers and
C movement source stay exact to v77. Windows release/exports/imports and full
source reconstruction/bundle/ZIP hashes are verified in delivery receipts.
No actual Windows/game/audio/GPU run is claimed.
