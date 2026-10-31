KH1FM SIX STYLES -- PROTOTYPE v28 (s367)

INSTALL
1. Fully close KH1FM. Disable v27 and all older Dual Wield prototypes.
2. Import this ZIP into OpenKH, enable ONLY v28, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s367 / PROTOTYPE v28 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not Lua. Keep the full KH2 Combat
overhaul, older offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied.

DUAL C RIG ADMISSION FIX
Both supplied s366/v27 logs get past filename/resource loading, then
reject Roxas: body anchor 10 differs from the admitted retarget layout.
The donor and attack_adapter remain false, so no imported moveset ran.

That check required Roxas's parent indices to match Sora's exactly.
The actual retarget measures positions and calibrates from each donor's
own bind skeleton. v28 validates the relevant body geometry instead:
required joint locations, finite/nonsingular matrices, proportional
bounds and 17 usable core body-part frames. Different parent links or
wardrobe bone counts alone no longer reject the donor.

The real retarget constructor/pose methods are unchanged; C already uses
Roxas's own hierarchy and bind for its calibration. Wrong, missing or
degenerate body landmarks are still rejected. This does not substitute
Sora/Valor animations or merely remove every rig check.

CONFIRMED GLIDE AND WORKING STYLES ARE UNCHANGED
Full Glide attachment/color renderer, ability policy, combo controller,
A's actual Superglide finisher, B's working Quick Run/Guard/Fire/effects,
C's filename resolver and existing retarget methods match v27.

FIRST TEST
1. Fresh process; equip Style: Dual C.
2. Check idle/run and jump, then a basic ground and aerial combo.
3. Successful startup should show:
   DUAL C ASSETS READ ... bones=... weapon_joints=...
   DUAL C BIND GEOMETRY ADMITTED ... different_parents=...
   DUAL C DONOR LOADED ...
   DUAL C DATA ... playable dual Roxas=true attack_adapter=true
Equipping the menu entry alone is not proof the donor loaded.

If rejected or still acting native, return the FULL fresh log including
startup before restarting. New notes show the actual loaded resource,
bone/motion/row counts, weapon joints and measured geometry failure.
Native KH1 attack abilities deliberately keep their existing combo lane;
missing Roxas visual slots, spells, Guard and Roll retain native behavior.
The confirmed Glide fix needs no further exploratory changes.

RETAINED
Six exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed),
Dual C 121 (playable dual Roxas). Equipping any style cancels the others.
Only A/B/C duplicate the currently equipped weapon. No second weapon
selection, costume, Drive state/gauge, stat reward, extra ability or
party removal. C uses real authored base ground/air two-blade contacts
and matching poses when the installed donor is admitted. Existing native
Combo Plus/Air Combo Plus policy remains. Single B Run .75/Guard, Anti's
weaponless moves/aura and magic/item/summon restrictions remain.

Your existing kh1-dual-wield.ini is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Offhand-only testing affects Dual weapon contacts, not spells or party.
To remove custom entries: set remove_dual_wield on; launch/load/save with
v28; close; disable the mod and Build again. Only the six custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
472 tests pass across 31 suites (151 style tests). New cases reparent
source bone 10 without changing its measured bind position, change
wardrobe count/proportions and compare real moving-arm retarget outputs.
Missing/wrong/singular/nonfinite/degenerate body data is rejected.
Existing filename/controller/Glide/Fire/Quick Run/finisher/Win64 Guard
bridge tests remain. Windows x64 release, PE interface, 11 native anchors,
7 protected-model metadata checks and 148 scope/preservation checks pass.
ZIP CRC/extraction and saved-copy entry hashes are verified.

No live v28 game/GPU test or actual installed Roxas rig execution was
performed here. The proportion tolerance is our validation rule, not a
native game constant. Offline fixtures do not prove that your installed
rig passes the geometry checks or that every donor pose renders correctly.
Source patch, pinned upstream, credits, licences and validation receipts
are included. No game executable, recording, extracted asset or
disassembly is distributed.
