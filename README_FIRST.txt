KH1FM STYLES v64 / s403 - FOOTER FIX AND VENTUS TYPE G

INSTALL
1. Close KH1. Disable v63 or any older main Styles/Dual Wield package.
   Keep standalone Aqua/Terra tests and the full KH2 Combat DLL disabled.
2. Import this ZIP into OpenKH Mod Manager. Enable v64, Build and launch
   with Panacea. Retain existing KH2FM resources/settings for older stances.
3. Confirm s403 / STANCES v64 in kh1-dual-wield.log beside the executable.
   The new native UI/body adapter targets the supplied Steam Global build.

DESCRIPTION AND AP FOOTER
Descriptions now use the normal inset, measured word wrapping and fixed line
spacing. Native leading/font/position commands no longer send later lines
down the page. Up to three lines fit in the left footer; long help ends in ...

Passives and Limits show AP Used in a separate right footer column. The label
is white at size16 and spent/max numbers are white at size22, compared with
size12 previously. Long totals shrink only enough to fit the column. The
display is moved up to avoid clipping at the bottom. Both use Sora's current
native AP budget and update on equip/remove. Limits remains empty, using the
same budget; it has no separate AP pool. Stance and Outfits omit the AP total.

VENTUS - TYPE G
Customize -> Stance -> Type G now equips Ventus's initial BBS moveset test.
It uses the original53-bone model and animation banks from the returned
Ventus capture, fitted onto Sora's native293-bone body.

Ground combo:300,301,302. Air combo:305,306,307.
Guard:400. Dodge Roll:009. Ground casting:354. Air casting:355. Items:600.
Locomotion, combat poses, jumps, ledges, falling and landing are also mapped.
VENTUS_ANIMATIONS.csv lists all37 mapped native records, source frames/ranges,
bank names, requests and native durations. All listed BBS clips are30fps.

KH1 retains action selection, hitboxes, spell/item/Guard events, contact timing,
travel, collision and damage reactions. The bodies are retimed to existing
KH1 clip durations. Native Glide and Superglide remain available. Terra's
Square dash and special recovery variants remain confined to Type F.
This is an initial animation mapping for game testing; source fit checks do
not establish mesh/grip clearance or matching BBS contact semantics.

STANCES AND NUMBERED ABILITIES
Type G is Single/I, zero AP, between Type F and Type H?. It uses former test
slot115, which is no longer shown as a numeric passive. All previous stance
names, IDs and saved codes remain. The other50 placeholders66..114 and127
remain visible and cost0 AP. Their test flags still use the mod-wide
kh1-numbered-abilities.ini file. The former115 test flag is ignored; it cannot
equip Type G or shift another flag. ID127 and other saved selections retain
their meaning. Confirm Type G to equip it explicitly.

Type A..G use one weapon, H?/I?/K?/L? use two, M? uses none. Armed types
retain KH1 spell execution (I); M? uses0. Original native definitions/AP costs
remain. Passives opens Sora directly; Confirm toggles the row, Back returns
to Customize, then the main menu. A stance still uses one hidden native save
token, and inserting it requires free capacity in the48-byte learned array.
There are at most98 Passives rows:48 normal native entries plus50 numeric.

Scan, Dodge Roll, Guard, High Jump, Mermaid Kick, Glide and Superglide remain
active without AP or learned slots. Room/action gates and stance replacements
still apply. All190 retained native/Terra/variant body-part payloads match v63;
Single E's payload and both E/F action controllers are unchanged.

As requested in earlier versions, non-Sora member1..9 learned ability arrays
are removed and their equipped-ability queries suppressed. Saving retains this
removal. Stats, equipment, items and AI/customize settings remain. Uninstall
does not reconstruct the removed partner lists or reuse their arrays.

TEST / REPORT
Check Combo Master's description and a longer description. Lines should stay
inside the left footer; the larger AP total should be white on the right in
both Passives and Limits. Check native AP costs and toggles.
Equip Type G, return to the field and stand idle for the body switch. Test
movement, both combos, Guard, roll, casting/items, jumps and Glide/Superglide
in normal Sora and Olympus rooms. Check switching to F/E and back after an
action. Return kh1-dual-wield.log and a screenshot/video for remaining issues.

VALIDATION
632 Rust tests across30 nonempty suites and145 final-PE adapter checks pass:
98 F/G/menu/ability and47 E. All37 G records apply/restore in both supported
banks with raw and relocated pointers; tests check F dash retirement, ordinary
G Square/movement, native Glide/Superglide eligibility and stable numeric flags.
Footer tests verify native command operands, line positions, width/truncation,
white AP color and16/22 font parameters. Existing AP/native paging regressions
pass. Windows x64 builds with4 exports and8 imported DLLs.

Conversion bounds: max pose error2.445 model units, basis error0.050,
segment-length error below4.1e-11, zero scale error and zero root-helper error.
The harness substitutes Windows APIs, rendering submission and shared Rust
dispatch. Actual Windows/game/GPU execution, mesh/grip alignment, combat feel
and live switching remain for testing. Current receipts are validation.json
and source/STYLES-V64.MD; older receipts are historical. Exact rebuild inputs
and a full64-commit source patch are included. See source/SINGLE-G.MD for
optional conversion regeneration from the original private source assets.

UNINSTALL / ROLLBACK
Use the explicit uninstall path before disabling or reverting: set
remove_dual_wield=on in kh1-dual-wield.ini, load/save with v64, close KH1,
disable the package and Build again. This removes the hidden stance token,
including Type G. Built-in normal entries are restored where capacity permits:
Sora's Scan/Guard/Roll unequipped, shared movement equipped. No unrelated
ability is evicted. Partner abilities stay removed. Numbered flags stop
overriding queries and are not written into the game save. Keep/delete the
numbered settings file as desired. Never enable two Styles DLLs together.
