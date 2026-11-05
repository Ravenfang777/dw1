# Styles v68 / s407: G grip transitions, air travel and paired contacts

## Evidence and scope

The supplied s406 log confirms completed330/410 travel at39 native ticks and
some extra blade-contact records. The video shows the weapon jumping between
orientations, and the user clarified that this happens across pose transitions.
The log demonstrates record creation, not two finalized damage applications on
every attack. Previous contact code only supplied a second-pass attempt and
assumed that the native first contact had landed.

The runtime grip writer reconstructed from immutable bind offsets, while the
converted records use a different calibrated grip. Source inspection finds a
fixed160/0/-65-degree rotation and calibrated translation in every converted
clip; the raw bind uses different values. Repeated skin/transition updates plus
an independent writer provide competing weapon outputs. Confidence is high for
the conflicting paths and differing attachments; live resolution still needs
the user's game test.

## Reverse grip in the native records

Retire the runtime280..292 correction and its unused pure helper. Instead,
right-multiply the existing local grip280 rotation by a180-degree local-Z turn.
This reverses its longitudinal-X blade axis at the same hilt. Bake only the
three rotation values, either in constant channels or existing one-key curves.
Never change headers, allocation, channel/key counts, helpers, translation,
scale, body/hair/finger curves or source files. Every build starts from the
immutable converted inputs, so regeneration cannot compound the transform.

Main G, its four body variants, the immutable038 display and all35 Ventus test
profiles receive the same rotation. Native sampling and blending now carry the
hold between converted poses. No world/local palette is rewritten for grip.
The existing post-update/final-draw callback remains only for the separate038
visual and physical contact coordinator. Original/Type F data and E's private
payload remain exact. Unmapped native actions retain their own native records.

## Faster, longer G air actions

| Parameter | v67 G | v68 G | Type F retained |
| --- | ---: | ---: | ---: |
| Horizontal speed per native tick | 8 | 16 | 16 |
| Duration, native ticks | 39 | 29.25 | 39 |
| Unobstructed horizontal distance | 312 | 468 | 624 |
| Dodge lift per native tick | 0.75 | 1.5 | 0 |
| Total dodge lift | 29.25 | 43.875 | 0 |

Both330 dash and410 dodge have2x the previous movement speed and1.5x distance.
Duration is75% of the previous value. Their visual rate is4/3, so the complete
animation fits that shorter travel. The existing shared native motion hook calls
the G-only rate adapter before the original update; a terminal clamp holds the
last pose until movement finishes. Other actors, F, tests, casting and other
styles keep their previous rates. No new hook is installed.

Keep native collision, initial direction/facing lock, one use per real airtime,
shortcut/cast/script/damage gates and ordinary038 Glide after the action.

## Two contact passes

| Clip / native request | First source-frame window | Second window |
| --- | --- | --- |
| 379 / C9 or CA | 8..13 | 14..18 |
| 411 / CB | 2..7 | 8..14 |
| 482 / CE | 2..6 | 7..11 |

Both windows now test the actual blade against native body parts. A ledger
shared with native record construction permits one successful record per target
per pass. Witness an original native hit; skip the corresponding fallback.
After a fallback succeeds, reject a later duplicate native record in that same
pass. The second pass has a separate allowance. Rejected attempts do not consume
the pass, and the blade sweep never bridges the gap between passes.

The native filter requires main G, the exact field binding/current regular
request and an original attack row for that request. It does not intercept
other styles, actors, unrelated/ability rows or concurrent spell data. Internal
fallback contacts bypass it explicitly, avoiding recursion. Pause/header gaps
retain hit allowances; a new request/restart/binding creates a new action key.
Native hit witnesses do not consume the next physics sampling opportunity.

The prior timing conversion also collapsed some native on/off gates to the
same timestamp. Shift their edges together instead, preserving positive-width
windows after the second swing. Only selected main-G timestamp floats change;
original/F/test timelines, event counts, payloads and descriptor pointers remain.
The actual native event sampler verifies those windows in the PE test.

Contacts still use native physical damage/feedback and defensive processing;
no HP edits or general invulnerability bypass is introduced.411/482 retain
first-pass flinch and second-pass native finisher knockback.330 retains its
single blade-contact pass. Contact logs label pass1/pass2 and whether native
record construction or the blade fallback supplied it. Damage-record values
do not themselves establish finalized HP loss or visible effect timing.

## Validation and live limits

- 647 Rust tests in30 nonempty suites pass. Replace obsolete runtime-grip tests
  with tests for the two-pass ledger and actual Windows G contact coordinator
  compiled with fake memory/native dependencies. Cover native-first/fallback-
  second, fallback-first/native-second, duplicate suppression, failed retries,
  pause gaps, restarts, binding changes and unrelated native attacks.
- 118 shared-adapter and48 E final-PE checks pass. New checks execute the actual
  shared native motion hook and verify4/3 visual delta, terminal clamp, native
  return preservation, restored rate, non-collapsed native gates, exact29.25 duration/468 travel/43.875 lift
  under fractional/different ticks, both banks, budgets and previous controls.
- 324 converted source records /2268 sampled poses pass: body error0, travel
  helper error0, reverse-weapon position error below0.000004 and basis error
  below0.0000001. Every clip has the same baked grip rotation. Only its rotation
  values change; hilt position, lengths, body poses and native counts remain.
- Original/Type F/Type F variants and E payload are byte exact. All existing
  G animation assignments, event payloads and Dark Riku previews remain.
- Windows x64 builds with the existing4 public exports/8 imported DLLs. The
  full source patch, archive CRC and file hashes are verified for delivery.

No Windows/game/GPU session was run here. Geometry and finalized native damage
are not emulated by the portable contact-coordinator test. Check transition
appearance, two distinct contacts on reachable enemies/objects, and travel in
game. Native collision can shorten distance; a blade that misses cannot hit.
