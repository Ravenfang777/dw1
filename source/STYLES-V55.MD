# Styles v55 / s394

This revision follows the user's v54 gameplay log and requested UI/action changes.
The eleven style IDs, native65 ability definitions and native AP values remain.

## Menu and Anti items

Ability labels now read Single A–F, Dual A–D and Anti. The Styles page omits its
AP-cost column and its Sora current/max AP panel. Normal Abilities keeps its AP
column/panel and native ability values. Two scoped native window-creation calls
omit the optional AP panel in Styles; their existing null-window paths still
activate the parent/list. A scoped row-drawing bridge skips the entire cost
background/label/digits block while retaining loop state. Normal Abilities runs
the original indexed-color calculation. All additional anchors are admitted
before publishing the menu patches.

Passive Anti permits item commands in top lists, target lists and shortcuts,
including item IDs overlapping a summon command ID. Its items show the same
looping Anti battle idle as normal combat idle, with no weapon. Native item
eligibility, consumption, targets and effects remain native. Magic/summons and
physical specials remain restricted. Legacy Drive Anti keeps its item restriction.

## Aerial dodge visuals

Single A/C and Dual C/D retain the original Master action controller, travel2x,
steering, action duration and terminal velocity. Only RigAnim's body/weapon sample
uses75% of the current source frame. The original Output still owns physics and
events. Single E keeps movement speed21, lift1.125 and duration26 native ticks:
546 horizontal units and29.25 lift. Its native motion sampler advances1.125
instead of1.5, a75% visual rate; collision displacement and handoff are unchanged.
Single F remains a Superglide-based air slide with its existing playback speed.

## Single F repeated airborne use

The supplied log shows an initial accepted dash, an in-air spent-budget rejection
0x1000, then animation-admission failures0x800. A landing-only counter by itself
therefore did not resolve the reported lockout.

Each use now refreshes one private writable copy of the original native60-frame
Superglide record. The exact original bytes are already in the private payload;
all nine pointer fields are re-encoded and verified before use. This avoids
reusing the live source record's playback state. One bounded allocation is reused.
The temporary fall-pointer lease returns to the same admitted fall handle.
Rollback checks array, handle, header and part-address identity; it does not
reject or overwrite body bytes merely because playback updated them. Unavailable
resources keep a pending lease and unknown destinations receive no writes.

Only a valid native landing refills the airtime budget. Floor-height rounding
below zero is accepted with the native ground state. Release, completion, damage,
model/cache changes and unequip/re-equip do not refill it. The ledger is observed
under other styles too. Successful landing resets are logged once per spent use;
animation-admission failures include their stage.

## Single E second ground hit

Both native301 variants now sample the full pose continuously, removing the old
held-pose tail. Slot99 runs47/24 and slot100 runs63/24 native frames per tick.
The authored body still finishes in24 ticks; native actions finish in24.51/24.38
instead of carrying an extra held recovery. The chain window opens at20 ticks
and lasts through the native endpoint, avoiding a sub-frame input window.
Contact and sound events preserve their previous real-time placement. Native
travel-helper curves, headers, descriptor counts and event payloads remain.

The asset-free retime_second.py resamples the user's serialized v21 pose through
the existing native-curve fitter, carrying native root travel at its new sample
phase. It does not retarget or change anatomical lengths. Two new fits have
maximum sampled position errors below0.93 native units and root-helper error0.
Generated payloads and all private models/MSETs remain outside Git.

## Evidence and limits

Sources: the user's kh1-dual-wield(20261103-133515).log, v54 source44fcf96,
Aqua v21/Terra v4 private fixtures and the supplied Steam Global executable
(timestamp1721645006). Offline tests execute the final combined PE's C adapters,
real native ability-record prologue and both AP branch paths. They cover repeated
landings, private playback reset, pointer rollback, normal AP behavior, native
item policy, preserved dodge movement and the retimed hit/chain events. Shared
Rust dispatch/rendering and the Windows loader are not executed in that harness.
Live item effects, final menu layout and action feel still need a game test.
Final counts, source reconstruction and binary hashes are in the delivery receipt.

Validation: 627 Rust tests in 30 nonempty suites pass. All 47 Single E and 40
Single F/menu adapter checks pass against the final Windows x64 release DLL.
