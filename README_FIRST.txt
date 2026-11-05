KH1FM STYLES v69 / s408 - TYPE F DAMAGING AIR DASH

INSTALL
Close KH1. Disable v68 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v69, Build and launch with Panacea. Keep the existing
KH2FM resources/settings required by the other stances. Standalone Aqua/Terra
and full KH2 Combat DLLs remain disabled. Confirm s408 / STANCES v69 in
kh1-dual-wield.log. This native adapter targets the supplied Steam Global build.

TYPE F AIR DASH
Type F now copies Type G's damaging Ventus330 air dash, with ordinary weapon
grip. Tap Square in the air. It travels1.5x Type G's current distance:702 vs468
unobstructed native units. Speed24 vs16 keeps the same29.25-tick duration and
animation timing. Native collision may shorten travel.

The initial stick/facing direction stays locked. Use once per actual airtime;
landing resets it. L1/LB magic shortcuts and the active shortcut menu cannot
start/spend the dash. Casting, damage and script exclusions remain. Ordinary
held Glide is usable after the dash; the tap dash replaces held Superglide.

Damage uses the same physical blade-contact/native damage path as G. The blade
must reach the enemy. One successful contact per enemy per dash; rejected
contacts may retry. Normal F combos and their contact/reaction behavior remain.

RETAINED
G's330/410 speed/distance, reverse grip, two attack-contact passes and mappings
remain. Ventus66..100/Dark Riku101..104 previews, other stances, Customize,
Passives, AP and seven built-in abilities remain. Previously requested removal
of non-Sora abilities remains; saving persists it and uninstall does not restore
the partner ability lists.

CHECK IN GAME
After changing stance, stand idle for the safe body handoff. Check F's Square
330 dash against an enemy, locked facing, once-per-airtime reset and L1+Square
shortcut casting. Then check F -> G -> another stance and ordinary Glide.

647 Rust tests/30 suites and167 final-PE checks pass (119 shared,48 E).
Unchanged37-profile/G-action/038/E payloads are byte-verified. Source, hashes
and validation are included. See source/STYLES-V69.MD for exact scope.
No Windows/game/GPU session was run here; appearance and actual HP damage
still need an in-game check.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v69, close KH1,
disable the package and Build. Existing native-entry restoration/capacity
rules and numbered-flag behavior remain as described in prior versions.
