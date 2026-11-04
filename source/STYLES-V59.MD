# Styles v59 / s398: Customize stance menu

The user replaces the v58 three-slot proposal with an Abilities-style Customize
page matching the attached layout reference. Main-menu order becomes Items,
Customize, Equipment, Abilities, Shortcuts, followed by the remaining native
options. The old native Customize functionality is only relabeled Shortcuts.

## Categories and interaction

The left column contains Stance, Limit, Outfit and ???. Opening Customize
focuses the category column with Stance selected and its entries previewed.
Confirm Stance to enter the right-hand list. Confirm an unequipped type to
select it exclusively; confirm the equipped type again to turn the stance off.
Cancel returns to the categories; cancel there returns to the party menu.
Limit, Outfit and ??? have no entries/effects yet. They do not expose stances.

The right list retains eight visible native-height rows, original Abilities
scrolling and scrollbar, rounded row graphics, native equipped marker, clipping,
and confirmation/cancel settings. The name column is166 pixels; adjacent
weapon and magic information boxes are both52 pixels wide and use the same
row height. Native height26/gap2 produce the reference's eight-row layout.
The first new-page callback ignores the entry press to avoid double selection.

## Stance labels

| Previous label | New label | Saved ID | Weapons | Magic |
| --- | --- | --- | --- | --- |
| Single A | Type A | 124 | Single | I |
| Single B | Type B | 123 | Single | I |
| Single C | Type C | 120 | Single | I |
| Single D | Type D | 119 | Single | I |
| Single E | Type E | 117 | Single | I |
| Single F | Type F | 116 | Single | I |
| Dual A | Type H? | 126 | Dual | I |
| Dual B | Type I? | 125 | Dual | I |
| Dual C | Type K? | 121 | Dual | I |
| Dual D | Type L? | 118 | Dual | I |
| Anti | Type M? | 122 | None | 0 |

The question marks are intentional labels. Weapon labels report stance weapon
count. Magic uses0 for unavailable, I for KH1 and II for KH2. All current armed
stances still execute KH1 magic; imported KH2 spell poses/effects are visual.
Type M? retains its existing magic restriction. The II label is supported for a
future KH2-magic stance; this menu revision does not replace spell controllers.

## Persistence and retained behavior

The existing single hidden style token stores the stance; renamed labels do not
change IDs or AP. Native abilities, equip flags and other-party records/AP are
preserved. No native equipment, shortcut assignments or inventory records are
repurposed. Empty categories do not claim save fields. Normal Abilities remains
functional and hides the custom stance entries. Its AP cost and totals remain.
All v58 combat behavior remains, including Type F's fixed-facing, once-per-airtime
air dash and L1/LB shortcut exclusion. Both private payload headers are unchanged.

## Sources, validation and live limits

Sources are the user's mockup/request, v58 source, and the supplied Steam Global
executable. The native row/font geometry, palette, glyph, paging and title paths
are primary local evidence. All helper entries and coupled menu anchors are
checked before publication; a mismatch leaves the native menu unmodified.

The Windows x64 DLL builds and the release passes627 Rust tests in30 nonempty
suites plus104 final-PE checks (57 F/menu,47 E). Tests cover exact renamed IDs,
root order and remembered cursor IDs, title/Shortcuts routing with unchanged
native callback, all eleven types and matching metadata boxes, fixed-point
scroll preservation, exclusive selection/unequip, empty categories, swapped
buttons, cancellation, full/malformed save refusal, native abilities/AP and
all prior E/F action regressions. Original native page-scroll code reaches the
last entries and wraps back, with mouse/sound/cursor-animation tails substituted.
Original native index, offset, confirm, normalization and close routines execute.

Rendering, Windows startup and shared Rust dispatch are mocked. The GPU's final
appearance, focus transitions and controller feel still need an in-game check;
the supplied image is a reference, not proof that this build was run in-game.
Source, hashes and reproducible-input details are included in the package.
