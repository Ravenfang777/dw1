DARK RIKU TO SORA BODY MAP -- v47

Source: original main1160,247 bones,31 clips; v44 validated authored solver.
Target: current native Sora293-bone table read at runtime.103 target joints
use101 distinct active source joints. Primary palm202->101; free palm99->206.
Inactive source tips, cape, hair and sword are not copied. One equipped weapon.

Most mapped turns are solved source rotation * inverse(source bind rotation),
applied to Sora's own bind basis. Child offsets retain Sora's own geometry.
Source3's authored basis did not place the hips along their solved separation.
For that pelvis turn, form a frame from hip39->5 and the perpendicular torso86
above their midpoint; forward is side cross up. Use the posed/bind frame turn.
The same actual target hip width and bone lengths remain. No guessed outward
translation or copied source limb length. Collapsed source landmarks reject.
Only the pelvis and its descendants change from v46; all228 other matrices
stay byte-identical over the full2139-pose probe.

Secondary joints use v46's checked immutable rest/bind, preserving own bind
scale. No live local cache enters Single D. Check complete private output and
final skin bases after existing floor/weapon handling, before publication.
Source travel is subtracted; model-to-world placement stays independent.
Script/event/hold/current-request/header/native field guards remain intact.
No boss AI, source gameplay scripts, events or hit windows run.

Current action policy:0 idle,1 walk,2 run,6 all airborne phases,7 land.
Air source6 plays once then holds its end. One per-Sora pause-aware game-frame
clock spans native takeoff/rise/fall; native clocks cannot restart it. Drawing
and pauses add no time. Native/ground/style/instance handoff resets it. Other
movement retains existing clocks. All Single D combat actions remain native.

REPRODUCTION
Apply source/NineStyles_v47.patch to the pinned upstream with git am.
Use your own original models and main bank; no source assets are bundled.
cargo run --locked -p kh1-data --example dark_riku_map -- DARK.mdls DARK.mset SORA.mdls OUTPUT.bin
The private probe samples every integer/end plus fractional/quantization points
on all31 clips. Do not distribute/install the raw matrix output.
validation/mapping_validation.json is the current v47 matrix/invariant result.
The v45 baseline and v44 source-solver/native-CPU proofs are labelled history.
None establishes live game/GPU skin parity. See combat-model Stage386 for
sources/confidence, observed stance discrepancy and exact scope.
