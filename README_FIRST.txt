KH1FM STYLES v55 / s394 - TEST BUILD

INSTALL
1. Close KH1. Disable the previous main Styles/Dual Wield package, standalone
   Terra/Aqua animation tests, and the full KH2 Combat DLL.
2. Import this ZIP into OpenKH Mod Manager. Enable it, Build, launch with
   Panacea. Keep existing KH2FM resources/settings needed by older styles.
3. Pause > Styles selects Single A-F, Dual A-D or Anti. Select an enabled
   style again to turn it off. Only one style can be active.
4. Check kh1-dual-wield.log beside the executable for s394 / v55,
   STYLES MENU READY and SINGLE F READY. Restart after DLL changes.

CHANGES
- Remove the Style: prefix from all eleven names. IDs and saved choices stay.
- Styles omits AP costs and the Sora current/max AP panel. Normal Abilities
  keeps its original AP display and behavior. Styles still cost zero AP.
- Single A/C/E and Dual C/D aerial dodge animations play at 75 percent of
  their v54 speed. Movement, travel duration, distance and handoff stay the
  same. Single F is a Superglide air slide and keeps its existing visual rate.
- Anti can use native items again; item use shows its looping combat idle.
- Single F Square dash rearms on each landing. Private native Superglide
  playback data is refreshed before reuse. Still only one dash per airtime;
  completion, release, damage and changing styles cannot refill it midair.
- Single E ground hit2 no longer carries its held-pose tail. The pose fills
  the action continuously; hit timing is retained and the finisher has a
  usable late input window. Other main combo choices remain.

RETAINED SETUP
Single E: ground300/301/366, air305/407/353, Guard400, keyblade-tip magic,
1.25x normal/High Jump height; regular Glide replaced, Superglide retained.
Single F: ground300/411/332, air305/306/353; Fire/Blizzard/Gravity315/316,
other magic317/318; Guard354, item399; idle head up15 degrees. Square uses
native Superglide, speed16/duration39; normal held Glide stays usable.
Native Guard/Dodge Roll abilities are not granted by these styles.
Numbered standalone animation test profiles remain separate.

STYLES MENU / SAVES
Eleven choices use a private menu view. Normal Abilities hides only custom
IDs116..126. Saves keep one hidden style token; native duplicates, equip flags
and AP are retained. Donald/Goofy's normal Abilities retain their native view.
A completely full47-native-ability list cannot persist a new style token;
it is never evicted to make room. Malformed native tails are also retained.
Finish the current action and stand idle to complete a pending style switch.

TEST / REPORT
Check both Styles and normal Abilities, including Sora/party navigation and
normal ability equip/unequip. Test Anti items, repeated F dashes separated
by landings, A/C/E and Dual C/D dodges, and E's second hit into finisher.
Try your normal and Olympus saves plus a room/style change. Return the log
with issues. Final menu layout, live item effects and action feel still need
an in-game check; no Windows game/GPU session was available here.

VALIDATION / SOURCE
627 Rust tests in30 nonempty suites;40 final-PE Terra/menu and47 Aqua adapter
checks pass. They cover repeated landings in both banks, native menu call
sites/branch paths, pointer rollback, hit/chain timing and preserved E travel.
Shared Rust dispatch/rendering and Windows startup are not run in the native
C harness. Windows x64 release has4 exports and8 imported DLLs. Source patch,
incremental bundle, exact rebuild inputs and receipts are included. New native
adapters/menu target verified Steam Global. Existing Epic routes remain.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini, load/save with this DLL, close
KH1, disable the package and Build again. Only custom IDs116..126 are removed;
native abilities remain. Do not run standalone Terra/Aqua alongside this DLL.
