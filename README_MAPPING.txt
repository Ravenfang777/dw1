DARK RIKU TO SORA BODY MAP -- v45

Source: captured xa_ex_1160 (247 bones), using v44's validated authored solver.
Target: current native Sora (293 bones); runtime reads the actual bone table.
Mapped body/finger joints: 103 target / 101 distinct active source.
Primary palm: Dark Riku 202 -> Sora 101. Free palm: 99 -> 206.
Source inactive endpoints, cape, hair and sword are not retargeted.

Global turn = solved source rotation * inverse(source bind rotation).
Target rotation = global turn * target bind rotation. Target child placement
uses Sora's own parent-relative bind offset. This is a separate KH1-to-KH1
calibration; the existing KH2 position-frame retarget is untouched.
Unmapped target children keep valid native locals. Native unused/non-affine
locals use their own bind fallback. The source's root travel is subtracted
before root-height scaling; model-to-world placement stays independent.

Admission checks bone counts, hierarchy, limb geometry, hand sides, source
activity and affine finite transforms. It produces a whole private pose before
any existing render publication. Failure leaves native posing in place.
Only current regular-bank field locomotion is drawn in this stage. A matching
locomotion request is also required, so an accepted attack/cast cannot retain
an obsolete walking/landing overlay during its header handoff. No event,
script or hold can borrow an overlay. No source AI/events/hit windows run.

REPRODUCTION
Apply source/NineStyles_v45.patch to pinned upstream using git am.
Use your own source main model/bank and Sora model; no input assets are bundled.

cargo run --locked -p kh1-data --example dark_riku_map -- DARK.mdls DARK.mset SORA.mdls OUTPUT.bin

The probe samples every integer/end frame plus fractional/quantization points
and emits a private binary pose stream. Do not install/distribute that stream.
validation/mapping_validation.json contains the 2139-pose independent matrix
comparison and invariant results. Those are not native-solver or GPU parity.
The legacy native-solver comparison remains in the separate v44 receipt.
Source profiles/rules/confidence are in docs/combat-model.md Stage 384.

The eight movement slot roles are inferred from solved pose sequences. The
remaining clips are numerically mapped, but their semantic names, attack
ownership, timing and contacts are not inferred from slot numbers alone.
That action/contact integration is the next stage after live body alignment.
