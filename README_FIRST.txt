KH1FM STYLES v67 / s406 - TYPE G DISPATCH AND SWITCHING FIX

INSTALL
Close KH1. Disable v66 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v67, Build and launch with Panacea. Keep the existing
KH2FM resources/settings required by the other stances. Standalone Aqua/Terra
and full KH2 Combat DLLs remain disabled. Confirm s406 / STANCES v67 in
kh1-dual-wield.log. This native adapter targets the supplied Steam Global build.

THIS FIX
Type G now reaches the shared Rust Glide/Superglide checks, so native Glide
cannot immediately replace its finite air actions. Its held038 body is displayed
from immutable data, without writing native Glide streams or requiring them
for admission of the37 body records. A failed entry that changed no bodies
cannot hold up unequipping G or selecting another stance. Successfully applied
bodies still restore safely at idle before the next stance runs.

Reverse grip now refreshes at final field model submission as well as after
animation/IK. The attachment uses the skinned wrist and fixed palm/grip offsets,
avoiding stale unskinned helper matrices. Other body/hair/finger poses remain.
The log includes bounded state/request/queue diagnostics for interrupted dashes.

TYPE G MAPPING (UNCHANGED FROM v66)
Ground combo:300,379,411. Air combo:305,306,482.
Ground and air item:395. Held ordinary Glide:038.
Ground Cure/Aero/Thunder/Stop:390. Air:508.
Ground Fire/Blizzard/Gravity:416. Air:417.
Square air dash:330, half Type F distance (312 vs624 unobstructed native units),
locked initial stick direction, native collision, direct Keyblade contacts.
Fresh airborne Circle:410, slight lift; held038 Glide remains after completion.
Release the ground jump button before an aerial Circle tap. Each action is once
per actual airtime; landing resets it. L1 shortcuts, casting, damage and scripts
cannot start these actions.379/411/482 retain their second blade-contact pass.
Source spans/durations are in VENTUS_ANIMATIONS.csv.

PASSIVES AND OTHER STANCES
Working Ventus66..100 and Dark Riku101..104 previews are retained. Equipping a
test unequips stances/other tests; a stance clears the test. Other stance mappings,
menus, normal passive AP, white AP Used/max and seven slot-free built-ins stay.
Stance IDs and native48-byte capacity are unchanged. Numbered test flags remain
in kh1-numbered-abilities.ini. As requested previously, non-Sora ability lists
stay cleared; saving persists this, and uninstall does not reconstruct them.

CHECK IN GAME
After closing the menu, stand idle for the safe body handoff. Check G's combos,
Square330, Circle410, held038 and grip transitions. Then unequip G and select a
different stance. Also check that a numbered preview can replace G and return.

647 Rust tests /30 nonempty suites and163 final-PE checks pass. The actual Rust
Glide callbacks are now exercised in a separate portable regression. Changed
Glide flags and failed entry/exit are covered in both banks.131 immutable038
pose samples match the independent evaluator. All37 shared profiles/variants,
including35 Ventus previews, and E's private payload match v66 byte for byte.

No Windows/game/GPU session was executed here. Live grip appearance, movement
feel and contact-window alignment need your game check. Source, hashes and
validation details are included in source/STYLES-V67.MD and validation.json.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v67, close KH1,
disable the package and Build. The hidden stance token is removed. Built-in
normal entries restore where capacity permits without eviction (Sora entries
off, shared movement on). Partner ability lists stay removed; numbered flags
stop applying when the mod is removed.
