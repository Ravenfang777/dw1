KH1FM STYLES v59 / s398 - CUSTOMIZE STANCE MENU

INSTALL
1. Close KH1. Disable v58 (or any older main Styles/Dual Wield package).
   Keep standalone Terra/Aqua tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v59, Build, and launch
   with Panacea. Keep existing KH2FM resources/settings for older stances.
3. Confirm s398 / STANCES v59 in kh1-dual-wield.log beside the executable.
   This native menu/Single F adapter targets the supplied Steam Global build.

MENU
Items -> Customize -> Equipment -> Abilities -> Shortcuts, then native options.
The new Customize is the previous Styles entry. The original native Customize
is only visually renamed Shortcuts; it retains its original functionality.

The new Customize screen follows the supplied mockup's Abilities layout:
- Categories: Stance, Limit, Outfit, ???.
- Stance: eleven types, eight visible rows, native scrolling/scrollbar and
  equipped marker. Matching weapon and magic boxes replace the AP display.
- Limit, Outfit and ???: no entries yet and no current effect.

Open Stance to select a type. Confirm it to equip it exclusively. Confirm the
currently equipped type again to turn the stance off, like a native ability.
Cancel returns to the categories; cancel again returns to the party menu.
The list keeps its scroll position when returning from the categories.

RENAMED STANCES              WEAPONS   MAGIC
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

The question marks are intentional. Magic markers:0 unavailable, I KH1,
II KH2. Current armed stances execute KH1 magic, including those which overlay
KH2 casting poses/effects. They therefore show I. II is supported for a future
actual KH2-magic stance; this revision does not change spell execution.
Type M? still allows items and blocks magic, as before.

SAVES / RETAINED BEHAVIOR
Saved stance IDs and the single hidden style token are unchanged. Normal
Abilities still hides custom stances and retains native AP costs/totals.
Equipment, inventory, shortcut assignments and other-party abilities are not
repurposed. Empty categories do not reserve save bytes yet.
All v58 combat behavior is retained, including Type F's fixed-facing air dash,
L1/LB + Square shortcut exclusion and once-per-airtime use. Both generated
animation payload headers and the F action/controller source are unchanged.

TEST / REPORT
Check the root order, new titles and the normal Shortcuts configuration.
Open Stance, scroll through all eleven names, equip one, toggle it off and
select another. Both information boxes should stay aligned with each row.
Check that Limit, Outfit and ??? contain no stance entries. Check normal
Abilities/AP and Equipment, then confirm your usual combat still works.
If an issue remains, return the new kh1-dual-wield.log and a screenshot or
short video of the action/layout concerned.

VALIDATION
627 Rust tests in30 nonempty suites and104 final-PE checks pass:57 F/menu,47 E.
Original native paging reaches the last entries and wraps. Native index,
offset, confirm, normalization and close routines also execute. Tests cover
root cursor IDs, title routing, row alignment, selection/unequip, reserved
categories, save boundaries and prior combat regressions. Windows x64 builds
with four exports/eight imported DLLs. Rendering, Windows startup and Rust
dispatch are mocked; final in-game appearance/feel remain to be tested.
Source, rebuild inputs, incremental bundle, licenses and receipts are included.
Older validation files are historical; current results are in validation.json.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Never run two versions of the Styles DLL together.
