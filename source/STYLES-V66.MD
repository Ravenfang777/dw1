# Styles v66 / s405: Type G actions and Dark Riku previews

## Type G mapping

| Action | Ventus source |
| --- | --- |
| Ground combo | 300 / 379 / 411 |
| Air combo | 305 / 306 / 482 |
| Items, ground and air | 395 |
| Held regular Glide | 038 |
| Square air dash, replacing Superglide | 330 |
| Circle aerial dodge | 410 |
| Ground Cure / Aero / Thunder / Stop | 390 |
| Air Cure / Aero / Thunder / Stop | 508 |
| Ground Fire / Blizzard / Gravity | 416 |
| Air Fire / Blizzard / Gravity | 417 |

Unspecified main G actions retain their previous mapping. The main profile now
contains38 regular records, adding held Glide75. Native Glide entry/exit and
travel remain; its held body uses038. Spell and item IDs, release events and
native effects remain. Requests36/37/3A use ground Fire/Blizzard/Gravity bodies;
38/39/3B/3C use the other family. Air83/84/87 and85/86/88/89 follow the same
split. The shared recovery switches only its body according to that family.
Source magic is divided into cast/recovery spans, listed in the delivered CSV.

## Air actions

Main G shares the proven native-fall collision movement path with Type F.
Square starts330 in the initial stick/facing direction and holds that facing
through release/steering. Its speed8 times39 native ticks gives312 unobstructed
horizontal units, exactly half Type F's16 times39 =624. Both retain native
collision; a wall can shorten actual travel. This replaces G's Superglide.

A fresh airborne Circle plays410, with speed8 and slight upward lift0.75 per
tick through the same39-tick duration. It allows held regular Glide038 after
completion. A ground Jump press must be released before an airborne Circle
can start the dodge. Each air action has one use per actual airtime; only a
real, unpaused, unscripted native landing resets its budget. Re-equipping does
not reset it. L1/shortcut-menu spells, active casts, damage, scripts and other
ineligible actions retain native input. Numbered previews gain neither action.

The dash/dodge bodies use scoped variants of the existing fall record, with
unchanged counts and allocation. G does not borrow a new game handle or alias
Type F's native Superglide source. All variants restore on interruption, exit
or safe bank readmission. Type F's existing alias and movement stay unchanged.

## Blade contacts and two-pass attacks

The330 dash checks the equipped Keyblade's actual native start-to-tip range
against native enemy body parts, once per enemy for that dash. It uses dense
blade spheres and bounded movement sweeps. No area hitbox around Sora is added.

379,411 and482 get one additional contact opportunity on the second blade pass.
Provisional source windows are379 frames14..18,411 frames8..14 and482 frames7..11.
The source paths, including blade rotation, were inspected offline. The native
first contact timestamps on ground records are aligned to the first pass; the
existing action/chain timestamps cannot end those attacks before pass two.
The air finisher's native lifetime is likewise extended. No event count, key
payload, script, descriptor pointer or native root-movement event changes.

First-pass411/482 finisher hits use native flinch3 instead of knockback5, so
small enemies can remain in reach for the second pass. This is restricted to
the exact original Sora finisher attack-data pointer and its first source phase;
concurrent spells and unrelated records are excluded. The additional final
contact uses the original native finisher row and knockback. Damage values,
stats, elements, resistances, impact effects/sounds and enemy processing run
through the existing native contact path. No HP writes, KH2 power multiplier,
extra Drive value, invulnerability or donor attack scripts are introduced.

Contacts run after the native actor animation update, never from a render
callback. They require main G, its admitted C binding, the current regular
request/header, a matching actor/model/generation and eligible field state.
They reject duplicate physics callbacks and reset per-action hit records on
real request/restart/binding changes. Native defensive rules still apply;
a second hit requires the blade to meet a hittable enemy on that pass.

## Reverse grip through blends

v65 corrected weapon matrices after the sampled skeleton/IK callbacks. Native
actor animation can perform a subsequent blend/rebuild. v66 also refreshes the
weapon after that complete original actor update, using fresh wrist100 and
untouched local transforms. Missing unskinned palm101/grip280 matrices can use
immutable bind-relative fallback rather than skipping the grip correction.
The transform remains idempotent and writes only280..292. Body, fingers, hair
and native local matrices are untouched. Wooden/dream0x52..0x55 remain excluded.
This addresses the reported transition flicker; live appearance remains to test.

## Dark Riku numbered previews

Passives101..104 provide the23 unused clips in the available main1160 bank.
The bank has31 clips;0/1/2/6/7/28/29/30 already supply Type D. The exact original
model/MSET match the previously admitted hashes. All2139 sampled mapped poses
across all31 clips pass the existing solver/map checks.

| Passive | Ground 1 / 2 / finisher | Air 1 / 2 / finisher |
| --- | --- | --- |
| 101 | 3 / 4 / 5 | 8 / 9 / 10 |
| 102 | 11 / 12 / 13 | 14 / 15 / 16 |
| 103 | 17 / 18 / 19 | 20 / 21 / 22 |
| 104 | 23 / 24 / 25 | 26 / 27 / 27 |

The last27 is explicit filler. These are pose previews, without guessed move
names, donor AI or donor hit/effect scripts. They use D's admitted map and
existing locomotion/jump/Guard routes with native Sora combo execution.
Main Type D's action assignments remain unchanged. Separate1580 source is not
included in this gallery. DARK_RIKU_TESTS.csv supplies source durations and IDs.

Both galleries are mutually exclusive with all stances and with each other.
Ventus66..100 remain unchanged; new Dark Riku101..104 are zero AP. IDs105..114
and127 remain visible and unassigned. Stance IDs, AP behavior and native48-byte
lists remain. Internal code14 selects a Dark Riku preview without a stance ID.
The settings marker migrates v65 while preserving its selected Ventus test;
old no-effect101..104 flags cannot autoactivate a new preview.

## Validation and limits

644 Rust tests/30 nonempty suites and160 final-PE checks pass (112 shared F/G/
menus,48 E). New PE checks cover half-distance travel under different tick sizes,
both banks, release/landing budgets, fixed facing, Circle lift/held Glide,
shortcut/script/damage rejection, cast recovery, event-schema rejection and
restoration, and all39 test choices. Pure checks cover second-pass scope,
actual-blade sweep coverage, duplicate contacts/restarts, first-pass finisher
reaction scope, grip fallback/idempotence, Dark Riku coverage and migration.

All190 previous original/Terra/variant payload parts, all35 existing Ventus
preview profiles and E's payload remain exact. Main G's38 bodies and4 action
variants satisfy the existing curve bounds: position <=5, basis <=0.12, segment
error <=0.01, zero native root-helper error. The shared payload explicitly admits
and restores only the four selected G contact-timestamp streams. The Windows
x64 DLL retains4 exports and8 imported DLLs.

The existing E motion hook forwards one post-update notification to Rust;
no duplicate actor hook or broad probe is installed. A PE check verifies its
original-first ordering, float delta, return value and single callback.

The PE harness executes the compiled C adapter with Windows APIs/rendering and
shared Rust dispatch substituted. Pure matrix/contact policy and the original
Dark Riku offline solver run locally. No actual Windows/game/GPU session or
live enemy contact is claimed. Check grip transitions, second-pass contacts,
dash damage, native defenses and action feel in game; TYPE G BLADE CONTACT logs
report native contact damage when the engine creates a record.

Sources: current user assignments/flicker report; delivered v65; original Ventus
capture, native Sora model/MSETs, main Dark Riku capture and supplied Steam Global
EXE; existing native contact and collision adapters. Source identity, bounds,
byte restoration and tested state routing are high-confidence offline findings.
Hit-window selection and the rendered transition fix remain provisional until
tested in game. Game assets/generated payloads stay outside Git.
