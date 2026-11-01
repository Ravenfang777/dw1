DARK RIKU TO SORA BODY MAP -- v48

Body map/solver/secondary guards are unchanged from v47.103 Sora target joints
use101 active source joints. The pelvis uses solved source hips5/39 and torso86
relative to their bind frame, retaining Sora's own hip width and limb lengths.
Other rotations use the authored source/bind turn. Only checked immutable
secondary rest/bind is used; validate complete and final skin bases before
the existing publication. Source travel is removed; placement is independent.
Native request/header/field/script/event guards remain. One equipped weapon.

Corrected Single D movement policy:
Idle0, walk1, run2; takeoff3 (restored native phase); rise/fall6; landing7.
Only rise/fall enter the pause-aware play-once/hold clock. Takeoff does not
start or consume it. First rise/fall begins source6 at zero; continue once,
then hold its end until native landing or interruption. No gameplay, input,
velocity, damage, collision or jump-height changes. All combat mapping remains
pending; native KH1 combat is retained. Other styles and attachment routes stay.

Apply source/NineStyles_v48.patch to the pinned upstream with git am.
The offline example and v47 mapping calibration are unchanged:
cargo run --locked -p kh1-data --example dark_riku_map -- DARK.mdls DARK.mset SORA.mdls OUTPUT.bin
Use only your own original model/motion inputs. Do not distribute raw outputs.
validation/mapping_validation_v47.json retains the original2139-pose reference;
current mapping_validation.json documents exact source inheritance. v45/v44
reference files are historical. None is new v48 GPU/skin validation.
Source/confidence: docs/combat-model.md Stage387.
