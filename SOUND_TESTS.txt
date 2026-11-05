# Styles v77 / s416: charge-length activation and sound auditions

Overdrive motion52 now stops when Infinity Tip Charge finishes. It no longer
waits for the unused tail of the full160-game-frame transformation clip. The
same centered, recolored Limit20 and Sora41 activation elements start once per
fresh Triangle press. The selected aura still waits for a submitted pose at
the stopping point. All12 stances and base Sora use this common path.

Customize -> Passives replaces the previous weapon-effect gallery with45
sound-audition choices in66..110. Pick one, return to the field, then start a
ground combo. It plays once at combo entry; later hits do not restart the sound.
Allow the combo to finish, then start another to listen again. Selecting the
active passive again disables it. Sound previews keep the equipped stance.

## Catalogue

| Passive | Sound source | Identifier |
| --- | --- | --- |
| 66 | Infinity Tip Charge sound reference | KH2 Limit Form, element20 |
| 67 | Counterguard Hand Flash sound reference | KH2 Sora, element41 |
| 68..110 | KH2 bank999, sound IDs0..42 in order | SE999000..999042 |

Rows66/67 resolve each source PAX element's actual sound field at runtime. The
description appends the resolved SE number when assigned. An effect may have
no assigned sound; it then reports No playable sound assigned. Rows68..110 are
an indexed first batch from se/se999.win32.scd, not claimed semantic names for
unheard clips. The description names the bank and SE ID. These are45 choices,
not necessarily45 distinct recordings: package references can alias a bank ID.

Three measured footer lines show the name, source/SE identifier and readiness.
Ready says Plays once at ground combo start. Other states are loading, no
playable assignment, missing archive/bank, decode failure or audio budget.
Native Passives AP cost and the AP Used/max footer remain. Preview rows cost0.
Reserved111..114/127 keep their flags and have no assigned audition.

## Transformation timing

Physics advances the two existing isolated activation Effects instances.
The finite Infinity handle's actual expiry reports a serial-scoped charge-end
event. That event shortens the current animation endpoint to its current source
frame, preserving normal playback speed. It cannot finish a later activation.
A matching pose at that endpoint must still be drawn before aura enable.
Counterguard's shorter flash may expire naturally; both handles are retired
when the sequence finishes or is interrupted. Effect state clears cancel an
incomplete activation rather than restarting its effects under the same press.

If Infinity's DPD is authored to loop, it has no natural completion callback.
For this requested one-time activation, use its checked authored DPD end tick
for one pass, including element start wait and the interpreter's final tick.
The source bound is1..240 effect ticks plus0..60 game frames of start wait.
Reject a looping payload without a valid finite authored pass rather than
inventing a fixed animation duration. Logs record its real authored end and
the chosen limit. The original immutable effect library is unchanged.

The source motion remains clamped at its full length if a charge outlasts it;
it never loops. An uncompleted charge cancels after600 game frames, and a
missing final cut-pose witness cancels after120 further waiting frames (within
the total cap). Pause freezes these clocks and effect simulation. Cancellation
does not grant an aura. Native Triangle interaction priority, fresh-press
latch, selection/scope lifecycle and visual-only native controls remain v76's.

Useful timing lines: OVERDRIVE CHARGE TIMING READY and OVERDRIVE CHARGE END.
The latter reports actual effect frames, transform cut point and natural vs
authored-pass expiry. There is no new hardcoded shortened duration in seconds.

## Sound loading and trigger

The existing KH2 SCD reader resolves sound-ID records, not stream indices,
using the same Backup/Live install policy as other KH2 resources. A background
thread reads only the two PAX references and needed sound banks, decodes each
unique recording once and publishes an immutable PCM cache. The game thread
does no sound-file I/O or decoding. Missing/empty IDs remain visible as such.
Original game sounds and game assets are not redistributed in the mod package.

Use the existing waveOut mixer and the user's kh2_volume plus native master/SFX
sliders. A preview's PCM plays once, including any stored loop region only once.
The preview filter admits mono/stereo,4000..96000Hz, at most15 seconds per clip
and64MiB total decoded audition PCM. Reject unsupported/malformed/budget clips
with a visible status; never substitute an unrelated sound.

Each native physics callback samples the exact actor/instance/generation.
Native normal ground-combo requestsC8..CB require native state0 and a matching
current motion header. CC..CE air combos, casts, guard and roll do not trigger.
Imported stances require an actual grounded Attack output; guard, roll, recoil
and aerial-dodge sessions are excluded. This covers normal native/base/E/F/G/D
combos and the existing KH2-owned style lanes. Native ability-only attacks
outside the basicC8..CB range are not additional audition triggers.

A latch spans continuing combo hits and tolerates brief one/two-game-frame
gaps. Three non-combo game frames rearm the next audition. Duplicate callbacks
for the same frame cannot replay it. Selection/scope changes reset it; pause,
events/scripts, removal and Overdrive transformation suppress it. A tagged
preview voice is retired on selection/scope/pause changes or a new audition;
ordinary mixer voices remain. Already submitted audio buffers can take up to
roughly80ms to drain. Sounds are not attached to Overdrive activation yet;
this batch lets the user select suitable SE IDs for that next change.

Persist choices with sound_previews=kh2-v1 in kh1-numbered-abilities.ini. Old
animation and weapon-effect preview flags reset on upgrade, including the six
newly repurposed IDs, so installing cannot unexpectedly play a sound. Other
reserved flags remain. WeaponFxChoice and both old animation selectors return0;
the audio choice never starts a body profile or particle preview. Both private
generated animation headers stay byte exact. No stance, AP, HP/MP, native save
or attack/contact state is written by the audition sampler.

Useful audio logs: SOUND PREVIEW READY, SOUND PREVIEW CATALOGUE READY and
SOUND PREVIEW PLAY, including passive number, actual SE ID and decoded length.
Look for s416 / STANCES v77 after restarting with the new DLL.

## Sources, confidence and validation

Source: user's request for charge-length transformation and ground-combo sound
auditions. Existing v75/v76 catalogue identifies Limit20/Sora41; actual PAX
sound fields are read at runtime. docs/kh2-sound.md and kh2_formats::scd document
SE bank/ID lookup, codec decoding and the existing mixer. docs/combat-model.md's
native request table identifiesC8..CB ground andCC..CE air. Existing takeover
Attack/airborne/session state supplies imported-lane classification.

Actual Infinity expiry is authoritative for finite effects. Loop single-pass
termination uses DPD's checked fixed-point end; bounds, latch grace and PCM
budgets are deliberate audition-host choices. Confidence high for tested
state/mapping/storage boundaries; source resource availability, exact audible
recordings and visual cut quality still require the user's game/audio/GPU test.
No semantic sound names are guessed for numeric bank entries.

683 Rust checks in30 nonempty suites pass, including nine new checks for
catalogue/migration/budgets, combo latching, the actual physics adapter with
inert audio/engine leaves, and serial-scoped charge shortening. Existing
native Triangle adapter tests now verify an early charge cut with delayed aura.
Ten focused final-PE C/menu checks pass against the supplied Steam image,
covering all45 descriptions, resolved source IDs, readiness, exclusive choices,
all12 stance coexistence paths, full passive capacity and native AP/help.
Their Rust callbacks, mixer and actual playback are mocked.

Windows x64 release, PE exports/imports, unchanged generated headers, full
source reconstruction/bundle and package CRC/hashes are verified in receipts.
No actual Windows/game, audible playback or GPU run is claimed. The nine
Overdrives, palette3/Drain/help, Customize/Appearance, footstep mute and existing
stance combat remain. This adds no Overdrive bonus, Drain deduction or KH1/BBS
sound gallery.
