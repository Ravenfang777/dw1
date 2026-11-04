# Styles v60 / s399: Passives and native metadata panels

## Result

The main menu now begins Items, Customize, Equipment, Shortcuts. Abilities is
removed from that list; a remembered Abilities selection resolves to Customize.
Customize contains Stance, Passives, Limits and Outfits, in that order. Existing
stance names, saved IDs and weapon/magic meanings remain as documented in v59.
Limits and Outfits are empty reserves.

Passives opens the complete native Abilities menu under Customize, initially
selecting Sora. It retains native scrolling, descriptions, equip/remove dialogs,
AP costs and totals, and the normal party/shared selectors. Custom stance tokens
are filtered from Sora's list. Back returns to the Customize categories, with
the stance and normal ability flags preserved. This uses the original ability
controller rather than a separate implementation of its AP rules.

The header displays Customize, then Passives inside the native submenu. Native
Customize remains visually labeled Shortcuts with its original callback.

## Metadata correction

The supplied v59 screenshot exposed an incorrect helper classification:
0x2f3a80 draws a blue framed shape, and the supposed text helper 0x2d7770 also
draws a capsule via its wrappers. Combining them produced the offset second
background and bright border. Earlier v59 notes describe the intended geometry,
not the actual native output; this finding supersedes that classification.

Weapon/magic metadata now uses the actual native AP panel renderer 0x2f2430,
followed by glyph-only text 0x2ebcd0. There is one panel per value. Both panels
use the native width42, height22 and font12; their x positions are327 and373.
They are centered within the native26-pixel row with2-pixel row gaps. Background
and text palettes follow their stance row. No blue-frame or capsule text wrapper
is used for these two columns.

## Native page ownership and saves

The native window factory 0x2e5a40 enforces uniqueness for page definitions
whose flags include4. Customize therefore receives a private copy of the native
full-page definition, with its own callback. The original Abilities definition
0x5490f0 remains available to its unchanged constructor 0x311850. Native linking
helpers 0x2e2de0/0x2e2e40 connect the new page to its parent.

While Passives is live, its child page owns the native return-chain global
0x2e9cb70. Closing it marks only that chain; native engine cleanup owns unlinking
and freeing windows. Customize resumes after observing the child close. Restore
the prior return pointer only while it still identifies our child, then rebuild
the stance shadow view. The custom parent does not paint over the native child.

Sora's native record is still presented through the existing filtered shadow
and snapshot-checked commit. A completely full47-entry native list with no style
token may still equip/remove its native entries; this does not allocate a style
token or evict an ability. Selecting a new stance still refuses when there is
no spare token slot. Equipment, inventory, shortcut assignments and AP are not
used as new storage. Limits and Outfits do not allocate save records.

The actual Abilities header message is0x6b, as used by native root-entry callback
0x311810. The previous alias targeted ability-help message0xbd; that help message
now follows its normal native path. Header substitution is scoped to custom
root ID8 and its owned Customize/Passives pages.

## Sources and confidence

Primary sources: the user's two comparison screenshots and requested order;
delivered v59 source; the supplied Steam Global executable, timestamp1721645006.
Native AP panel geometry, text ABI, window factory/constructor, definition flags,
header message and equip/remove decisions were checked against local native
code. Confidence is high for those findings and offline execution. No original
executable, extracted table or disassembly is committed or shipped as source.

All coupled menu destinations and admitted helper entries are verified before
publication. An anchor or protection failure leaves the native menu unchanged.
Combat/action sources and both generated animation payload headers are unchanged.

## Validation and limits

- Windows x64 release builds with4 exports and8 imported DLLs.
- 627 Rust tests pass across30 nonempty suites.
- 109 final-PE checks pass:62 F/menu and47 E regressions.
- New checks execute the original window factory and Abilities constructor,
  create distinct nested page definitions, preserve hidden stance flags, return
  to Customize, and reopen Passives. Native cleanup is simulated after close.
- The complete native equip/remove callback executes for allowed equip,
  insufficient-AP rejection and removal. Its budget-availability flag is an
  input; no replacement AP policy is substituted.
- The original AP renderer emits draw packets with the expected42x22 geometry
  and row positions, including the clipped ninth scroll row. The first packet
  matches a direct native AP-panel call byte for byte. GPU allocation/submission
  and fade color are substitutes; this does not execute a Windows GPU renderer.
- Existing original native paging, focus, index, confirm and close checks,
  root selection mapping, empty reserves, full-save refusal, and E/F combat
  regressions continue to pass.

Windows startup, shared Rust dispatch, most menu drawing and native engine
cleanup are harness substitutes. Actual in-game graphics, focus transitions and
controller feel still need verification. The supplied screenshots show v59,
not an in-game run of this build.
