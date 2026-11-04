# Styles v65 / s404: Ventus numbered tests and reverse grip

## Equip rules

Passives66..100 are35 zero-AP Ventus animation tests. Selecting one disables
all equipped stance tokens in Sora's existing learned array, then selects only
that test. Selecting a stance clears the active test. Normal native passive
flags, their AP costs, the other unused numeric flags and all neighboring save
fields are preserved. Selecting the current test again disables it without
automatically equipping a stance. The native48-byte capacity is unchanged.

The test transaction admits the current save identity, a valid complete list
and an unchanged snapshot before writing. It never appends a learned entry or
evicts a normal ability. A full48-entry list can still select a test. Stance
selection retains its existing hidden-token capacity requirement.

Numbered settings remain mod-wide in kh1-numbered-abilities.ini. A version
marker distinguishes actual animation-test selections from older no-effect
placeholder flags: old flags66..100 are cleared on upgrade, while unassigned
101..114/127 retain their meaning. A saved equipped stance wins any conflict
introduced by loading a different save. Former115 bit49 remains retired;
127 stays at bit50. The same single-test normalization applies on load/write.

Tests use internal runtime code13, with no saved stance ID and no Stance row.
The shared native adapter uses profile1 for Terra,2 for main Ventus and3..37
for tests66..100. It restores the previous native body data at idle before
another adapter runs. Changing tests also waits for the current action to end.
Only Terra profile1 can use Terra's dash and cast-recovery variants. Tests
retain KH1 movement, contact, magic/item/Guard events and native travel.

## Animation coverage

The supplied Ventus inventory has298 records but210 distinct source hashes.
The main G mapping uses23 distinct clips, leaving187 unused distinct clips.
Every unused clip is assigned to a ground or air combo position in the35 tests.
Exact duplicate archive copies share one preview; aliases are listed in the
package CSV. Numeric source labels are not interpreted as move names.

Each test has three ground and three air positions; the native alternate
second ground hit also uses the listed second ground animation. Every source
frame range is covered. Complex clips that exceed an existing native record's
curve capacity are split into contiguous inclusive ranges, with the boundary
frame shared. Those ranges are labeled in VENTUS_TESTS.txt and the detailed
VENTUS_TESTS.csv. Splitting preserves coverage without expanding game buffers
or weakening fitting bounds. No source events, scripts or BBS command behavior
are imported. All source clips are30fps, retimed into existing KH1 records.

The builder deduplicates by source SHA256, verifies each canonical source,
checks all frame-range unions and retains the original root helper. The245
converted records meet the existing limits: position error <=5 model units,
basis error <=0.12, segment error <=0.01 and native root-helper error <=1e-7.
Measured maxima are4.688/0.105/below3.9e-11/zero respectively, with zero scale
error across52,185 quarter-frame pose samples. This bounds approximation error;
it does not establish mesh clearance, ideal combat timing or move suitability.

The generated shared header keeps all190 original/Terra/Ventus/variant part
payloads identical to v64. Only the seven combo records differ between main G
and a numbered profile. Existing E/F action controllers and E payload remain.
A compile-time guard rejects an incomplete shared test payload.

## Reverse Keyblade grip

Type G and numbered Ventus tests turn the weapon180 degrees about the grip's
local Z axis, reversing its longitudinal X axis at the same hilt. This differs
from the old optional X-axis teeth roll. The source is the supplied original
Sora model: skinned wrist100, palm101, grip280 and weapon subtree281..292.

The native-pose path rebuilds the weapon from fresh wrist100 and untouched
relative local matrices, with bind-relative fallback for absent weapon-child
matrices. It never feeds back a previously reversed weapon pose. Both skeleton
and IK passes therefore produce the same result. Parent topology, affine
matrices, attachment distance and all output matrices are checked before any
weapon write. Body, arm, finger, hair, native local and scale data are untouched.
Wooden/dream weapons52..55 are excluded. Other stances retain their own grips.

## Validation and limits

636 Rust tests pass in30 nonempty suites.150 final-PE checks pass:103 shared
F/G/test/menu checks and47 Single E regressions. All35 test profiles apply and
restore every record in normal and Olympus banks using relocated pointers.
UI checks cover all12 stances in both equip directions, every test selection,
full native lists, zero AP, invalid lists, native AP behavior, migration and
ordinary menu regressions. Geometry checks cover blade-axis reversal, hilt
and segment preservation, repeated-pass idempotence and invalid input.

The Windows x64 DLL retains4 exports/8 imported DLLs. The harness executes the
final PE's C adapter but substitutes Windows APIs, rendering and shared Rust
dispatch. Geometry tests exercise pure matrix policy. Actual Windows startup,
GPU weapon appearance, mesh clearance, contacts and live switching remain for
the user's game test; no game execution is claimed.

Sources: the user's Ventus capture and requests for unused-animation previews,
reverse grip and mutual exclusion; delivered v64; original Sora model/MSETs and
supplied Steam Global executable; this project's original retarget tools.
Inventory/hash/range, byte-capacity and mathematical findings are high-confidence
offline results. Suitability of each preview and the final rendered grip remain
provisional until observed in game. No game assets or generated payloads enter
Git; exact private rebuild inputs are included only in the delivered package.
