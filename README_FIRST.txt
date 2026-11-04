KH1FM STYLES v60 / s399 - CUSTOMIZE PASSIVES AND NATIVE PANELS

INSTALL
1. Close KH1. Disable v59 or any older main Styles/Dual Wield package.
   Keep standalone Terra/Aqua tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v60, Build, and launch
   with Panacea. Keep existing KH2FM resources/settings for older stances.
3. Confirm s399 / STANCES v60 in kh1-dual-wield.log beside the executable.
   This native menu/Single F adapter targets the supplied Steam Global build.

MENU
Main menu: Items -> Customize -> Equipment -> Shortcuts, then native options.
The old Abilities main-menu entry has been removed. The original native
Customize remains visually renamed Shortcuts with its original functionality.

Customize categories, in order: Stance, Passives, Limits, Outfits.
- Stance: eleven types, eight visible rows, native scrolling and equipped
  marker. Weapon and magic values use a single native AP panel per value.
  The bright blue frames and second offset capsules are removed. Both boxes
  have matching native 42x22 geometry and centered labels.
- Passives: opens the complete normal Abilities menu, starting with Sora.
  Native party/shared access, scrolling, descriptions, equip/remove dialogs,
  AP costs and totals are retained. Custom stances stay hidden from its list.
  Cancel out of that submenu to return to Customize.
- Limits and Outfits: empty categories reserved for later additions.

The page header reads Customize and becomes Passives inside that submenu.
Open Stance to select a type. Confirm it to equip it exclusively. Confirm the
currently equipped type again to turn it off. Cancel returns to the categories;
cancel again returns to the main menu. The stance scroll position is retained.

STANCE LABELS                WEAPONS   MAGIC
Single A -> Type A           Single    I
Single B -> Type B           Single    I
Single C -> Type C           Single    I
Single D -> Type D           Single    I
Single E -> Type E           Single    I
Single F -> Type F           Single    I
Dual A   -> Type H?          Dual      I
Dual B   -> Type I?          Dual      I
Dual C   -> Type K?          Dual      I
Dual D   -> Type L?          Dual      I
Anti     -> Type M?          None      0

Question marks are intentional. Magic markers: 0 unavailable, I KH1, II KH2.
Current armed stances execute KH1 magic, including those with KH2 casting
poses/effects, so they show I. II is reserved for a future KH2-magic stance.
Type M? still allows items and blocks magic.

SAVES / RETAINED BEHAVIOR
Saved stance IDs and the hidden style token are unchanged. Native ability
flags, duplicate entries and AP remain intact. Equipment, inventory and
shortcut assignments are not repurposed. A full native ability list can still
toggle its normal entries; selecting a new stance refuses when no token slot
is available. Limits and Outfits do not allocate save fields yet.
Combat behavior, all action/controller sources and both generated animation
payloads match v59, including Type F's fixed-facing once-per-airtime air dash
and its L1/LB + Square magic-shortcut exclusion.

TEST / REPORT
Check the main-menu order and the Shortcuts configuration. Open Customize;
check its title and all four categories. Scroll through Stance and compare
both metadata columns: one aligned dark AP-style box behind each value.
Open Passives, equip/remove a normal Sora ability, check AP and descriptions,
then cancel back to Customize and confirm the stance remains selected.
Reopen Passives and check party/shared selection as needed. Limits and
Outfits should be empty. Confirm your usual combat still works.
If an issue remains, return the new kh1-dual-wield.log and a screenshot or
short video of the action/layout concerned.

VALIDATION
627 Rust tests in 30 nonempty suites and 109 final-PE checks pass: 62 F/menu,
47 E. New tests execute the original native AP renderer to its draw packets,
the window factory/Abilities constructor and the equip/remove decision
callback, including insufficient-AP rejection. Existing paging, input,
selection, save-boundary and combat regression checks continue to pass.
The Windows x64 DLL builds with four exports and eight imported DLLs.
GPU allocation/submission, most menu drawing, native cleanup and Rust
startup/dispatch are harness substitutes. This build has not been run inside
KH1 on Windows; final appearance, focus transitions and feel need a game test.
Source, rebuild inputs, incremental bundle, licenses and receipts are included.
Current results are in validation.json; older results are historical.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Never run two versions of the Styles DLL together.
