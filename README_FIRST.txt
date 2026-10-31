KH1FM SIX STYLES -- PROTOTYPE v27 (s366)

INSTALL
1. Fully close KH1FM. Disable v26 and all older Dual Wield prototypes.
2. Import this ZIP into OpenKH, enable ONLY v27, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s366 / PROTOTYPE v27 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not Lua. Keep the full KH2 Combat
overhaul, older offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied.

DUAL C LOADER FIX
Your s365/v26 log confirms the Dual C entry equipped, but the Roxas donor
was rejected before loading: dual Roxas motion filename invalid.
The log then reports attack_adapter=false and native KH1 attack rows.
The held-blade Glide path is independent, which explains why it worked
without Roxas's actual animations and attacks.

v27 accepts an absent animation override by reading the playable dual
model's own P_EX110_BTLF.mset. Complete archive names are normalized once,
without double prefixes/extensions. An unusable override is never passed
as a path: only that same known dual Roxas model's bank is attempted.
Playable-object identity, actual moveset, both weapon tracks and valid
body/combo/motion checks still apply. No Valor or boss substitute.

The original rejected string was not printed by v26, so its exact value
is not established. New diagnostics include declared name, resolved path,
source/origin and moveset, including original rig-reader failures.

CONFIRMED GLIDE FIX IS UNCHANGED
The full Glide attachment/color renderer and policy match delivered v26.
No change to A's actual Superglide attack finisher, B's working Quick Run,
Guard, Fire/effects, C's combo adapter/controller or ability selection.

FIRST TEST
1. Fresh game process; equip Style: Dual C.
2. Check idle/run and jumping, then one ground and one air combo.
3. Check startup in kh1-dual-wield.log for BOTH:
   DUAL C DONOR LOADED ... motion_file=... origin=...
   DUAL C DATA ... playable dual Roxas=true attack_adapter=true
Equipping the menu ability alone does not prove its donor loaded.
If its data is rejected or attacks remain native, return the FULL fresh
log including startup before restarting. The resolved file and next
failed prerequisite will now be recorded.

Native KH1 attack abilities deliberately retain their normal combo lane.
Missing Roxas visual slots, spells, Guard and Roll retain native behavior.

RETAINED
Six exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed),
Dual C 121 (playable dual Roxas). Equipping any style cancels the others.
Only A/B/C duplicate the currently equipped weapon. No second weapon
selection, costume, Drive state/gauge, stat reward, extra ability or
party removal. C uses authored base ground/air two-blade contacts and
matching poses when the installed donor is admitted. Existing native
Combo Plus/Air Combo Plus policy remains. Single B Run .75/Guard, Anti's
weaponless moves/aura and magic/item/summon restrictions remain.

Your existing kh1-dual-wield.ini is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Offhand-only testing affects Dual weapon contacts, not spells or party.
To remove custom entries: set remove_dual_wield on; launch/load/save with
v27; close; disable the mod and Build again. Only the six custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
469 tests pass across 31 suites (151 style tests), including absent and
complete filename resolution, exact-model fallback without forwarding
unsafe paths, and retained six-style/controller/Glide/Fire/Quick Run/
finisher/Win64 Guard bridge regressions. Windows x64 release, PE interface,
11 native anchors, seven model metadata checks and 140 scope/preservation
checks pass. ZIP CRC/extraction and saved-copy entry hashes are verified.

No live v27 game/GPU test or installed Roxas asset execution was performed.
Offline tests do not prove that your installed donor passes all remaining
admission checks or that its poses render correctly. Use the startup and
moveset checks above.
Source patch, pinned upstream, credits, licences and validation receipts
are included. No game executable, recording, extracted asset or
disassembly is distributed.
