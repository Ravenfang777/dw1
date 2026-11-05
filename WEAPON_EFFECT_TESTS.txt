# Styles v75 / s414: KH2 weapon effect previews

Customize -> Passives66..104 replace the35 Ventus and four Dark Riku animation
preview abilities with39 individual KH2 PAX elements. Rows retain their numeric
labels and zero AP cost. One preview can be selected; confirming it again turns
it off. IDs105..114/127 remain reserved, and all normal passives/stances remain.

The selected element starts automatically after returning to the field. It
repeats every180 native game frames (three seconds at60fps). Each cycle allows
up to120 frames of playback then60 clear frames; short flashes expire normally.
Persistent elements are killed at the finite end, rather than accumulating.
No original attack, motion, spell, script, sound, damage or resource effect runs.
Original particle colors and authored transforms remain; Overdrives are separate.

Each description has three measured lines: effect name, KH2 package family plus
its element number, and current readiness. Actual full filenames are listed
below and in WEAPON_EFFECT_TESTS.csv. Status is loading, ready, partial programs,
missing archive/element, unavailable particle data, or retired geometry budget.
All39 candidates remain listed even if a particular user's KH2 package is absent.
Unsupported programs are skipped by the existing interpreter, not invented.

A preview does not change Sora's moveset or unequip a stance. It can be used with
stock Sora or an equipped stance. Only preview choices exclude one another.
Old animation-test flags are cleared on upgrade; reserved flags remain. Future
saves use weapon_effects=kh2-v1 in kh1-numbered-abilities.ini. Native save arrays
and AP do not store these selections. Removal disables preview queries.

## Catalogue

Each row is one package/element pair, not an entire attack's combined effects.
Labels identify traced source families; final appearance remains a visual test.

| Passive | Effect name | KH2 package | Element |
| --- | --- | --- | --- |
| 66 | Weapon appearance flash | obj/W_EX010.a.us | 0 |
| 67 | Last Arcanum root glow | obj/P_EX100_KH1F.a.us | 35 |
| 68 | Last Arcanum tip glow | obj/P_EX100_KH1F.a.us | 36 |
| 69 | Strike Raid blade ribbon | obj/P_EX100_KH1F.a.us | 32 |
| 70 | Valor finisher burst 13 | obj/P_EX100_BTLF.a.us | 13 |
| 71 | Valor finisher burst 14 | obj/P_EX100_BTLF.a.us | 14 |
| 72 | Final weapon burst 20 | obj/P_EX100_ULTF.a.us | 20 |
| 73 | Final weapon burst 42 | obj/P_EX100_ULTF.a.us | 42 |
| 74 | Final weapon burst 43 | obj/P_EX100_ULTF.a.us | 43 |
| 75 | Final weapon burst 44 | obj/P_EX100_ULTF.a.us | 44 |
| 76 | Final weapon burst 45 | obj/P_EX100_ULTF.a.us | 45 |
| 77 | Final weapon burst 46 | obj/P_EX100_ULTF.a.us | 46 |
| 78 | Final weapon burst 47 | obj/P_EX100_ULTF.a.us | 47 |
| 79 | Final weapon burst 101 | obj/P_EX100_ULTF.a.us | 101 |
| 80 | Final weapon burst 102 | obj/P_EX100_ULTF.a.us | 102 |
| 81 | Guard Break effect 30 | obj/P_EX100.a.us | 30 |
| 82 | Guard Break effect 31 | obj/P_EX100.a.us | 31 |
| 83 | Guard Break effect 32 | obj/P_EX100.a.us | 32 |
| 84 | Finishing Leap effect 33 | obj/P_EX100.a.us | 33 |
| 85 | Finishing Leap effect 34 | obj/P_EX100.a.us | 34 |
| 86 | Aerial Finish effect 35 | obj/P_EX100.a.us | 35 |
| 87 | Aerial Finish effect 36 | obj/P_EX100.a.us | 36 |
| 88 | Aerial Finish effect 37 | obj/P_EX100.a.us | 37 |
| 89 | Aerial Finish effect 38 | obj/P_EX100.a.us | 38 |
| 90 | Final first swing effect 52 | obj/P_EX100_ULTF.a.us | 52 |
| 91 | Final first swing effect 53 | obj/P_EX100_ULTF.a.us | 53 |
| 92 | Final first swing effect 54 | obj/P_EX100_ULTF.a.us | 54 |
| 93 | Final first swing effect 55 | obj/P_EX100_ULTF.a.us | 55 |
| 94 | Final first swing effect 56 | obj/P_EX100_ULTF.a.us | 56 |
| 95 | Final first swing effect 57 | obj/P_EX100_ULTF.a.us | 57 |
| 96 | Sonic Rave effect 26 | obj/P_EX100_KH1F.a.us | 26 |
| 97 | Sonic Rave effect 27 | obj/P_EX100_KH1F.a.us | 27 |
| 98 | Sonic Rave effect 28 | obj/P_EX100_KH1F.a.us | 28 |
| 99 | Sonic Rave Finish effect 29 | obj/P_EX100_KH1F.a.us | 29 |
| 100 | Sonic Rave Finish effect 30 | obj/P_EX100_KH1F.a.us | 30 |
| 101 | Sonic Rave Finish effect 31 | obj/P_EX100_KH1F.a.us | 31 |
| 102 | Strike Raid catch flash | obj/P_EX100_KH1F.a.us | 34 |
| 103 | Infinity tip charge | obj/P_EX100_KH1F.a.us | 20 |
| 104 | Counterguard hand flash | obj/P_EX100.a.us | 41 |

## Attachment and lifecycle

Packages are read once from the existing KH2 installation/backup using the same
Install source policy and texcommon as existing visuals. The catalogue includes
base Sora, Kingdom Key, Valor, Final and Limit archives, independently of which
stance donor was loaded. Their original textures are appended once to the shared
renderer pool; no original particle payload is compiled or committed.

Weapon point codes4003..4008 map to the current primary blade's tip/root/midpoint.
Even left-weapon codes use that primary blade for an isolated comparison.
Weapon-package flash, Strike Raid ribbon and catch flash use a blade preview
host. Other body/object anchors retain their authored mapping. Previewing a
Strike Raid ribbon does not throw the blade. Calibrate KH2 blade coordinates to
the actual native grip using bind matrices, retaining baked Type G reverse grip.
Floating stances use the actual drawn primary blade. This alignment is an
adaptation, not a claim that the complete original KH2 attack is reproduced.

The shared immutable effect pose is also requested when only a preview is active.
Stock Sora and native E/F/G previews refresh parent-local joints at actual field
draw; mapped styles publish their admitted pose. Scope is the exact actor,
instance and binding generation, with a two-tick pose lifetime. Reconstruct joints
without writing native body matrices. Continuously bound roots refresh again at
draw without advancing effect clocks. Missing anchors never spawn at identity.
Selection change, scope loss, menu/pause hiding and removal retire/hide previews;
physics owns time. Only one preview handle is admitted. The existing geometry
cap also retires an oversized preview for the session rather than retrying each
frame. Status reports this explicitly.

## Sources and confidence

User request: repurpose the animation gallery, KH2 only, with effect names/IDs in
help. Existing kh2fx.rs weapon/form routes, docs/kh2-effects.md sections12.3/12.4,
and docs/drive-model.md Limit traces identify the chosen families/elements.
Final52..57 are the first ground-swing effects; Limit26..31 Sonic Rave/Finish,
34 its catch flash and20 Infinity charge. The prior v74 catalogue supplies the
other candidates. Names describe family membership, not unobserved visual detail.
Confidence high for recorded mappings and isolated selection/storage; final file
availability, skipped programs, blade fit and appearance require runtime checks.
The180/120/60 preview cycle and first-blade host are deliberate test choices.

## Validation and retained scope

665 Rust policy/math checks in30 nonempty suites and9 focused final-PE C/menu
checks pass. Current receipts record their scope and final source/archive checks.
The focused PE harness admits the real native adapter/menu against the supplied
Steam executable, and exercises39 descriptions, all12 stance coexistence paths,
exclusive toggles, zero-AP full-capacity lists and dynamic readiness. Rust/GPU
callbacks and package availability are mocked there. It requires no animation
regeneration fixtures and does not execute Windows or the game.

Both private generated headers stay byte exact to v74. Main Type G/Type D and
all other stance mappings, damage, contacts, movement, intrinsic passives,
Overdrives/palette3, Customize/Appearance and footsteps mute remain. Historical
animation payloads remain unused in the build; their old menu access is retired.
No KH1/BBS preview is added. Check actual effects in the user's field session.
