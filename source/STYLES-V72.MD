# Styles v72 / s411: lighter Overdrive effects and Customize labels

## Overdrive effect selection

The user wants Wisdom's swirling wind retained, with its foot sparkles and
the shared Anti darkness removed. Keep two cloned Overdrive packages: Valor
and Wisdom. Remove Anti from the shared package list entirely, rather than
merely changing its color or leaving invisible running handles.

The received v70 log, carried forward in the v71 implementation, admits Wisdom
elements11/12/100. Exclude the paired11/12 foot emitters from the shared Wisdom
selector; retain100, the remaining wind/body effect. Apply the filter after
the existing authored body-aura admission, without broadening its fallback to
other attacks, projectiles or motion effects. Valor selection remains intact.
All five Overdrives use this same reduced set with the existing colors.

The ordinary Anti/Wisdom stance and attack-effect packages are separate from
these clones. Do not remove their original resources or gameplay effects.
While an Overdrive is active, Type M?'s ordinary idle darkness remains
suspended so it cannot reintroduce the removed shared darkness. When that
Overdrive is disabled, the normal stance aura follows its existing policy.

Sources: user visual feedback/request, witnessed Wisdom element list in the
received log, existing selector/renderer and docs/kh2-effects.md. Confidence
high for the exact excluded IDs, absent Anti shared layer, ownership and
retained policy; the wind-versus-foot visual identification is a targeted
interpretation of the three admitted Wisdom effects, not a fresh asset/GPU
inspection. The actual donor archives are on the user's installation, so
confirm wind remains and foot sparkles are absent in game.

## Customize header and names

The native header message0x6B previously returned a Passives-specific buffer
when the Passives picker was active. Native header caching can retain that
string after changing categories. Return the same Customize buffer for the
entire active Customize page, including the Passives selection window. The
category/ability descriptions remain unchanged and Shortcuts keeps its own
message lookup. Native messages outside Customize still use the original table.

| Previous label | New label | State retained |
| --- | --- | --- |
| Outfits | Appearance | Category3; empty/reserved entries |
| Prowess | Brilliance | Overdrive ID4; default white; existing selection |

The category order is Stance, Passives, Overdrives, Appearance. This is a name
change; no appearance options or new equip behavior are added. Colors remain
Power red, Will blue, Resistance yellow, Brilliance white, Rage black.

Use brilliance_color in kh1-overdrive.ini. Existing prowess_color values are
read as an alias, and a canonical brilliance_color is appended when a menu
selection is saved. An explicit brilliance_color takes precedence. Keep the
old key/unknown settings and saved selection ID; no user settings reset is
needed. The existing strength_color alias remains supported as well.

Sources: user report/request and the actual native message/menu callback path.
Confidence high for fixed string identity, category/name/state mappings and
config migration; final native header caching/font fit need a game check.

## Overdrive Drain panels

Remove only the Overdrives AP Used/current/max footer. Passives retains its
live native AP display and ability-cost behavior. In every Overdrive row,
replace AP0 with Drain in the existing native AP panel at x327, then draw a
second identical panel at x373 showing5. Both use the same y/palette/size and
the native glyph-width query for centered text. Other metadata retains its
existing alignment policy.

5 is a fixed display value for the user's next testing phase. It does not
subtract AP, HP, MP or any other resource and does not assign a drain function.
The Overdrive choice remains free/exclusive and independent of Stance.
Sources: user steering and existing native AP-box drawing/width helpers.
Confidence high for routing, dimensions, centering policy and display-only
scope; final font/panel appearance remains a live game check.

## Retained scope and validation

656 Rust tests across30 nonempty suites,122 shared final-PE checks and49 E
final-PE checks pass. Windows x64 release retains4 exports/8 imported DLLs.

No combat controller, animation mapping/body/event, movement, contact geometry,
AP/ability slot or save behavior changes. v71 Type E jump/GC2 tuning and
Overdrive pose/hand anchors, color masks and bounded particles remain.
Both private generated headers stay byte exact to v71.

- Rust checks cover the reduced Wisdom selector, absence of a shared Anti
 layer, all five shared selections, palette persistence and legacy Prowess
 color migration with canonical precedence.
- The final shared PE harness visits Passives, Stance, Overdrives, Appearance
 and Passives again, checking that each returns the same Customize pointer.
 It verifies Brilliance/exclusive selection, ten matching Drain/5 panels,
 centered5 glyphs, absent Overdrive AP Used and unchanged live Passives AP.
 Existing menu/stance behaviors and E's final-PE checks are retained.
- Delivery receipts record exact counts, Windows x64 release export/import
 checks, full72-commit source reconstruction and ZIP/file hashes.

The native adapters execute under Win64 ABI/API mocks; Rust startup/rendering
and GPU submission are substituted. No Windows/game/GPU session was executed
here. In game, verify the reduced wind/hand effects in each color and the red
Customize header after entering Passives and returning to other categories.
