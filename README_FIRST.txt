KH1FM STYLES v54 / s393 - TEST BUILD

INSTALL
1. Close KH1. Disable the previous main Styles/Dual Wield package, standalone
   Terra/Aqua animation tests, and the full KH2 Combat DLL.
2. Import this ZIP into OpenKH Mod Manager. Enable it, Build, launch with
   Panacea. Keep existing KH2FM resources/settings needed by older styles.
3. Pause > Styles > Style: Single F (0 AP) selects Terra. Styles appears
   immediately after Abilities. The normal Abilities screen contains normal
   abilities; style choices are shown only in Styles. Select an enabled style
   again to turn it off. Only one style can be active.
4. Log beside the executable: kh1-dual-wield.log. Confirm s393 / v54,
   STYLES MENU READY and SINGLE F READY. Restart after DLL changes.

SINGLE F / TERRA
- Main Terra v4 setup retained: ground300/411/332; air305/306/353.
- Fire/Blizzard/Gravity315 ground,316 air. Cure/Thunder/Aero/Stop317 ground,
  318 air, including corresponding recovery animations.
- Guard354; items399; ground slide009; idle skull tilted up15 degrees.
- Fresh airborne Square: same tested direction/distance/speed as Terra v4,
  now using KH1's original Superglide animation. One dash per airtime.
  Completion, release, damage or changing styles cannot refill it; land first.
- Replaces held Superglide. Ordinary held Glide stays usable.
- Native damage/knockback, collision, hit/magic events and keyblade-tip effects
  remain. Native Guard/Dodge Roll abilities are not granted by this style.

STYLES MENU
Singles A-F, Duals A-D, Anti: eleven zero-AP choices. Existing style IDs and
saved choices are retained. Style rows use a private view. Saves keep one
hidden style token instead of many style entries, preserving native copies,
equip flags and AP. Donald/Goofy's normal Abilities retain their native view.
A completely full47-native-ability list cannot persist a new style token;
it is never evicted to make room. Malformed native tails are also retained.
Only the main Terra profile is integrated; numbered Terra tests stay separate.

TEST / REPORT
Finish an action and stand idle to complete a pending style switch. Test menu
entry/back navigation, native ability equip/unequip, Single F combos/magic,
one Square dash followed by a second press before landing, and another dash
after landing. Try Terra > Aqua > another style, a room change, and both your
normal/Olympus saves. Return the log with issues.
The native menu's final layout/navigation and live game transitions still need
your in-game check. No Windows game/GPU session was available here.

VALIDATION / SOURCE
624 Rust tests in30 nonempty suites;36 final-PE Terra/menu checks and46 Aqua
regressions pass. Includes native ability-record prologue execution, body and
request restoration, UI filtering/equip commits, native Superglide source
admission, dash budgets and resource transitions. Rendering/shared Rust
routing are mocked in the C harness. Windows x64 release:4 exports,8 DLL imports.
Source patch, incremental git bundle, rebuild inputs and receipts are included.
New adapters/menu target verified Steam Global. Older Epic routes remain.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Do not run standalone Terra/Aqua alongside this DLL.
