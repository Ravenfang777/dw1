# Styles v64 / s403: readable footer and Ventus Type G

## Footer

The supplied v63 screenshot shows help at the divider instead of its normal
inset, a large gap before the next line, and a small gray AP total at the bottom
edge. Native help messages can carry leading, font, color and position commands;
passing their layout through the custom footer made that spacing inappropriate.

The description now starts at x174/y309 and wraps by measured native glyph width
within226 units. It draws up to three16-unit lines at y309/327/345, each as a
separate native text call. Layout/style commands are consumed with their full
operands and normalized in the footer copy. Button/extended glyph tokens remain
whole; long descriptions end in an ellipsis. The source message is not modified.

Passives and Limits have a separate right footer column: a white AP Used label
at x414/y310, font16, and spent/max at x414/y333, font22. Very long totals reduce
their font only enough to fit98 units. Both use native full-white0x80ffffff.
Their AP calculation and native equip/cost checks are unchanged. Stance and
Outfits retain no AP budget. Limits remains empty and uses Sora's shared budget.

The only new native helper reference is width measurement0x2d0e10. Its entry
joins the coupled menu admission before any callback/table publication. The
native glyph helper remains0x2ebcd0; no blue frame or duplicate pill is added.

## Ventus

The returned Ventus_Source_Capture_20261104_040031_281eba.zip contains the
original53-bone p01ex00 model and non-event animation banks. They now supply
Type G, a zero-AP Single/I stance between Type F and Type H?. It uses ID115 and
runtime code12. All previous stance IDs/codes and their save meaning remain.

The initial native-body profile contains37 mapped records, including ground
300/301/302, air305/306/307, Guard400 and Dodge Roll009, locomotion, jumps,
ledge movement, items and casting. Its full mapping and source frame counts are
recorded in single-g.md and the package's VENTUS_ANIMATIONS.csv.

Type G retains KH1 action selection, hit/defense/item/spell events, timing,
collision, travel and damage reactions. Body poses are fitted into the existing
native durations. Native Glide and Superglide remain. Terra's Square dash and
spell-recovery variants are confined to profile1; Ventus is profile2. The shared
adapter restores native data at idle before publishing another stance.

ID115 replaces its previous numeric test placeholder. The50 remaining numeric
entries are66..114 and127. Old registry bit49, formerly115, is ignored and cannot
equip Type G. ID127 remains at bit50; other numeric settings do not shift. The
native definition table still stops at127 and learned arrays remain48 bytes.
One hidden stance token still requires free native capacity to be inserted.

All seven built-ins and the requested removal of partner ability arrays remain.
All190 before/Terra/variant part payloads, including the native dash descriptor,
are byte-identical to v63; the common descriptor now also holds Ventus bodies.
Single E's payload and E/F action controllers are unchanged.

## Validation and limits

632 Rust tests pass across30 nonempty suites. The Windows x64 DLL builds with
the existing4 exports and8 imported DLLs.145 final-PE checks pass:98 F/G/menu/
ability checks and47 E regressions.

New checks cover measured help lines, consumption of native command operands,
fixed footer positions, ellipsis/width limits and the white16/22 AP draw calls.
They retain the prior AP toggle/zero-budget tests. All12 stances and50 numeric
entries are exercised, including original native paging beyond the viewport,
Type G selection, ID115 retirement and stable ID127 settings.

Every mapped G body is compared with its converted fixture and restored in both
normal/Olympus banks, using serialized and relocated pointer fields. Tests check
F dash cancellation/lease restoration before G, G's ordinary Square/movement,
native Glide/Superglide eligibility and a return to F. Existing E/F regressions
pass. Conversion samples have maximum positional error2.445 Sora model units,
basis error0.050, segment-length error below4.1e-11, zero scale error and zero
native root-helper error. These are fitting bounds, not proof of rendered mesh
clearance or contact alignment in gameplay.

Sources are the user's request/screenshot/capture, delivered v63, the supplied
Steam Global executable and the previous original Terra retarget tooling. Source
rig and native byte/capacity admission are high-confidence offline findings.
The action assignments are an initial playable test mapping. Mesh/hair/weapon
alignment, attack contact feel, Guard/roll timing, GPU output, Windows startup
and live stance switching need the user's game test. The harness substitutes
Windows APIs, most drawing/navigation and shared Rust dispatch; it does not run
the game. No original models, archives, dumps or generated payloads enter Git.
