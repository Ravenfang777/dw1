KH1FM STYLES v62 / s401 - NUMBERED SORA PASSIVES

INSTALL
1. Close KH1. Disable v61 or any older main Styles/Dual Wield package.
   Keep standalone Aqua/Terra tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v62, Build and launch
   with Panacea. Keep your existing KH2FM resources/settings for older stances.
3. Confirm s401 / STANCES v62 in kh1-dual-wield.log beside the executable.
   The native menu/ability adapter targets the supplied Steam Global build.

ALL UNUSED ABILITY IDS
Passives now includes all51 previously blank IDs:66 through115, then127.
Each is named its decimal number and costs0 AP. The existing native definitions
and stance names/IDs remain. These numbered entries are test placeholders;
no combat effects are assigned yet. Confirm toggles their equipped marker.
They are all available immediately, regardless of Sora's level or learned-list
space. Existing normal abilities keep their names and native AP costs.

The numbered flags are stored in kh1-numbered-abilities.ini beside the game
executable. These are MOD-WIDE test settings shared between saves. They use
no native learned slots. With the game closed, delete that file to reset them.
The file is created when a selection changes; unchanged frames do not write it.
Enabled legacy numeric entries in Sora's list migrate into these settings.

DIRECT SORA PASSIVES
Main menu: Items -> Customize -> Equipment -> Shortcuts, then native options.
Customize categories: Stance, Passives, Limits, Outfits.
Choose Passives to enter Sora's ability list immediately. The Sora/Donald/Goofy/
Shared selector is skipped entirely. Sora's learned native entries come first,
followed by all51 numbered entries. Scroll down to reach115 and127.
Eight rows show at once; the list supports up to99 rows without enlarging the
48-byte native save array. Existing full native lists can toggle flags without
adding a new token; new stance insertion still requires free native space.

Confirm directly equips/removes the selected row. Normal abilities use native
AP cost/free-AP queries, and equipping is refused if AP is insufficient.
Their native descriptions and AP budget are shown. Numbered rows showAP0 and
can all be selected with zero available AP. The native equip/sort popup is
replaced by direct toggling. Back returns to Customize's category column;
Back again returns to the main menu. Stance selection and scroll are retained.
Limits and Outfits remain empty. Original native Customize is still Shortcuts.

PARTNER ABILITY REMOVAL
All learned abilities for non-Sora member IDs1..9 are automatically removed,
including inactive partners. Their equipped ability queries return0. Abilities
awarded later are blocked immediately and removed on the next update.
Only the learned-ability arrays are cleared. HP/MP, experience, stats, equipment,
items and AI/customize settings are retained; basic commands/spells are not
separately deleted. Saving retains this removal. Uninstall DOES NOT reconstruct
the deleted partner ability lists. Their arrays are not repurposed as storage.

BUILT-IN ABILITIES / COMBAT
Scan, Dodge Roll, Guard, High Jump, Mermaid Kick, Glide and Superglide remain
available without AP or learned slots, even with no stance equipped. Normal
room/action/swimming restrictions and stance movement replacements still apply.
Both animation payloads and E/F action controllers match v61. All eleven stance
names, existing combos, spell effects and dash/shortcut behavior are retained.

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
Question marks are intentional. I means KH1 spell execution, II KH2,0 no magic.
Current armed stances execute KH1 spells; imported cast poses/FX are visual.

TEST / REPORT
Open Customize -> Passives. It should enter Sora's scrollable list with no
member selector. Check normal ability names/AP, then scroll through every
number from66..115 and127. Toggle numbered entries, including127. Their AP
cost must be0 and ordinary AP availability should not change. Restart to check
the mod-wide test selections. Check Stance/Back transitions and normal combat.
Partners should have no learned abilities. The seven built-ins should work
with no stance equipped and retain each stance's existing replacements.
Return the new kh1-dual-wield.log and a screenshot/video if a problem remains.

VALIDATION
631 Rust tests/30 nonempty suites and137 final-PE checks pass:90 F/menu/ability,
47 E. All51 numeric IDs and flags,99-row lists, zero-AP toggles, native AP
queries, original paging beyond48, partner boundaries, migration, settings
serialization and callback payloads are checked. The Windows x64 DLL builds
with4 exports and8 imported DLLs. Source and exact rebuild inputs are included.
The harness substitutes Windows APIs, rendering and shared Rust dispatch.
Actual Windows file replacement, native graphics, focus and gameplay remain
for a live game test. Current receipts are in validation.json; older files
are historical. STYLES-V62.MD explains scope, sources and limitations.

UNINSTALL OR ROLL BACK
Use v62's uninstall path before disabling it or reverting: set
remove_dual_wield=on in kh1-dual-wield.ini, load/save with v62, close KH1,
disable the package and Build again. The style token is removed. Missing
normal built-in entries are restored where space permits: Sora's Scan/Guard/
Roll UNEQUIPPED to preserve AP, shared movement equipped. No unrelated ability
is evicted to make room; any shortfall is logged. Partner abilities stay
removed. Numbered flags stop overriding queries and are not written into the
save. Keep or delete kh1-numbered-abilities.ini as desired.
Never enable two versions of the Styles DLL together.
