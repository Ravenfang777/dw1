KH1FM STYLES v73 / s412 - NINE OVERDRIVES, HAND FOLLOW AND FOOTSTEPS

INSTALL
Close KH1. Disable v72 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v73, Build and launch with Panacea. Keep existing
KH2FM resources/settings. Standalone Aqua/Terra and full KH2 Combat DLLs stay
disabled. Confirm s412 / STANCES v73 in kh1-dual-wield.log. The native adapter
targets the supplied Steam Global build. Restart after updating the DLL.

OVERDRIVES
Nine choices in your requested order, each with its own Drain number and
exact future-effect description. See OVERDRIVES.txt and OVERDRIVES.csv.
Eight rows are visible; scroll down to reach Spite. One selected at a time,
free of AP/native ability slots and independent of Stance. Select its active
row again to turn it off. The header stays Customize; Appearance remains.
Descriptions state FUTURE functions. No buffs, healing, invincibility, free
magic, damage/speed changes or Drain resource deductions are implemented yet.

The requested nine-color set replaces older palette defaults automatically.
Old settings cannot keep Will blue. The next selection save writes palette
version2 and all new color keys, keeping the choice/other settings. Later
custom version2 colors persist normally. Existing selection IDs are stable:
Power->Might, Brilliance->Prowess, Rage->Spite; Will/Resistance remain.

HAND EFFECT FOLLOW
Visible continuously bound Overdrive roots now refresh immediately before
draw using the latest witnessed pose. Effect clocks/RNG/alpha/particle history
do not advance again. Detached particles, authored wind trails and script
anchors retain their placement. Valor/Wisdom wind remains, with Wisdom foot
sparkles and shared Anti darkness excluded as in v72. Live fast-motion hand
tracking still needs an in-game check; no static hand offset was added.

FOOTSTEPS
Native footstep/material-movement sounds are muted for all actors/kinds,
including steps accidentally triggered during attacks and shared stop/jump/
landing material sounds. Known imported walk/run sounds are also suppressed.
Attack, impact, weapon, magic, voice, music and push/contact audio paths remain.
Check FOOTSTEPS MUTED: native step routine installed=true in the log.
The supplied Steam executable matches the checked native step entry.

RETAINED
All stance/numbered animation mappings, E jump/GC2/Cure/dodge controls, F body
dash contacts, G reverse grip/two-pass contacts and Passives AP behavior stay.
Both generated animation headers remain byte exact to v72. Previously requested
non-Sora ability removal remains permanent when saved; uninstall does not
reconstruct partner lists. Stand idle for safe stance handoffs.

VALIDATION / LIVE CHECK
660 Rust checks/30 suites and172 final-PE checks pass (123 shared,49 E).
Checks cover nine labels/Drain/help, exact percent/comma output, native scrolling,
palette migration, near-black policy, opt-in bound-root refresh without time/
RNG/alpha advancement, and the checked native footstep signature. Windows x64
release, full source reconstruction, ZIP CRC and file hashes are verified.
No Windows/game/GPU/audio session ran here. Check glows during fast movement,
all nine shades, help/glyph fit and absence of footstep sounds during attacks,
walking/running/landing, with attack/impact/music still audible.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v73, close KH1,
disable the package and Build. Removal mode restores step-sound routing.
Existing ability restoration/capacity rules remain.
