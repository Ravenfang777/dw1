V46 NOTE: historical calibration/solver method below. Current runtime uses
checked secondary rest, not live cache locals. See README_SECONDARY_FIX.txt.

DARK RIKU AUTHORED POSE SOLVER -- v44 REFERENCE RETAINED IN v45

The pipeline now includes model defaults -> constant channels -> native fixed-
tick curves -> helper hierarchy -> authored bone constraints. It is stateless
and can sample frames out of order. Tangents are per 1/256-frame tick; duplicate
time keys use the original binary-search selection. Arm/leg bend, pole/roll,
orientation copying, cached transforms and seeded endpoints follow source data.

The bank has 247 bones, 205 native-active joints per clip and 12 helpers. Inactive
joints are explicitly marked; their identity matrices are not solved landmarks.
The separate root-motion channel is returned as data, never applied to the actor.
The solver does not run terrain/floor IK, gameplay, AI, events or hit detection.
v45 adds body mapping and a first field movement test; action/contact mapping remains pending.
The supplied v45 GIF compares the source rig with Sora; it is not gameplay video.

REFERENCE METHOD
The original captured Steam pose evaluator was run inside isolated Unicorn CPU
emulation with private model/motion buffers and identity actor placement. Pointer
resolution uses emulated buffers; CRT math uses host math; event queries and
cookie checks are excluded. Floor/actor flags are disabled. No original Windows
executable is launched as a process and no running-game memory is accessed.
Native matrices = diag(1,-1,-1,1) * source-model solver matrices.

Compared 2139 poses over all 31 clips: every integer frame, end frame, nine spaced
fractional samples and non-tick input times. Checked 205 active bone matrices,
12 helper matrices and root channel per pose; 7426608 float components.
All passed. Max position distance 0.001807024 units; basis component 0.000038028;
helper component 0.000066758; root component 0. Float results are not bit-identical.
See validation/native_solver_validation_v44.json for the per-clip error report.
No actual game/GPU or Sora-retarget validation has run here.

OPTIONAL REPRODUCTION FROM SOURCE
Apply source/NineStyles_v46.patch to the pinned upstream using git am (see
source/PROVENANCE.txt). Use your own captured xa_ex_1160.mdls/.mset and the exact
reference executable version. Those files are deliberately not included.
The Rust example emits a private binary pose stream:

cargo run --locked -p kh1-data --example native_mset_solve -- MODEL.mdls BANK.mset POSES.bin

The standalone reference harness requires NumPy and Unicorn 2.1.4 in a separate
development Python environment. These are NOT DLL/runtime dependencies.

python validation/native_pose_reference.py --exe GAME.exe --model MODEL.mdls --bank BANK.mset --poses POSES.bin --output comparison.json

The harness verifies the captured executable/model/bank hashes. It refuses a
version that was not verified; no guessing of native addresses or substitution.
It takes several minutes and does not modify any input file.
Model SHA256: ef243b6ffe6d5234a1c4b795946f82db34cafb5f427ab816c8090b89379d91e3
Bank SHA256: b50be471d376786a80caabbdaf08e861985d0d957e914552dc98180aa6c4d2a8
EXE SHA256: d790746245d26159f3ee0e1060e33b2fa2de06941850a4ac724f598722884bac

The parser/math and reference harness are our own source. Native instruction
bytes are read only from the provided executable; none are embedded/distributed.
Unicorn API: https://www.unicorn-engine.org/docs/tutorial.html
Rules, source addresses and confidence: docs/combat-model.md Stage 383.
