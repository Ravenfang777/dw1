# Type G: BBS Ventus in KH1FM Styles v68

The original53-bone Ventus p01ex00 model and PAM sources are fitted to Sora's
293-bone native body. Native headers, allocations, helper travel and action
selection remain. Type G is ID115/runtime12, Single/I, zero AP. Profile1 remains
Terra,2 is main Ventus and3..37 keep the same numbered Ventus preview assignments.
Dark Riku previews use internal runtime14 and their own existing pose map.

| Action | Source |
| --- | --- |
| Idle / combat idle | 001 / 002 |
| Walk / combat walk | 003 / 012 |
| Run / combat run | 004 / 013 |
| Jump / high jump | 005 / 014 |
| Fall / land | 006 / 007 |
| Ledge hang / climb | 020 / 021 |
| Ground combo | 300 / 379 / 411 |
| Air combo | 305 / 306 / 482 |
| Guard / Dodge Roll | 400 / 009 |
| Ground Fire / Blizzard / Gravity | 416 |
| Air Fire / Blizzard / Gravity | 417 |
| Ground other magic | 390 |
| Air other magic | 508 |
| Ground / air item | 395 |
| Held Glide | 038 |
| Square dash / Circle aerial dodge | 330 / 410 |

All listed source clips are30fps. The delivered VENTUS_ANIMATIONS.csv includes
native record numbers, durations and source spans. Main G uses37 reversible
body records and a separate immutable038 held-Glide visual. The live Glide75
record is never patched or required for body admission. Native entry/exit/travel remain. Casting uses
scoped family recovery bodies while native release events and effects remain.

Square330 replaces Superglide at468 unobstructed units (Type F remains624), with
a locked initial direction and native collision.330/410 now move at2x v67 speed
and1.5x distance over29.25 native ticks, with4/3 visual playback.410 lifts43.875 units and
allows held038 Glide after completion. Each is once per real airtime. Shortcuts,
casts, damage and scripted states cannot start an air action. Numbered previews
retain their prior native controls. v67 fixes G's actual Rust constructor gates;
see styles-v68.md for current grip/travel/contact rules and styles-v67.md for the exit fix.

Main G's dash and both379/411/482 passes use the actual equipped blade against
native body parts, sharing successful-hit tracking with native contacts to
prevent duplicate hits. Native physical rows supply damage/feedback. First
finisher knockback waits until pass two through a scoped native record reaction.
Selected native first-contact/action timestamps are admitted and restored as
float-only changes; donor scripts/event payloads are never installed. Game feel,
window alignment and actual contact damage still need an in-game test.

The reverse grip is baked into the existing grip280 rotation of every converted
main/test clip and the separate038 visual. Native animation carries it through
blends; the runtime weapon-matrix writer is removed. Hilt, body curves, lengths,
header/count/capacity and native travel stay exact. Unmapped native records remain native.

## Rebuilding

Normal rebuilding uses the exact included private aqua_data.h and terra_data.h
headers; no asset regeneration is needed. Apply the full source patch, copy the
headers to local/single_e and local/single_f and use the documented Windows x64
build. Generated private data must never enter Git.

For optional full regeneration from the user's original Ventus capture, provide
Sources and separate work directories containing the original Sora model,
normal/Olympus MSETs used for Terra. Python requires NumPy, SciPy and Pillow.
The original main-G work is retained for the existing v65 gallery; the new main
work supplies current G actions. Commands:

```
python3 tools/ventus-retarget/build_ventus.py CAPTURE/Sources OLD_G_WORK --workers 6
python3 tools/ventus-retarget/build_ventus_tests.py CAPTURE/Sources OLD_G_WORK TEST_WORK --workers 6
python3 tools/ventus-retarget/build_ventus_v66.py CAPTURE/Sources OLD_G_WORK NEW_G_WORK --workers 6
python3 crates/kh1-hook/src/single_f/generate_data.py TERRA_V4_SOURCE local/single_f NEW_G_WORK TEST_WORK OLD_G_WORK
```

The gallery builder also stores its common original G fixtures under
TEST_WORK/common/fixtures. It covers all187 distinct originally unused clips;
fixed-capacity failures split into labeled contiguous source ranges. Its35
profiles retain their body curves/assignments and gain only the baked grip. Set VENTUS_SOURCE=NEW_G_WORK and
VENTUS_TEST_SOURCE=TEST_WORK for the current F/G final-PE tests, along with the
existing TERRA_SOURCE, STYLES_DLL and KH1_EXE variables.

Original/Terra/variant parts and E's private payload remain exact. All35 Ventus
previews retain their assignments; only grip rotation values change. The
generator imports tools/ventus-retarget/reverse_grip.py and leaves its input
fixtures untouched. Source identity, fitting, timestamp admission and current
validation limits are recorded in styles-v68.md. The original
retarget tools derive from this project's Terra tooling; ARC/PAM/PMO references
remain credited in bbs_source_inspector.py.
