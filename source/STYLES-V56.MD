# Styles v57 / s396

This update addresses the supplied v56 gameplay log and the user's additional
request for a green Styles screen below Customize. Both generated animation
payload headers and the successful v55/v56 behavior outside this scope remain.

## Single F

The log contains an accepted dash, an airborne spent-use rejection, a successful
landing reset, and repeated animation-admission failures at stage3. This proves
the landing reset worked. The source byte comparison still rejected an animation
that had previously passed admission; the log does not identify the exact bytes
changed by the native player.

Each new source is still fully checked before its first lease. Up to16 admitted
source bindings are retained. Reuse checks the array, handle, motion address,
layout counts, decoded stream addresses and readable spans. Native timing/cache
data is retained rather than compared with the unplayed file on every tap. No
source animation bytes are written. A changed source handle needs new admission;
a changed layout/address on a known lease is rejected. Once admitted, native
stream contents belong to the engine and are not protected against a later
third-party edit by a repeated file-byte comparison.

Movement lasts39 native movement ticks at speed16, with requested distance624.
It no longer terminates merely because the animation clock is already beyond39
or loops backward. Native request/state changes, damage, landing and unavailable
resources still cancel the action. A fresh Square tap is required, and landing
alone refills the once-per-airtime budget. Collision stays native. New bounded
logs distinguish queued start, committed Fall, first movement and termination.

The old v56 DLL fails two added regression cases: native cache fields changed
between uses, and a committed Fall with an inherited/looping animation clock.
These reproduce the relevant failure paths; the precise first-dash movement
failure in the user's run is not directly observed in the old log.

## Styles menu

Styles follows native Customize (ID3) in the root list. Selection remains keyed
by native ID; other rows keep their order and remembered selection.

The native panel renderer reads a window-specific palette at window+0x90 and
otherwise uses the global preset. Styles uses the existing native green preset,
including its border and shadow colors. The current window chain is reached by
the verified native previous/next links at+0x18/+0x20, with bounded traversal.
Original palette pointers are leased and restored when the party root regains
focus or normal Abilities is entered. Restore writes require the same window
definition and the unchanged owned green pointer. Global palettes remain intact.

Sources: the supplied Steam Global executable's native panel palette-selection
block, green preset, focus check and link setters; the v56 user log; the v56
delivered DLL/source. Confidence is high for native branch/data interpretation
and offline behavior. Tests execute the original native palette-selection code
for both green Styles and normal fallback. Native rendering, Windows startup
and final gameplay feel still require the user's in-game check.

Final tests, source reconstruction and binary hashes are in the package receipt.
