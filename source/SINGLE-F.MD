# Single F and the native Styles menu — v54 / s393

Single F is the user's tested Terra v4 main profile, integrated into the existing
Styles DLL. Ability ID116 and runtime code11 are new. The other ten saved IDs
and all65 native ability definitions remain unchanged. No numbered Terra test
profiles, Drive states, second weapon or KH2 controller are added to this lane.

| Action | BBS Terra source |
|---|---|
| Ground combo | 300 / 411 / 332 |
| Air combo | 305 / 306 / 353 |
| Ground Fire / Blizzard / Gravity | 315 |
| Air Fire / Blizzard / Gravity | 316 |
| Ground Cure / Thunder / Aero / Stop | 317 |
| Air Cure / Thunder / Aero / Stop | 318 |
| Guard | 354, former grounded Cure pose |
| Items, ground and air | 399 |
| Ground Dodge Roll replacement | 009 |
| Idle and combat idle | Existing Terra poses, skull150 pitched up15 degrees |
| Damage and knockback | Native KH1 reactions |

Spell recovery follows its cast family. Magic and effects retain native
keyblade-tip origins. Native Guard/Dodge Roll eligibility, hit events, damage,
MP and collision remain. Single F retains ordinary held Glide.

## Air dash

A fresh airborne Square starts the tested v4 horizontal dash: captured stick
or character-facing direction, speed16,39 native ticks, maximum624 units. The
visual now uses the original KH1 Superglide active loop (normal physical slot76,
Olympus slot38,60 frames), sampled by KH1 itself. Its native animation bodies,
hair, helper data and events are not converted or overwritten. The burst samples
the beginning of that loop for its finite39 ticks. It replaces held Superglide.

A checked temporary pointer lease makes native fall slot10 resolve to that
original Superglide record during the dash. KH1 resolves the physical slot from
the live MSET each motion update (Steam29F3B8 and29FF80 paths). Completion or
interruption restores the original fall handle. Room/model transitions retain
a pending lease; rollback requires the same live MSET array, unchanged alias and
a fully admitted fall target. Unknown/reused pointers receive no writes.

The dash budget belongs to airtime. Completion, button release, damage,
unequip/re-equip, native Glide and cache readmission do not refill it. Only a
valid native ground state at floor height refills it, including landing while
another style is selected. A newly created Sora actor gets its own budget.
The v4 fix accepting the user's legitimate Square marker bits is retained.

## Native Styles page

The pause/party menu gains Styles immediately after Abilities. It opens KH1's
ability UI with a private Sora record containing eleven zero-AP style choices:
Singles A–F, Duals A–D, Anti. Only one may be enabled. The normal Abilities view
filters only style IDs116..126; every native ability copy and equip flag remains.
Other party members' normal Abilities still use their original records.

The menu's root list and indexed name/help/window/callback tables are enlarged
in private storage. All18 instruction references, three inline sites and four
window definitions must match the supplied Steam Global executable before any
coupled patch is published. Every destination page must be writable first; an
admission or protection failure leaves the native menu unchanged. Fallback on an
unsupported menu retains the prior ability-based style selector.

The native ability-list prologue still selects the party member. A bridge only
redirects Sora's record to its private view, preserving registers, XMM0..5, flags
and stack alignment. Native menu cursor/equip/sort behavior acts on that view.
Commit checks the actual save against its snapshot before merging changes.
Normal abilities retain their copies, equip flags and relative order; no global
save pointer is redirected. Native AP values and costs are retained.

Styles are virtual menu rows. Saves persist only one hidden style token instead
of ten or eleven learned rows. Legacy style entries compact without losing any
native ability, freeing their previous slots. One slot plus the native zero
terminator is needed for the hidden token: a save with47 native abilities stays
unchanged and cannot persist a new style selection. A rejected selection is
restored in the view. Malformed tails receive no save writes.

## Ownership and rebuilding

Rust owns the sole control, Guard-row, normal Glide, Superglide and fall hooks.
Both C adapters receive the same original fall trampoline. Retire the current
native-body lane, restore its bodies and cast lookup at idle, then admit the next
lane. Neither inactive adapter writes into another style's active bodies. Their
landing observers run independently of the selected style.

Generate private payloads with the two source generators and the user's Aqua v21
and Terra v4 source fixtures. Outputs belong in ignored local/single_e and
local/single_f. The delivery includes the generated headers for rebuilding; never
commit them or the private fixtures. Build with the existing Windows GNU target
and MinGW toolchain. Native adapter tests in native-tests use TERRA_SOURCE,
AQUA_SOURCE, STYLES_DLL and KH1_EXE environment variables. Shared Rust dispatch
and rendering are mocked; C code runs from the final combined PE. Windows loader,
GPU rendering and a complete game UI session are not exercised by that harness.

## Source and confidence

Sources: the user's confirmed-working Terra v4 package, Aqua v21 main payloads,
Styles v53 source commit7940a95, and the supplied Steam Global executable with
timestamp1721645006. Instruction anchors, native MSET lookup and menu record
semantics were checked directly. Confidence is high for the admitted addresses,
body/lookup round trips, save merging and offline dispatch behavior. The native
menu's final layout/navigation and live motion/collision transitions need the
user's in-game test. The package validation receipt records the final test counts
and exact source/DLL hashes. Existing licenses and credits remain.
