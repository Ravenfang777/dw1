# Styles v62 / s401: numbered slots and Sora-only Passives

## Result

All51 unused native IDs are now zero-AP test abilities whose names are their
decimal numbers:66 through115, followed by127. IDs1..65 keep their native
definitions and the eleven stance IDs116..126 keep their existing definitions.
No combat effects are assigned to the numbered entries yet.

Choosing Passives opens Sora's list directly inside Customize. There is no
Sora/Donald/Goofy/Shared selection screen. Sora's learned native abilities appear
first, followed by all51 numbered rows. The eight-row viewport uses the native
scrolling, scrollbar, cursor and confirm/cancel helpers. Confirm toggles the
selected ability; Back returns to the Customize categories and Back again to
the main menu. Stance, Passives, Limits and Outfits retain their order.

Normal Sora entries retain native names, descriptions, AP costs and the AP
budget. The page uses original native cost/free-AP queries, rejects equipping
when AP is insufficient, and permits removal. Numbered entries always show
AP0 and do not spend AP. This direct controller replaces v60's nested native
Abilities page and its member selector; it no longer opens native equip/sort
context dialogs. The custom controller toggles flags directly with native AP
queries and the existing snapshot-checked commit.

## Capacity and persistence

The numbered entries are displayed from a separate catalogue and use a51-bit
test flag registry. They are not appended to Sora's48-byte learned array or
stored in another party member's array. The page supports up to99 rows:
48 existing Sora entries plus51 numbered entries. Existing full arrays can
toggle native flags without allocating a new token or writing the next field;
new stance insertion retains its prior free-space/terminator requirement.

Test selections are saved in kh1-numbered-abilities.ini beside the executable.
They are mod-wide settings shared between game saves. All numbered entries
start unequipped if that file is absent or invalid. Deleting the file while
the game is closed resets the test selections. A change writes a temporary
file and renames it into place; unchanged frames perform no settings write.
Native abilities and the stance continue to use their normal save storage.

Existing numbered IDs found in Sora's learned array are compacted out. Enabled
copies enable the corresponding test flag; disabled copies do not clear an
already selected mod-wide flag. The first and last IDs and duplicate copies
are bounded explicitly. These virtual flags are returned by the native equipped
ability counter for Sora, without depending on available learned-list space.

## Other party members

While enabled, the mod reports no equipped abilities for native member IDs1..9
and clears each member's48-byte learned-ability array. This includes inactive
partners as well as the current party. Newly awarded copies are suppressed
immediately by the query hook and removed on the next game-thread update.
Only those arrays are cleared; HP/MP, experience, equipment, items, AI/customize
settings and other save fields are retained. Basic commands/spells are not
deleted as a separate feature.

This removal persists when the game is saved. Uninstall does not reconstruct
deleted partner abilities. The request explicitly authorizes their removal;
there is no hidden transfer of those slots to Sora or to the numbered registry.

The seven v61 built-ins remain: Scan, Guard, Dodge Roll, High Jump, Mermaid
Kick, Glide and Superglide without AP or learned slots. Native action/room
restrictions and stance-specific movement replacements still apply. Shared
movement is a Sora capability rather than a partner ability row in this menu.

## Implementation, sources and confidence

Primary sources: the user's exact request; delivered v61 source; the supplied
Steam Global executable, timestamp1721645006. The native ID/list boundaries
are documented and tested in styles-v61.md. No new capacity is inferred merely
from an eight-row viewport or a failed allocation.

- Rust table construction fills only IDs66..115/127 from a native template,
  with AP0 and separately encoded numeric names/help handles. Native1..65 and
  all stance records are byte-for-byte preserved by the extension.
- The direct Passives page uses native definition lookup0x28f8f0, cost0x2e8120,
  free AP0x2e8660, handle decode0x38adc0 and the previously admitted native
  row, AP panel, text, clipping, paging, focus and input helpers. Their entry
  signatures join the coupled read-only admission before menu publication.
  The root menu already calls stat-cache builder0x2e7ec0 at0x2db082, filling
  the per-member cache containing Sora's maximum AP at0x2e942c4; that cache
  does not depend on first opening the removed member-selection screen.
- Choosing Passives switches this page's controller to Sora's filtered shadow
  plus the separate numeric catalogue. It creates no native member-selection
  child. The header switches to Passives and returns to Customize on Back.
- Normal native flag writes retain snapshot/identity checks, duplicate records
  and the hidden stance token. Existing full48-byte arrays are read within
  bounds and can update flags without adding records; new style insertion
  still refuses when space is unavailable.
- The admitted native counter's fallback remains intact. Its override handles
  numbered Sora flags and suppresses member1..9. The game-thread update verifies
  Sora, Shared and all nine partner snapshots before committing any array
  changes. The numbered settings callback runs after those writes.
- The registry is intentionally test configuration, not an invented extension
  of KH1's on-disk save format. Native definition IDs still stop at127 and
  native physical learned arrays remain48 bytes.

Confidence is high for the local ABI, bounded native queries and offline
execution. GPU output, actual Windows file replacement, menu focus and gameplay
still need live verification. No original game data or disassembly is committed.

## Uninstall and retained behavior

Use the included explicit remove_dual_wield path before disabling or reverting
the mod. Numbered flags stop overriding native queries and are not inserted into
the KH1 save. The settings file can be retained for later testing or deleted.
The prior built-in restoration path remains, subject to free native capacity;
Sora's three ordinary entries return unequipped and shared movement equipped.
Cleared partner arrays stay cleared. Both generated animation payloads and
E/F combat/action controllers are unchanged.

## Validation

- 631 Rust tests pass across30 nonempty suites, including all51 ID mappings,
  preservation of native/style definition records, zero AP, atomic refusal of
  missing text handles and settings parse/format boundaries.
- Windows x64 builds with4 exports and8 imported DLLs.
- 137 final-PE checks pass:90 F/menu/ability checks and47 E regressions.
- All51 numbered rows are discovered by scrolling. All51 can be enabled and
  disabled at zero available AP alongside a full48-entry native list, with
  no writes to that native list. The highest registry bit is exercised.
- Original native paging reaches127 beyond the48-entry boundary. Tests cover
  direct Sora entry/no member child, cancel/reopen, native names/help, real
  native AP queries, insufficient-AP refusal and existing full-list flag edits.
- Every partner array is checked for removal with all surrounding save bytes
  preserved. Reawards are blocked before cleanup, and tests confirm the
  uninstall behavior and intentional mod-wide test state across save changes.
- C registry initialization, migration and persistence callback payloads run
  from the final PE; the Windows file-write callback is substituted in that
  harness. Rust tests exercise its serialization. Final Windows filesystem
  replacement and live game rendering are not claimed as executed.

Earlier native equip/remove dialog checks remain as regression/reference tests;
they do not imply that the new direct Passives view opens those dialogs.
All prior Stance, built-in, E/F movement, magic and source-admission checks pass.
