# Styles v56 / s395

The user reports that Single F cannot air dash in v55 and that everything else
worked. This revision changes only F's animation admission plus version labels.
The successful menu, Anti items, aerial-dodge visual rates and Single E timing
remain as delivered in v55. Both generated payload headers are byte-identical.

## Single F

The dash now uses the existing native Superglide record and encoded handle in
the loaded Sora/Olympus bank. It does not allocate a second motion or register
new pointers. The temporary fall-slot pointer lease and verified rollback stay.
All serialized source bytes other than native-owned header word zero and proven
pointer relocations must still match. The adapter never writes the native source
record, including that header word. Foreign curve/event changes remain rejected.

Square remains a fresh tap in the air, once per airtime. A valid landing rearms
it, including a small negative floor-height rounding value. Completion, damage,
release and changing styles cannot refill it midair. Direction, native collision,
speed16, duration39 and requested distance624 are retained. Normal Glide remains
usable; held Superglide remains replaced. No other style action code changes.

## Sources, confidence and validation

Sources: the user's v55 result, the delivered v55 DLL/source tree, Terra v4
private fixtures and the supplied Steam Global executable (timestamp1721645006).
The native pointer encoder uses a fixed64-entry bank table. Its original leaf
body is executed in the regression harness with all entries occupied, proving
that an unregistered allocation cannot reliably round-trip through its handle.
The new dash still starts and repeats across landings with the table full.

The delivered v55 DLL fails the new test when allocation and pointer registration
are unavailable after adapter setup. The revised DLL passes that same test and
the full42 F/menu checks; all47 Single E checks pass. Tests also check native
header-state retention, rejection of changed curves, both animation banks,
repeated landings, exact travel, spent-airtime persistence and pointer restoration.

Confidence is high for removal of the demonstrated admission dependency and for
the preserved source scope. The user's exact failing branch is unconfirmed
without a new runtime log. Header-state variation is a protected regression
case rather than an observation from that run. The C harness executes the final
PE adapters and identified native excerpts; Rust dispatch/rendering and Windows
startup are mocked. The user's next game test must confirm actual dash behavior.
Rust checks, source reconstruction and hashes are recorded in the package.
