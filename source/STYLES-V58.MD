# Styles v58 / s397

This update follows the user's v57 feedback: abandon the unsuccessful green
menu, lock Single F facing during its dash, avoid L1/LB magic shortcuts, and
present three equipment-style slots for future customization.

## Single F dash

Capture the normalized horizontal direction and native yaw atan2(X,Z) on the
initial airborne Square press. Apply that forward direction, current yaw and
target yaw during the owned dash, before/after native control and before native
collision displacement. Subsequent stick direction cannot rotate the character.
Ending the dash, landing, damage/casting, scene changes and loss of ownership
release the lock. Native XYZ position, camera and unrelated actors are untouched.

L1/LB is the native logical0x40000 modifier. The active shortcut menu also has
its own native root pointer. Either blocks dash admission and input masking;
Square remains available to native shortcut dispatch and no airtime use is
spent. Releasing the shortcut modifier while still holding Square cannot start
a delayed dash; release Square before a genuine new dash press. Square's
ordinary high marker is accepted. Native command and queued-action guards stay.

Travel remains39 movement ticks at speed16, requested distance624, with native
collision and the default Superglide visual. Native animation-clock changes
cannot shorten movement. One dash per airtime, refilled only by landing. Both
private generated animation headers remain byte-identical to v57.

## Three Styles slots

Styles remains immediately below Customize. A Styles-only native window
callback shows Primary, Secondary and Tertiary. Primary shows the equipped style
or None. Confirm it to open the eleven style choices plus None. Confirming the
current style keeps it equipped; choosing None unequips the custom style.
Secondary and Tertiary show Empty and have no choices or effects yet.

Native navigation, cursor, confirm/cancel masks and sound helpers are used.
Cancel in the picker returns to the slots without saving; cancel on the slots
closes the native Styles chain as before. The first new-page callback ignores
the entry press so opening Styles cannot also select Primary accidentally.

The new view uses the existing snapshot-checked single hidden style token.
Secondary/Tertiary do not claim save bytes yet. Native equipment, item inventory,
party data and AP are not repurposed. Normal Abilities continues to hide custom
style IDs and retains native ability behavior/AP. Green palette code is removed;
all panel drawing uses the normal native palette, with no color override.

## Evidence and limits

Primary local sources are the supplied Steam Global executable, native facing
setter, pad/shortcut-root findings in kh1-shortcuts.md, native window helper
calls/fields, and the user's request. Confidence is high for these local
interpretations and offline behavior; final in-game visuals remain unobserved.
Read-only helper entry anchors join all coupled menu checks before publication;
a mismatch leaves the complete native menu intact.

The final integrated Windows PE C code is exercised with Win64 ABI mocks on
Linux. Tests include facing after opposite input and native turn writes, both
shortcut exclusions without budget/input loss, normal marker bits, exclusive
selection/None/current-style behavior, empty reserves, cancel, swapped buttons,
normal abilities/AP, source-cache reuse, exact travel and landing rearm. Original
native focus, selected-row, confirmation and close-chain code executes in these
checks. Navigation/rendering and shared Rust dispatch are mocked; no Windows
loader/GPU or full gameplay/menu session is run here. Final counts, hashes and
source-apply checks are recorded in the delivered package.

The release passes627 Rust tests in30 nonempty suites and100 final-PE checks
(53 Single F/menu,47 Single E). The delivered v57 binary fails the two added
facing/shortcut regression cases. Windows x64 builds with the existing four
exports and eight imported DLLs. These checks do not establish live rendering.
