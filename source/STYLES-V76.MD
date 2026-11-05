# Styles v76 / s415: Triangle Overdrive activation

Choose an Overdrive under Customize, then return to the field. Selection now
arms the native Triangle box above the command menu, labeled Overdrive. A fresh
Triangle press plays the full KH2 Sora Drive transformation (motion52) once.
Infinity Tip Charge and Counterguard Hand Flash start together, centered on
Sora and tinted with that Overdrive's configured color. The selected aura only
starts after the transformation's final pose has actually been submitted.

The same source motion and dedicated base-Sora retarget apply to stock Sora and
all12 stances, including the Riku/Roxas donors and native E/F/G body paths. The
stance remains equipped. Normal mod effect layers are hidden during the
transformation; its two activation elements are the only layers this renderer
draws then. At completion or interruption, current native parent-local matrices
restore the body before the regular stance/native pose path resumes.

## Input and lifecycle

The native context fill runs first. Only a free fourth root-command entry
(0,0x42,0x43) may become Overdrive, and only while the first entry is Attack.
Existing Talk/Open or other native contextual actions take priority. Submenus,
shortcuts/L1, events, scripts, occupied attacks/casts, custom air actions, pause
and removal do not offer a new activation. The native box supplies its existing
Triangle glyph, location and layout; no separate overlay is placed over it.

The reserved empty command record0x87 uses word0x1F5. Its held-input flag permits
KH1's Triangle dispatch; the adapter still requires the logical pressed bit
0x04000000 and a release latch. Holding Triangle cannot repeat the animation or
effects. The owned command is consumed before native command execution, so its
placeholder type never enters native spell/MP/event handling. Only the owned
fourth entry and its two bit3 disabled masks are leased/restored. A conflicting
record is left untouched and the prompt is not offered.

The transformation clock uses native game delta, capped against invalid/large
steps. It samples motion52 without looping for its full length (the source is
80 at30fps, exposed as160 game frames). Native player control still runs with a
neutral stick and temporary action-bit masks. System/pause input and native
collision, gravity and damage continue. No position, HP, MP, AP, gauge, partner
or stance-choice writes are introduced. This is a visual activation sequence,
not the earlier complete Drive-state system.

Only a matching actor/instance/binding-generation/selection/serial pose witness
at the final animation frame enables the aura. Interruption, missing final pose,
or changing selection/scope cancels an incomplete activation and leaves the
aura off. A missing final witness times out after120 game frames. Selecting a
different Overdrive, unequipping/re-equipping one, or a new actor/instance arms
it again. A completed activation survives ordinary attacks and stance changes
on the same actor/instance. Returning to the title/new actor needs activation.
The selection persists in the existing INI; activation is runtime state only.

After completion another fresh Triangle press may play one new sequence for
the selected Overdrive. Its old aura goes off while that sequence plays, then
returns after a new final witness. No cooldown, gameplay bonus or Drain
deduction is implemented in this iteration.

## Effects and anchoring

| Activation effect | KH2 archive | Element |
| --- | --- | --- |
| Infinity Tip Charge | obj/P_EX100_KH1F.a.us | 20 |
| Counterguard Hand Flash | obj/P_EX100.a.us | 41 |

Both are separate Effects instances sharing their immutable original package
libraries. Grayscale/alpha/subtract texture variants use the same color filter
as the nine existing Overdrives. Original preview textures and stance effects
remain unchanged. A live body-center anchor is70 native units above Sora's
actor origin; subtract each element's authored hand/tip translation while
retaining its rotation and scale. No hand/tip attachment is used for activation.

Each element starts once per activation serial. A short flash may expire
naturally and is not restarted. The looping Infinity charge is bounded by the
transformation's lifetime; both handles are killed on completion/cancellation.
Both source elements and motion52 must be admitted before offering the prompt.
Failure to start both elements or an oversized draw cancels the activation and
quarantines activation effects for that process. Original particle programs
still use the existing interpreter; skipped programs are reported, not replaced.

Useful log lines are OVERDRIVE ACTIVATION READY, ACTIVATION FX READY,
ACTIVATION START, TRANSFORM POSE READY, ACTIVATION FX START, and OVERDRIVE ACTIVE.
Cancellation, missing resources and geometry rejection have separate messages.
Look for s415 / STANCES v76 after restarting with the new DLL.

## Sources and confidence

User request establishes Triangle, both named elements, the common transform,
centered recolor and delayed aura. docs/kh1-drive.md's command records/input
notes and the existing limits.rs context-fill adapter establish the native
fourth-entry pattern, held-dispatch flag and logical Triangle bit. The supplied
Steam executable confirms the position-independent six-byte context prologue,
name call target and16-byte command-record getter. Existing Rva mappings are
used throughout; nominal Epic offsets are never read directly in Steam.

form.rs and docs/drive-model.md identify source motion52. The v75 catalogue and
docs/kh2-effects.md identify Limit20 and Sora41. Existing retarget/native-local
restore, inverse effect pose, texture/color filter and PAX interpreter provide
the implementation. Center height70 and full source-duration playback are
adaptation choices; they are not a claim about original KH2 activation timing.
Confidence high for source mappings and tested lifecycle/input boundaries;
native box rendering, retarget appearance, center/scale/color and particle
completeness need the user's actual game/GPU test.

## Validation and retained scope

674 Rust checks in30 nonempty suites pass. Nine new checks cover activation
policy, body-center math and the actual native adapter with inert engine
dependencies: held/fresh input, final-pose witness, all stance generations,
selection/scope resets, prompt conflicts/priority, interruption and temporary
control masks without actor writes. The tests do not run a game or GPU.

Nine focused final-PE C/menu checks also pass against the supplied Steam
image, retaining39 preview descriptions, all12 stance coexistence paths,
exclusive preview selection, passive capacity and native AP/help boundaries.
Rust callbacks/rendering are mocked in that harness. Windows x64 release and
PE exports/imports are checked. Both private generated animation headers are
byte exact to v75. Full source reconstruction, bundle, ZIP CRC and file hashes
are verified in delivery receipts. No actual Windows/game/GPU run is claimed.

The nine Overdrive names, palette3, Drain boxes and future-effect descriptions,
Customize/Appearance, footstep mute and39 KH2 passive previews remain. Existing
stance combat, movement and native ability policies are retained. There are no
KH1/BBS effect demos, new buffs, drains or full Drive-stat/party changes.
