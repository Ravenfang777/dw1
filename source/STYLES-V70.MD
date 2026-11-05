# Styles v70 / s409: body dashes, movement tuning and Overdrives

## Type F dash contacts

The user confirmed330 movement but no damage. Inspection found that v69 added
F to the contact coordinator but its actual registered post-motion caller still
admitted only the Ventus body lane. The caller now dispatches both main F/G;
the portable regression executes that exact callback, not just its callee.

F air dash330 and ground dash/Dodge Roll009 (native DC, ground state0) now use a
body-sized area instead of weapon reach. A radius30, half-height60 column is
centered60 above Sora's feet, covering0..120 above them. Dense columns sweep
between physics samples at no more than20-unit intervals; reject non-finite
samples and movements over600 as discontinuities. This catches front, sides,
rear and targets crossed between frames without becoming a room-wide attack.

Use the existing native physical damage/defense/contact path and one successful
contact per enemy per dash. Failed native contacts may retry. Ground uses the
native ordinary ground attack data; air uses ordinary aerial attack data. F
ordinary combos and G's original blade contacts/two-pass attacks remain.

Sources: user report/request, actual registered callback and native contact
implementation. Confidence high for dispatch/geometry/write scope; finalized
enemy HP loss and enemy-specific defenses require game testing.

## Requested animation and movement changes

| Change | v70 behavior |
| --- | --- |
| E ground combo2, both native variants |85% of v69 animation rate |
| E grounded Cure |318, previously the air Cure pose |
| E aerial Cure |427, previously the ground Cure pose |
| E Circle dodge horizontal reach |85%:464.1 vs546 full-stick native units |
| E Circle dodge lift/timing |29.25 lift and26-tick movement retained |
| A/C/L? Circle dodge visual |85% of previous visual rate; movement clock/travel unchanged |
| K? aerial dodge |Removed from the host action policy |

The user gave no rate for A/C/L?;15% is the stated working assumption. Their
visual sampling is now0.75*0.85 of the controller clock. E's two GC2 rates are
(47/24)*0.85 and(63/24)*0.85. Native events continue to follow that slower clock.
No extra held recovery frames are introduced.

Cure poses are refitted from the two immutable serialized conversions into
the other native record's existing capacities. Keep target headers, events,
request tables, travel, spell mechanics, MP, effects and origins unchanged.
Ground56 takes81's318 pose; air81 takes56's427 pose. No physical slot or native
spell action is exchanged. Regeneration: single_e/swap_cure.py followed by the
existing generator; private fixtures remain outside Git.

Sources: user request, existing native adapters and converted poses. Confidence
high for ratios, source mapping and verified bounds. Curve fit errors and live
visual limitations are recorded with the supplied validation.

## Independent Overdrives

Customize categories are Stance, Passives, Overdrives, Outfits. Overdrives has
five virtual zero-AP rows; confirming an equipped row turns it off, confirming
another replaces it. Selection is one value, independent of stance and numbered
test settings. No native learned slots or ability IDs are consumed. Existing
AP Used/max display remains. Persist in kh1-overdrive.ini beside the existing
mod settings; removal mode returns no active Overdrive.

| Overdrive | Effect donor |
| --- | --- |
| Strength |KH2 Valor |
| Will |KH2 Wisdom |
| Resistance |KH2 Master |
| Prowess |KH2 Final |
| Rage |KH2 Anti |

This version adds visual effects only. No power, defense, movement, magic,
command, gauge, ability or AP boost is assigned.

Load each donor's own effect archive through the existing isolated particle
renderer. Prefer authored idle/arrival bound body loops; otherwise consider
persistent body loops in that same archive. If no loop exists, repeat only
finite body-bound idle/arrival glows after they finish. Weapon-point effects,
free projectiles, screen flashes and attack-motion bursts are excluded. Rage
uses exactly the existing Anti aura selection. M? plus Rage reuses M?'s aura
rather than layering an identical duplicate.

Auras follow the actual current native field palette mapped onto the base KH2
body; they do not depend on a stale imported-pose cache. This supports native
E/F/G, other stances and normal Sora. Selection/binding changes clear owned
particles; pause/menu/resource gates and bounded effect/draw budgets remain.
The effects never run the donor's gameplay script, damage or form controller.

Sources: the existing Anti darkness renderer, form archives loaded on the user's
installation, and requested donor mapping. Confidence high for menu/state,
resource ownership and cosmetic separation. The actual form assets are loaded
on the user's PC; no Windows/GPU execution or live visibility test occurs here.
A missing archive or suitable bound body effect is logged as unavailable while
leaving the stance/gameplay intact; no substitute effect is invented.

## Validation

- 650 Rust checks in30 nonempty suites pass. They include the actual registered
 F/G post-motion callback, first/second G pass deduplication, F ground/air body
 routing and restart, swept body geometry, A/C/L visual policy/K removal,
 Overdrive donor selection/configuration and body-effect filters.
- 122 shared final-PE checks and48 E final-PE checks pass. Exercise the five
 Overdrive names/AP0/selection/removal/persist callbacks and independent Stance
 changes without save/slot writes; E GC2 rates/shorter travel; existing F/G
 travel/controls, menus, AP and safe body admission/restoration.
- All shared F/G payloads remain byte exact. E changes only the body curves/
 descriptors for Cure56/81; all original parts, native request tables, event
 payloads, Dodge504 and Blizzard variants stay exact. Cure refit maximum pose
 position error is0.402 native units; detailed receipts are included.
- Windows x64 release builds with4 public exports/8 imported DLLs. Full source
 reconstruction and archive/file hash checks complete the delivery.

The portable coordinator substitutes native collision/final damage and the PE
harness substitutes Windows/rendering/shared Rust startup. Form archive parsing
is implemented, with selections logged on the user's installation; actual form
particles and GPU appearance are not observed here. Test body damage against
reachable enemies and cycle all five Overdrives on native and imported stances.
