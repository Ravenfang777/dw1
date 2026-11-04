KH1FM STYLES v61 / s400 - BUILT-IN ABILITIES

INSTALL
1. Close KH1. Disable v60 or any older main Styles/Dual Wield package.
   Keep standalone Terra/Aqua tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v61, Build, and launch
   with Panacea. Keep existing KH2FM resources/settings for older stances.
3. Confirm s400 / STANCES v61 in kh1-dual-wield.log beside the executable.
   This native menu/Single F adapter targets the supplied Steam Global build.

BUILT-IN ABILITIES
Scan, Dodge Roll, Guard, High Jump, Mermaid Kick, Glide and Superglide are
always available while this mod runs, even when no stance is equipped.
They cost no AP and occupy no learned-ability slots. Their old copies are
removed from the corresponding save lists, freeing up to three Sora slots
and four shared slots. Other party members and other abilities stay native.
Normal action/room/swimming restrictions and stance-specific replacements
still apply. This does not automatically guard or change the dash controls.
Native definitions and max AP are not changed; the spent AP is freed normally.

ABILITY CAPACITY
Stock definitions: 65. The relocated table supports native IDs1..127, giving
62 possible IDs above stock. Eleven styles use116..126;51 representable IDs
remain unused. Each new ability still needs its actual behavior and labels.
Sora's learned list and the separate shared list each have48 bytes. Current
Styles keeps a terminator and one hidden stance token, allowing46 ordinary
Sora entries alongside a stance. This build does not enlarge those lists.
Beyond the saved-list/ID limits needs custom storage and lookup/menu routing.
The included STYLES-V61.MD gives exact findings, native IDs and test limits.

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
Saved stance IDs and the hidden token are unchanged. Only the seven requested
built-in entries are compacted from their appropriate learned lists. All other
native entries, duplicate flags, AP/stat fields, equipment, inventory and
shortcut assignments are preserved. Native AP accounting no longer charges
for Sora's three built-ins. Limits/Outfits do not allocate save fields yet.
Combat action controllers and animation payloads match v60, including Type F's
fixed-facing once-per-airtime air dash and L1/LB magic-shortcut exclusion.

TEST / REPORT
With no stance equipped, check the seven built-in abilities first, including
Scan, jump/glide and Mermaid Kick when swimming. The built-ins should not
appear in Passives/Shared or use AP. Check normal AP abilities and each
stance's movement replacements. Check the main-menu order and Shortcuts. Open Customize;
check its title and all four categories. Scroll through Stance and compare
both metadata columns: one aligned dark AP-style box behind each value.
Open Passives, equip/remove a normal Sora ability, check AP and descriptions,
then cancel back to Customize and confirm the stance remains selected.
Reopen Passives and check party/shared selection as needed. Limits and
Outfits should be empty. Confirm your usual combat still works.
If an issue remains, return the new kh1-dual-wield.log and a screenshot or
short video of the action/layout concerned.

VALIDATION
627 Rust tests in 30 nonempty suites and 125 final-PE checks pass: 78 F/menu/built-in,
47 E. New tests execute the original native AP renderer to its draw packets,
the window factory/Abilities constructor and the equip/remove decision
callback, including insufficient-AP rejection. Existing paging, input,
selection, save-boundary and combat regression checks continue to pass.
New checks execute native AP accounting, the movement/Scan cache, counter
fallback, the48th/49th append attempts and ID127 lookup. Save boundary,
other-party, duplicate, malformed-list and uninstall cases pass.
The Windows x64 DLL builds with four exports and eight imported DLLs.
GPU allocation/submission, most menu drawing, native cleanup and Rust
startup/dispatch are harness substitutes. This build has not been run inside
KH1 on Windows; final appearance, focus transitions and feel need a game test.
Source, rebuild inputs, incremental bundle, licenses and receipts are included.
Current results are in validation.json; older results are historical.

UNINSTALL OR ROLL BACK
Use v61's uninstall path before disabling it or reverting to an older build:
set remove_dual_wield=on in kh1-dual-wield.ini, load/save with v61, then close
KH1, disable the package and Build again. The style token is removed and the
seven missing normal ability entries are restored where there is space.
Sora's Scan/Guard/Roll are restored UNEQUIPPED to preserve the AP budget;
shared movement is restored equipped. Existing copies keep their flags.
If a learned list has since filled, no other ability is evicted. The log names
any restoration shortfall. Native storage cannot hold more than its capacity.
Never run two versions of the Styles DLL together.
