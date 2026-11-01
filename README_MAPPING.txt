DARK RIKU TO SORA BODY MAP -- v49

The original247-bone authored solver and103-target/101-source body map are
unchanged. Corrected solved-hip/torso frame retains Sora's own hip width and
lengths. Checked immutable rest/bind preserves scale; complete/final skin bases
are checked before publication. Source travel is removed; placement independent.

D's native basic ground slots C8/CA,C9,CB map to18,19,20; air CC,CD,CE map to
18,19,21. Each uses actual source length and current native normalized phase,
clamped at its end. Exact current/requested attack slot, field lane, actor,
binding, header and scene/script/hold checks are required. Other native action
abilities remain native. KH1 owns combo progression, hit timing and damage.
No new attack controller, callback, hit window, HP write or boss event import.

Only Jump borrows Single C: same Riku donor/motion, paired native takeoff/rise
clock and source-layout/rest calibration. A separate per-Sora retarget avoids
changing D's base retarget/map. No raw Riku matrices reach base-Sora secondary
or effect maps. D's fall6/landing7 remain; the fall interval starts on fall.

Apply source/NineStyles_v49.patch to pinned upstream using git am.
Original source probe (raw inputs/output stay private):
cargo run --locked -p kh1-data --example native_mset_solve -- DARK.mdls DARK.mset OUTPUT.bin
Original target mapping probe is unchanged:
cargo run --locked -p kh1-data --example dark_riku_map -- DARK.mdls DARK.mset SORA.mdls OUTPUT.bin
validation/source_validation_v49.json records fresh source checks. Current
mapping_validation.json documents source inheritance and action scope; the
v47 target-matrix receipt and v44 native-CPU receipt are labelled history.
None establishes new v49 GPU/skin or authored boss-contact parity.
See SINGLE_D_COMBO_MAP.txt and combat-model Stage388 for exact choices,
confidence, native timing limits and test instructions.
