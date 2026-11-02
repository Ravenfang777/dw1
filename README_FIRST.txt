KH1FM TEN STYLES -- PROTOTYPE v53 (s392)

Single E is the main Aqua v21 ability setup in the Dual Wield style system.

INSTALL
1. Close the game completely. Disable v52/older Dual Wield builds and the
   standalone Aqua Animation Test. Use only this v53 package.
2. Import this ZIP in OpenKH, enable it, Build and Run with Panacea.
   Keep your existing KH2FM resources/settings for the older styles.
3. Load a save. Equip Style: Single E (0 AP). New entries start unequipped.
   The other nine style entries and their saved IDs are retained.
4. Confirm s392 / PROTOTYPE v53 and SINGLE E READY in kh1-dual-wield.log
   beside the game executable. Restart after DLL changes; F1 cannot reload it.

SINGLE E
- Main Aqua v21 only; one equipped weapon. No numbered Aqua test entries.
- Ground combo300/301/366; air305/407/353.
- Second ground attack ends at source30; finisher begins at source15.
- Circle/Jump tap in free air starts504: 1.5x animation/movement speed,
  same travel distance and slight lift; once per airtime, reset on landing.
- Ordinary held Glide is replaced. Native Superglide remains usable.
- Normal and High Jump height +25 percent.
- Guard400 forward/reverse, source30fps; wider all-angle native shield,
  plus12 native ticks of release/parry grace. Native Guard must be equipped.
- Same Aqua casting, idle/run/item/fall poses and visual corrections as v21.
  Magic/effects use the native keyblade tip. Blizzard keeps its native spell
  logic/events with the Fire visual. Native KH1 damage reactions retained.
- Native Guard, Dodge Roll, High Jump and Superglide abilities are not granted
  by this style; equip the native abilities needed for the actions you test.

SWITCHING / TEST
Finish the current action and stand idle to complete a pending style switch.
The native bodies and cast lookup restore before another style takes control.
Test Single E combos, magic, Guard from behind, jump, one air dodge followed by
another press (blocked until landing), Superglide, and switching back to your
previous style. Also try a room change and both your normal/Olympus saves.
Return kh1-dual-wield.log with any issue. No live KH1 playtest was possible here.

VALIDATION / SOURCE
622 Rust tests in29 nonempty suites plus46 final-PE adapter checks pass.
Windows x64 release builds,4 exports/8 imported DLLs. Shared Rust dispatch is
mocked in the PE tests; native event/jump/Glide excerpts are executed offline.
See validation and source/SINGLE_E.md for limits, source patch and rebuilding.
Single E's adapter targets verified Steam Global; older style Epic routes remain.
Keep older packages as rollback. Do not run a second Aqua/Dual Wield DLL.

UNINSTALL
Set remove_dual_wield=on in your existing kh1-dual-wield.ini, load/save with
v53, close the game, disable the package and Build again. It removes only the
custom style IDs117..126 and keeps native abilities. Other INI settings remain.
