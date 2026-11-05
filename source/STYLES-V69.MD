# Styles v69 / s408: Type F damaging air dash

## Requested behavior

Copy Type G's damaging air dash330 to Type F and make the copy travel1.5x
Type G's current distance. Keep the same animation timing; increase travel speed
so the longer distance fits the same action duration.

| Parameter | Type G retained | Type F v69 |
| --- | ---: | ---: |
| BBS animation | Ventus330 | Ventus330 |
| Weapon grip | Reverse | Ordinary |
| Speed per native tick | 16 | 24 |
| Duration, native ticks | 29.25 | 29.25 |
| Unobstructed distance | 468 | 702 |
| Visual rate | 4/3 | 4/3 |
| Damage | Direct blade contact | Same native blade-contact path |
| Uses per airtime | 1 | 1 |

A fresh airborne Square starts the dash and locks the initial stick/facing
direction. L1/LB+Square magic shortcuts and the active shortcut menu retain their
input and cannot start/spend the dash. Native collision, casting/damage/script
exclusions, landing-only reset and ordinary held Glide remain.

## Implementation and boundaries

F's scoped fall variant copies the immutable G330 conversion before its reverse
grip bake. Native counts, header, events, travel helpers and allocation remain.
The native fall handle stays unchanged and no native Superglide record is
borrowed or edited. Full record admission precedes writes; finish/interruption
restores F's admitted fall body. This uses G's existing body-variant machinery.

The existing physical contact coordinator now permits main F only during the
live dash. It samples the equipped blade against native enemy body parts and
uses G's original physical damage/feedback route. One accepted damage record
per enemy per dash; failed/rejected contacts may retry. F's ordinary attacks,
magic and reactions never enter G's paired-contact/finisher logic. A style change
gets a fresh ledger even when native actor/binding/request are unchanged.

G's dash/dodge, grip bake, paired attack windows and all35 Ventus previews stay.
Other F poses, combos and casting, E, Dark Riku previews, all other stances,
Customize/Passives/AP and built-in ability handling remain.

## Sources, confidence and validation

Sources: the user's copy request and1.5x-distance clarification, v68 implementation
and immutable330 fixture. Confidence is high for source selection, requested
ratio, native write bounds and offline control/contact routing. Actual visual
appearance, collision distance and finalized enemy damage require game testing.
No Windows/game/GPU session is executed here.

- 647 Rust tests in30 nonempty suites pass, including the actual contact coordinator
 compiled with fake game memory/native contacts. F live dash, rejected-contact
 retry, one success per target, restart and F/G ledger isolation execute; F
 normal attacks remain outside G contact/reaction logic.
- 119 shared final-PE checks and48 E regressions pass. F330 normal grip, unchanged
 motion-array handle,29.25 ticks/702 units across multiple fractional tick sizes,
 both banks,4/3 shared animation rate, landing/reset/shortcut/cancel behavior and
 foreign-body refusal execute in the compiled adapter. The shared Rust caller,
 Windows services, collision and rendering remain mocked in this harness.
- All37 existing profile payloads, every G dash/dodge/cast part, immutable038,
 existing F cast variants and E private data remain byte exact. Only the new F
 fall variant adds the un-reversed330 body data.
- Windows x64 release retains the existing4 public exports/8 imported DLLs. Full
 source reconstruction, ZIP CRC and per-file hashes are checked before delivery.
