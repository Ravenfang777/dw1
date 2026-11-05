# Styles v71 / s410: shared Overdrive colors and Type E tuning

## Shared effect set and exact palette

Every Overdrive now selects the same three visual layers: Valor, Wisdom and
Anti body effects. The menu still permits one free Overdrive independently of
Stance, with no native ability slot consumed and no stat boost. Confirm the
active row to disable it. Strength is renamed Power without changing its ID1,
so a saved Strength selection becomes Power.

| Overdrive | Color | Default RGB hex |
| --- | --- | --- |
| Power | Red | #FF0000 |
| Will | Blue | #0000FF |
| Resistance | Yellow | #FFFF00 |
| Prowess | White | #FFFFFF |
| Rage | Black | #000000 |

The received v70 log shows Valor elements1/5/6, Wisdom11/12/100 and Anti1/5/6
available, while Master and Final report missing form effect archives. This
establishes a local resource failure; it does not establish that those forms
lack effects. The shared set removes the Master/Final effect dependency.
The user's existing KH2 resources still supply the three required layers.
Unavailable layers are logged individually; do not invent a substitute.

Clone only the Overdrive GPU textures. Remove their baked RGB bias while
retaining intensity and alpha, then apply the selected color to their particle
vertices. Separate alpha/luminance masks let authored darkening/subtractive
particles receive a hue; these use alpha blending. Black additive particles
also use alpha blending and a luminance mask so Rage can remain visible.
Other spell/stance packages retain their textures and render policy. Type M?'s
ordinary idle aura is suspended while an Overdrive supplies the Anti layer;
its attack-specific visuals remain. Changing the selection retires all three
old layer handles before the new set starts.

Colors can be edited in kh1-overdrive.ini beside the mod's other settings:

```
overdrive = 1
power_color = #FF0000
will_color = #0000FF
resistance_color = #FFFF00
prowess_color = #FFFFFF
rage_color = #000000
```

0 disables selection;1..5 are the table order. The file is read at startup,
so restart the game after a manual color edit. Menu selection changes preserve
custom colors and unknown settings and append any missing default color keys.
The old strength_color key is accepted; power_color takes precedence. No
texture extraction or manual image editing is required for these tints.

Sources: the user's combination/color/name requests; received v70 diagnostic
log; existing Anti body-aura selection, KH2 effect parser and isolated renderer.
Confidence high for selection, data isolation, palette/config and render policy.
Actual blend appearance and color intensity need a live GPU/game check.

## Hands and Rage geometry

The video shows hand glows displaced from the hands and long jagged dark
streaks extending across the room. Capture an immutable native model pose
during the known animation pass rather than reading the live render palette
later in physics. Scope it to the exact field actor instance/generation and
accept it for at most two game frames. Convert it to the base KH2 effect rig.

Translate that effect rig's wrists/palms and descendants onto the native
wrists/palms: KH2 left80/86 to KH1 left205/206; right172/178 to100/101. Preserve
bone axes and the character's actual body/weapon poses. Reject non-finite or
implausibly displaced anchors before starting an aura. Overdrive drawing
rejects invalid triangles and vertices more than350 native units from Sora,
preventing the observed room-spanning streak class from being submitted.
This bounded particle check applies only to the cloned Overdrive packages.

Sources: the received comparison video, existing native skeletal mapping,
animation-phase hooks and local inverse-retarget implementation. Confidence
high for write scope, immutable ownership and finite/boundary checks; moderate
for the visual diagnosis. Hand alignment during all poses/transitions and
Rage's complete appearance remain live verification work.

## Type E changes

The v70 log already reaches the1.25x native jump boost. Its air input adapter
nevertheless clears Circle in native takeoff/rise requests4/5/9/10, which can
shorten held ascent. Preserve held input in those requests while retaining the
native Glide constructor suppression. Fresh Circle still starts the finite
once-per-airtime dodge, and Superglide remains usable.

Raise the main E native launch-height factor from1.25 to1.5:20% higher than
v70. Scale arc time by sqrt1.5 so the existing native gravity remains. Both
ordinary and High Jump launches use the same scoped rule. Other stances,
numbered tests, finite dodge distance/speed/lift and attack jumps remain as
before. This is a calibrated increase; parity with every other stance has not
been measured in game.

Slow both301/native GC2 variants by another15%: their native motion-delta
factors are(47/24)*0.85*0.85 and(63/24)*0.85*0.85,72.25% of the rate before
the v70/v71 reductions. The animation and native event clock slow together;
no held recovery segment or new pause is added. No generated animation body,
event, request table or travel data is changed in v71.

Sources: user report/request, received log, native jump-curve implementation
and existing E adapters. Confidence high for ratios, native curve and input
preservation; visual jump parity and attack feel need a game check.

## Validation and preserved scope

- 655 Rust tests in30 nonempty suites pass, including palette persistence,
 exact default colors/Power alias, hand placement without body/axis changes,
 texture masks, visible black blending and rejection of malformed streaks.
- 122 shared final-PE checks pass, including Power/AP0/exclusive selection,
 menu persistence/independence and existing F/G/numbered profiles/controls.
- 49 E final-PE checks pass, including held input throughout ascent with
 ordinary Glide suppressed; actual native normal/High Jump launch/curve;
 both slower GC2 variants and existing dodge/Superglide/Guard controls.
- Both generated private headers remain byte exact to v70. No asset refit or
 animation regeneration is required. All prior stance mappings, F body-dash
 contacts, G reverse grip/two-pass attacks and numbered tests are retained.
- Windows x64 release builds with4 public exports and8 imported DLLs. Delivery
 also verifies full source reconstruction at the pinned upstream and ZIP/file
 hashes. No Windows loader, game or GPU session was executed here.

The PE harness executes the final compiled C adapters with Win64 ABI/API
mocks and substitutes the shared Rust/renderer startup. Rust pure tests cover
the render transformations, not the user's actual form assets or final GPU
output. In game, cycle each Overdrive on E/F/G and imported stances, check hand
tracking/black Rage through transitions, toggle off/change Stance and verify
old particles stop. Compare E's held jump and second attack to v70.
