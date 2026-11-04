KH1FM STYLES v58 / s397

INSTALL
1. Close KH1. Disable v57 (or any older main Styles/Dual Wield package).
   Keep standalone Terra/Aqua tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v58, Build, and launch
   with Panacea. Keep existing KH2FM resources/settings for older styles.
3. Confirm s397 / v58 in kh1-dual-wield.log beside the executable.
   This native menu/Single F adapter targets the supplied Steam Global build.

STYLES SLOTS
Styles remains directly below Customize and uses the normal blue menu palette.
Primary shows the equipped style. Select it to list all eleven styles plus None.
Confirming a style equips it exclusively; None returns to the normal moveset.
Secondary and Tertiary show Empty and are reserved for future customization.
They do not offer style choices or have an effect yet.
Cancel from the picker returns to the slots without changing the selection;
cancel from the slots returns to the party menu. Native button-swap settings apply.
Normal Abilities retains its native abilities and AP, with custom styles hidden.
Native equipment/items and AP are not used for the new reserved slots.

SINGLE F AIR DASH
A fresh airborne Square tap starts one dash. Sora keeps facing the initial
stick direction throughout it; neutral stick uses his initial facing.
Opposite stick input during the dash cannot turn him. Movement remains39 ticks
at speed16, requested distance624, with native collision and Superglide visual.
Landing alone refills the once-per-airtime use. Normal Glide remains available.
L1/LB + Square and the active magic-shortcut menu do not dash or consume the
use. Native casting retains its Square input. Release Square after a shortcut
before making a genuine dash press. Damage/casting/end release the facing lock.

TEST / REPORT
- In Styles, choose Primary and a style, then None. Secondary/Tertiary stay Empty.
- Check normal Abilities and Equipment for their usual behavior and AP display.
- With Single F, jump and cast with L1/LB + Square: magic should not dash.
- Release the buttons, then tap airborne Square toward a direction. Move the
  stick elsewhere during the dash: Sora should keep the initial facing.
- Try another tap before landing, then land/jump/dash again several times.
If an issue remains, send the new kh1-dual-wield.log and describe the action.

RETAINED SETUP
Other confirmed changes remain: short style names, Styles-only AP removal,
Anti items with combat idle,75% aerial-dodge visual rate in Singles A/C/E and
Duals C/D, Single E's smoother second ground hit, existing combos/magic/Guard
and jump settings. Both generated animation payload headers are unchanged.

VALIDATION
627 Rust tests in30 nonempty suites and100 final-PE checks pass:53 F/menu,47 E.
Original native focus, selected-row, confirm and close-chain routines execute
in the harness. Tests cover turning, magic shortcuts, slot selection/None,
reserved slots, cancellation, swapped buttons, native abilities/AP, source reuse,
exact dash distance and repeated landings. The delivered v57 binary fails the
new facing and shortcut reproduction cases. Windows x64 release builds with
four exports/eight imported DLLs. Rendering/navigation and Rust dispatch are
mocked; Windows startup and final in-game visuals/feel are not run here.
Source, rebuild inputs, incremental bundle, licenses and receipts are included.
Older validation files are historical; current results are in validation.json.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Never run two versions of the Styles DLL together.
