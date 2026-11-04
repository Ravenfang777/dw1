# Styles v61 / s400: seven built-in abilities and native capacity findings

## Result

Scan, Dodge Roll, Guard, High Jump, Mermaid Kick, Glide and Superglide are
available while the mod runs, independently of the selected stance and without
equipping them. They consume neither AP nor learned-list entries. Existing
stance replacements still control the actions they replace: for example, a
stance's aerial dodge continues to replace its designated native glide action.
This does not make Sora guard automatically, glide while grounded, or ignore
native room, swimming, action or shortcut restrictions.

Sora's existing Scan/Guard/Dodge Roll entries are removed from his learned list;
the four shared movement entries are removed from the shared list. Their native
definitions remain unchanged. Other party members' entries and AP stay native.
Duplicate unrelated abilities and their equip flags are preserved. No new
ability IDs are consumed by this feature.

## Capacity: three different numbers

| Boundary | Verified value | Meaning |
| --- | --- | --- |
| Stock ability definitions | 65 | The stock table contains65 records of12 bytes. It can be relocated and extended;65 is not a fixed engine-wide skill limit. |
| Native ID encoding | 1..127 | Each saved byte uses7 bits for the ID and bit7 for unequipped. There are62 representable IDs above the stock65. The eleven styles use116..126, leaving51 representable unused IDs in this isolated package. |
| Native learned-list storage | 48 bytes per member, plus a separate48-byte shared list | Each copy occupies one byte. Native append code stops after48 entries. Enlarging only the definition table does not enlarge these arrays. |
| Current Styles safe list policy | 47 entries including the hidden stance token | A zero terminator stays inside the48-byte array. With one stance token,46 ordinary Sora entries fit. A47-entry native-only list without a token may still toggle native entries. |

The seven built-ins free up to three Sora entries and four shared entries when
they were present. The freed shared entries do not increase Sora's array size.
This revision does not enlarge the native lists or implement additional unnamed
passives. More definitions can be added within the unused IDs. Going beyond the
native learned-list capacity requires separate persisted storage and routing
for lookup, learning, menu selection, AP and save loading; going above127 also
requires a new ID representation. Those are feasible mod changes, not a safe
single-number patch or functionality already delivered here.

The representable ID count is a format boundary, not a promise that filling all
unused records with unimplemented definitions creates usable abilities. Each
new skill still needs a name, help text, behavior and persistence policy.

## Implementation and sources

Primary sources: the user's requested ability set; current v60 source and local
Steam Global executable, timestamp1721645006. Native counter0x284be0 counts
exact equipped bytes in member0's save+0x44 list or the shared save+0x599 list
for member arguments above9. Its complete75-byte leaf is checked with a64-bit
FNV-1a fingerprint before publication. A private copy replaces its single
RIP-relative save-pointer load with an absolute load; all remaining branches
are internal and unchanged. The fallback retains native counts for every other
ability/member, including duplicate abilities and unequipped bytes.

The scoped override reports one equipped copy for these exact queries:

| Ability | Native ID | List/member |
| --- | --- | --- |
| Guard | 21 | Sora/member0 |
| Dodge Roll | 22 | Sora/member0 |
| Scan | 26 | Sora/member0 |
| High Jump | 1 | Shared/member above9, normally11 |
| Mermaid Kick | 2 | Shared/member above9, normally11 |
| Glide | 3 | Shared/member above9, normally11 |
| Superglide | 4 | Shared/member above9, normally11 |

The override requires a readable valid Sora save. It does not edit the native
AP table or OR cached action bits over the native builder. Native builder
0x2a6380 derives Guard/Roll, shared movement and per-actor Scan flags from the
same counter, preserving its own room/action restrictions and High Jump stat
handling. Native AP function0x2e8660 totals only the remaining equipped entries.

The game-thread update checks both arrays within their48-byte bounds, compacts
only the requested entries and verifies the save identity and both snapshots
again before writing. It handles a full48-entry array when compaction can free
space, rejects gaps followed by nonzero data, and never changes the following
save field. New copies awarded later are compacted on the next update. The
update runs before the existing stance-shadow normalization.

Native append0x284e10 and menu constructor0x311850 bound both arrays at48.
Save initialization0x285481 clears48 bytes at+0x599. Definition lookup
0x28f8f0 strips bit7 and indexes12-byte records; enabled127 and disabled255
resolve to the same last representable definition. These are primary native
evidence for the capacity numbers above, rather than limits inferred from a
failed test or the visible menu's eight-row viewport.

Confidence is high for the local ABI, capacities, scoped behavior, AP and
offline native-code execution. Windows startup, GPU output and actual gameplay
remain untested. No executable, extracted table or disassembly is committed.

## Uninstall

The existing explicit remove_dual_wield option disables the virtual grants.
After removing the stance token, it restores missing normal entries where space
permits. Sora's three entries are learned but off, preserving the AP budget;
the four shared movement entries are on and have no AP cost. Existing copies
keep their flags. No unrelated ability is evicted if a list has filled since
these slots were reclaimed; a bounded log explains any restoration shortfall.
Uninstalling cannot put more entries into the native array than it can hold.

## Validation

- 627 Rust tests pass across30 nonempty suites.
- Windows x64 release builds with the usual4 exports and8 imported DLLs.
- 125 final-PE checks pass:78 F/menu/built-in checks and47 E regressions.
- New checks execute the original append function at the48th and49th attempt
  for both arrays, and the original definition lookup for IDs127/255.
- The installed counter and relocated original leaf run for all seven grants,
  other party members, duplicate native counts and unrelated shared abilities.
- Original native AP accounting refunds only Sora's three built-ins. Original
  cache construction derives the expected movement/defense bits and honors its
  restriction branch. The original Scan cache block sets the native actor flag.
- Additional cases cover boundary bytes, malformed/full lists, failed byte
  admission/allocation/protection with no save changes, save identity changes,
  reawarded copies, uninstall capacity and the nested Passives/stance menu.
- Existing menu, E/F action, dash, collision and source-admission regressions
  continue to pass. Both animation payloads and action controllers are unchanged.

The harness executes native C adapter code from the final PE with Win64 ABI
substitutes for Windows APIs and shared Rust dispatch. Native cache/AP excerpts
execute as described above. Final in-game controls, story transitions, movement
and HUD rendering still need a game test; these checks are not a live game run.
