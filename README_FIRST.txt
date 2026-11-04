KH1FM STYLES v63 / s402 - SPENT AP AND VENTUS SOURCE PREPARATION

INSTALL
1. Close KH1. Disable v62 or any older main Styles/Dual Wield package.
   Keep standalone Aqua/Terra tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v63, Build and launch
   with Panacea. Keep existing KH2FM resources/settings for older stances.
3. Confirm s402 / STANCES v63 in kh1-dual-wield.log beside the executable.
   The native menu/ability adapter targets the supplied Steam Global build.

AP USED / MAXIMUM
Customize -> Passives and Customize -> Limits now show AP Used <spent> / <max>
in the lower information area. Both show Sora's current native AP budget.
Limits is still empty and uses the same budget; it has no separate AP pool.
Equipping/removing normal passives updates the total immediately. Numbered
zero-AP abilities and stances do not spend AP. Stance and Outfits omit this
display. Native AP costs and insufficient-AP checks remain unchanged.

VENTUS / TYPE G - SOURCE REQUIRED
Type G is NOT playable or listed in this build. Ventus's original skeleton
and motion banks have not been received. Existing Aqua/Terra poses cannot
establish Ventus's mappings, and no other stance is relabeled as Ventus.

To provide the missing files:
1. Extract the Ventus_Source_Locator folder from this ZIP somewhere writable.
2. Run Ventus_Source_Locator/RUN_ME.cmd.
3. Select the broad EXTRACTED BBS data folder containing arc AND chara.
   Selecting only pc_ven misses the shared p01base archive and p01ex00 model.
4. Upload the generated Ventus_Source_Capture_....zip beside the collector.

It reads the original files and writes a separate timestamped capture. There
is no automatic upload or game-file edit. It includes the source model,
named gameplay/command banks, relative paths, header inventory and file hashes.
Read/size-limit notes are retained even if no matching banks are copied.
Windows PowerShell5.1+ is required; no Python or administrator access needed.
Packed game containers must already be extracted. The new collector has not
been run on Windows here. See its README_FIRST.txt for details.

RETAINED v62 BEHAVIOR
Main menu: Items -> Customize -> Equipment -> Shortcuts, then native options.
Customize categories: Stance, Passives, Limits, Outfits. Passives opens Sora's
list directly, without the Sora/Donald/Goofy/Shared selector. Confirm toggles
the selected row; Back returns to categories, then to the main menu.

All51 numbered abilities66..115 and127 remain visible, zero AP and without
assigned combat effects. Their mod-wide test selections are stored beside
the executable in kh1-numbered-abilities.ini and shared between game saves.
They use no native learned slots. With the game closed, delete that file to
reset test flags. Normal Sora abilities keep their names and native AP costs.
The eight-row viewport supports up to99 rows without enlarging the48-byte
native learned array. Existing full arrays can toggle flags; adding a new
stance token still requires free native capacity.

Non-Sora member IDs1..9 have their learned abilities automatically removed
and equipped-ability queries suppressed, including inactive partners. Saving
retains this removal; uninstall does not reconstruct their ability lists.
Only the learned arrays are cleared. Stats, experience, items, equipment and
AI/customize settings are retained. Basic commands/spells are not separately
deleted. Partner arrays are not reused for Sora or numeric-ability storage.

Scan, Dodge Roll, Guard, High Jump, Mermaid Kick, Glide and Superglide remain
active without AP or learned slots. Native room/action/swimming gates and
stance movement replacements still apply. All eleven existing stance labels,
combos, magic effects, E/F controllers and animation payloads match v62.

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

TEST / REPORT
Check AP Used in Passives before/after equipping a normal ability. Limits
should show the same current total. Numbered entries must not alter spending.
Check zero/max AP and Back navigation. Return the new kh1-dual-wield.log and
a screenshot if positioning or totals are incorrect. For Type G, return the
collector's Ventus_Source_Capture ZIP so the original motions can be inspected
and retargeted with native KH1 action timing.

VALIDATION
631 Rust tests/30 nonempty suites and139 final-PE adapter checks pass:
92 F/menu/ability and47 E. New checks cover zero, partial, exhausted and
zero-max AP; updates after equip/remove; no-cost numeric rows; matching
Passives/Limits; and no AP display in Stance/Outfits. Existing native paging,
all51 flags, full lists, partner boundaries and both combat adapters pass.
The Windows x64 release builds with4 exports/8 imported DLLs. Source patch,
exact rebuild inputs and current receipts are included. Most rendering,
Windows APIs and shared Rust dispatch are substituted by the harness.
Actual game/GPU execution and the new Windows collector are untested here.
See validation.json and source/STYLES-V63.MD; older receipts are historical.

UNINSTALL OR ROLL BACK
Use v63's uninstall path before disabling or reverting: set
remove_dual_wield=on in kh1-dual-wield.ini, load/save with v63, close KH1,
disable the package and Build again. The hidden stance token is removed.
Missing normal built-in entries are restored where capacity permits: Sora's
Scan/Guard/Roll unequipped to preserve AP, shared movement equipped. No other
ability is evicted. Cleared partner abilities stay removed. Numbered flags
stop overriding queries and are not written into the save. Keep or delete
kh1-numbered-abilities.ini as desired. Never enable two Styles DLLs together.
