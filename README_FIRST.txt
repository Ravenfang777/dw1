KH1FM STYLES v56 / s395 - SINGLE F AIR DASH FIX

INSTALL
1. Close KH1. Disable v55 (or any older main Styles/Dual Wield package).
   Keep standalone Terra/Aqua tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v56, Build, and launch
   with Panacea. Keep existing KH2FM resources/settings for the older styles.
3. Confirm s395 / v56 in kh1-dual-wield.log beside the executable.

SINGLE F FIX
Fresh airborne Square uses the existing native Superglide animation handle,
without allocating or registering a copied animation. Only one dash is allowed
per airtime; landing rearms it. Releasing Square, finishing a dash, taking a
hit or changing styles cannot refill it in midair. Movement direction, speed,
distance and native collision are retained. Normal Glide remains usable.
The adapter preserves the native animation's header state and does not write
the source record. Unknown curve/event modifications are still rejected.

RETAINED FROM V55
- Single A-F, Dual A-D and Anti names, without Style:.
- Styles menu hides AP costs and Sora's current/max AP box. Normal Abilities
  retains its AP display and behavior; saved style IDs/choices are unchanged.
- Single A/C/E and Dual C/D aerial dodge visuals run at75% of their v54 speed,
  with the same movement, travel duration and distance. F keeps its slide rate.
- Anti uses native items with its combat-idle animation.
- Single E ground hit2 has no held-pose tail and chains into its finisher.
All other combos, magic, Guard and jump settings stay as delivered in v55.

PLEASE TEST
Select Single F. Jump, tap Square once, and try a second tap before landing:
only the first should dash. Land and jump again; Square should dash again.
Repeat a few times, and try both your normal/Olympus saves if convenient.
If it still fails, attach the new kh1-dual-wield.log from this v56 run.

VALIDATION
627 Rust tests in30 nonempty suites and89 final-PE adapter checks pass:
42 F/menu plus47 E. Includes repeated landings in both animation banks,
full pointer banks with the original native encoder, unavailable new handle/
allocation paths, exact distance, airtime budget and pointer restoration.
V55's failure under unavailable allocation/registration is reproduced against
its delivered DLL. Both payload headers remain byte-identical to v55.
Final menu rendering, Windows startup and live gameplay are not run here.
Source, rebuild inputs, incremental bundle, licenses and receipts are included.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Never run two versions of the Styles DLL together.
