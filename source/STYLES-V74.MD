# Styles v74 / s413: native Overdrive continuity and color tuning

## Blue and purple

Control is now brighter blue #0055FF, replacing #00008B. Will is deeper purple
#400060, replacing #800080. Other seven colors, all names/Drain values and exact
future descriptions remain. No gameplay bonus or Drain deduction is added.

Palette3 upgrades these two known version2 default values only. Other colors
and explicit custom version2 values remain. The next menu selection save
persists version3 and corrected defaults; older pre-version2 files still
upgrade to the complete current set. No settings reset/INI deletion is needed.
Later version3 custom values persist. Source: user feedback/current migration.
Confidence high for selective migration; the RGB shades are calibrated choices
and final glow brightness needs the user's in-game comparison.

## No stance equipped

The received 20.16-second video shows effects with a stance, then intermittent
effects after it is removed while stock Sora changes moves. v73 requires an
animation-pass pose witness no older than two physics ticks. Stock Sora may
reuse cached skeleton state; the witness can expire or unskinned helper joints
can be unsuitable during transitions. Extending the timeout would allow stale
hand placement.

For no-stance Sora only, the existing actual field-model draw callback now
publishes an effect pose from native parent-local matrices. Reconstruct the
model-space hierarchy, including hand helpers, instead of reading a possibly
skinned full draw palette. Use the last admitted external placement axes and
current actor translation. Keep exact actor/instance/generation, pointer/bone
count and finite checks, plus base-rig inverse/wrist/palm alignment. Publish at
most once per physics frame. The log marker OVERDRIVE NATIVE DRAW READY confirms
that this publisher ran.

No native local/world body matrix is changed. Equipped stances keep their
existing witness path. v73's draw-time root refresh still uses the newest
captured pose without advancing effect clocks/particle history. Two-tick draw
admission stays; actual native submission refreshes its input. Sources: user
video, native local-matrix schema and actual submission callback. Confidence
high for hierarchy/call placement and write isolation; moderate for live
diagnosis/repair. No Windows/game/GPU session was executed here.

Test stock idle/walk/run/attacks/jumps and transitions, then equip/unequip styles
with an Overdrive active. Final continuity remains a live check.

## Keyblade effect inventory

See keyblade-effect-candidates.md and package KEYBLADE_EFFECTS.txt/CSV. KH1
trails/sparks and KH2 flashes/glows/ribbons have established mappings/visual
paths. BBS captures include Aqua Keyblade attachment references and a scene
FEP, but no validated BBS playback/conversion route. The catalogue separates
references, payload availability, partial support and observed visuals. It
introduces no new demo selector or automatic cycle. Sources/confidence are
recorded per group; no original effect payload enters Git.

## Validation and retained scope

662 Rust checks/30 nonempty suites and 172 final-PE adapter checks pass
(123 shared,49 E). Checks cover selective palette2/3
migration, custom colors/IDs and local-pose reconstruction through cached draws,
blended transitions, malformed hierarchies and non-finite inputs. Delivery
receipts include final native adapter counts, Windows x64 exports/imports,
full74-commit reconstruction, source inventory and ZIP/file hashes.

Both private generated headers remain byte exact to v73. Footsteps stay muted;
Customize/Appearance/AP behavior, combat, contacts, animation mappings and all
movement rules remain. PE checks use Win64 ABI/API mocks and do not execute
the Rust field-draw callback or GPU. Final color/continuity needs game testing.
