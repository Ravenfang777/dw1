# Type G: BBS Ventus native-body test

Type G uses the user's returned p01ex00 model and original p01ex PAM animation
channels. The main p01base bank is canonical where numeric names have variants.
The source rig has53 bones; Sora has293. The existing named anatomical mapping,
bind-length calibration, wrist pivots, bounded arm/leg clearance and native-body
fitter are reused from the original Terra tooling. Ventus's actual named rig is
checked before sampling; it is not interpreted as Terra's51-bone layout.

The new stance is ID115/code12, Single/I, zero AP. It shares the checked native
body adapter as profile2. Profile1 remains Terra, including its own Square dash
and cast variants. Type G supplies no new input or movement controller, spell
damage, defensive objects, invulnerability, aerial dodge or weapon model.

| Action | BBS animation | Source frames | Source range |
| --- | --- | --- | --- |
| Idle / combat idle | 001 / 002 | 90 / 110 | Full, loop closed |
| Walk / combat walk | 003 / 012 | 36 / 32 | Full, loop closed |
| Run / combat run | 004 / 013 | 16 / 20 | Full, loop closed |
| Jump takeoff / rise | 005 | 14 | 0..9 / 9..13 |
| Fall | 006 | 15 | 7..14, loop closed |
| Landing | 007 | 14 | Full |
| High jump takeoff / rise | 014 | 32 | 0..16 / 16..31 |
| Ledge hang | 020 | 95 | 55..94 |
| Ledge climb start / finish | 021 | 14 | 0..4 / 4..13 |
| Ledge landing recovery | 007 | 14 | Full, normal bank only |
| Ground combo | 300 / 301 / 302 | 28 / 34 / 32 | Full |
| Air combo | 305 / 306 / 307 | 21 / 29 / 31 | Full |
| Ground cast / recovery | 354 | 36 | 0..23 / 23..35 |
| Air cast / recovery | 355 | 40 | 0..27 / 27..39 |
| Item, ground and air | 600 | 44 | Full |
| Guard | 400 | 40 | Full |
| Dodge Roll | 009 | 19 | Full |

All listed BBS clips are30fps. The existing KH1 records retain their durations,
event keys, helper travel, headers and capacities. Body playback is retimed to
those records; this is an initial animation selection and native-timing test,
not a claim that the complete BBS action controller or command deck is ported.
Glide, Superglide, damage reactions, hitboxes, spell origins/effects and actual
Guard defense/roll movement remain native. Visual grip and contact alignment
must be checked in game before any additional weapon-bone changes are selected.

## Rebuilding

Apply the full source patch and use its included exact private payload headers
to rebuild the DLL directly. For optional G fixture regeneration, provide the
user's extracted Ventus capture Sources directory and a separate writable work
directory containing the original xa_ex_0010.mdls, xa_ex_0010.mset and
xa_ex_0010_he.mset used for the existing Terra fixtures. Python needs NumPy,
SciPy and Pillow for the reused tools.

```
python3 tools/ventus-retarget/build_ventus.py VENTUS_CAPTURE/Sources WORK --workers 4
python3 crates/kh1-hook/src/single_f/generate_data.py TERRA_V4_SOURCE local/single_f WORK
```

The first command emits converted fixtures, complete source inventory and
curve_validation.json. The second retains Terra as profile1 and incorporates
the checked G records as profile2. No native event stream is a write destination.
Use VENTUS_SOURCE=WORK alongside the previously documented Terra/native EXE
variables when running the final-PE F/G adapter tests. The exact included
terra_data.h already contains both profiles and requires no regeneration.

The generated before/Terra/variant byte blocks are compared with v63, including
all190 parts. Both bank mappings, request handles and root helper trajectories
remain checked. See styles-v64.md for measured bounds and live test limitations.
Source tools are derived from this project's original Terra v4 retarget tools;
ARC/PAM/PMO format references are documented in bbs_source_inspector.py.
