SINGLE D SECONDARY REST REPAIR -- v46

The s384 log rejects target joints 9, 29, 112 and 259. All are outside the 103
mapped body/finger joints. The solver and map admit successfully, and the source
inventory is unchanged. v45 could reject its whole body over an unused helper,
resetting idle and falling back to KH1. Its finite-origin check also did not
bound the scale/shear that skinning applies to vertices.

v46 does not feed live +1B8 secondary records into Single D's map. It evaluates
the existing original Sora idle once at calibration and seeds checked local
rest for unmapped joints. Missing/bad rest entries use their own bind. Only
rotation/offset is retained from rest; scale stays the bone's own bind scale.
This prevents plausible local scales from multiplying down a helper chain.

Our bounds, not native constants: finite affine determinant; matching bind
handedness; per-axis length 0.5x..2x bind; normalized-axis dot/shear difference
at most 0.02; secondary offset at most 32 units from its own local bind.
Check every complete mapped output and check final skin bases again after
floor/weapon handling, before any existing matrix publication. Model-space
origins remain below 1000 units. Invalid authored source still rejects safely.

The shared secondary simulation is paused for mapped Single D movement, and
old particle state is cleared on entering D. This makes hair/cloth/keychain
more rigid for the mapping test. Other styles retain their normal behavior.
Do not weaken scene/script/native-request guards to hide unrelated fallbacks.

validation/secondary_fault_repro.csv compares old/new code on the same real
source/Sora rigs. Cases: 0=remote local; 1=finite 100x scale; 2=finite shear.
At each of four reported joints v45 drops the remote pose, but accepts large
scale/shear. All 12 cases recover in v46; maximum matrix difference from a
clean normal-scale pose is 0.0000306. This is injected-fault evidence, not a
capture of the player's exact bad matrices or a live GPU test.

The 2139-pose/31-clip unseeded output stream is byte-identical to v45, showing
the actual source-body mapping math is unchanged. Runtime rest seeding is
bounded separately and still requires a fresh-process game test.
Rules/source/confidence: docs/combat-model.md Stage 385 in the source patch.
