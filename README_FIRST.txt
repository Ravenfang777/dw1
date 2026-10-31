KH1FM SEVEN STYLES -- PROTOTYPE v30 (s369)

INSTALL
1. Fully close KH1FM. Disable v29 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v30, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s369 / PROTOTYPE v30 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod. Keep the full KH2 Combat overhaul,
older offhand/moveset Lua and duplicate Sora model mods disabled. Use
normal Sora. Existing kh1-dual-wield.ini is preserved. No game assets ship.

DUAL C: KH2 SORA GUARD
The user confirmed v29's playable Roxas moveset works. Its resource loader,
two-hand body map and authored combo adapter are unchanged. Dual C now uses
base KH2 Sora's actual Guard press animation when KH1 commits Guard.
Equip KH1's Guard normally; this style does not grant the ability.
Native blocking, timing, ability gates and Guard/Roll choice remain KH1's.

Guard has a separate Sora body calibration, so its bones are never measured
as Roxas's. The duplicate follows the final drawn hand without an imported
Guard attack/hitbox. Native held-attachment initialization uses the correct
selected Roxas/Valor idle rig and a separate cache. Confirmed Glide draw,
alignment/colors, Dual A Superglide finisher and Dual B actions are retained.

NEW: STYLE: SINGLE C
New ability id 120, 0 AP, initially disabled. Equipping it cancels every
other style. It uses playable final-battle Riku, P_EH000_LAST (2257), with
his actual declared/shared motion bank, NeoMoveset and SKLT hand metadata.
The rig reads his W_EH000 weapon skeleton/collision and WMST motion tracks.
You still see Sora and your equipped KH1 weapon. There is no duplicate,
Riku model, forced Way to Dawn, gauge, costume, stat bonus or extra ability.

Riku has a separate mapped body calibration. An available free-hand SKLT
joint is used only as a body landmark; otherwise a mirrored finger-bearing
palm is inferred and checked by the complete existing body map. Weapon leaf
helpers may calibrate from nearby palms. Actual weapon attachments, motion
channels and collision bones keep their native indices. No Sora-indexed
hair/hood map is applied to Riku; weapon-chain secondary motion is retained.

Base ground/aerial melee uses Riku's authored primary-weapon rows and timing.
Only native KH1 Combo Plus/Air Combo Plus policy carries into those attacks;
equipped native attack abilities keep the established native combo priority.
Matching idle/run/walk/jump/fall/land/ledge/item/damage/scene/Roll poses overlay
where present. Riku Guard press is optional and retains native blocking.

KH1 spell casts and normal Glide/Superglide remain native for Single C.
Missing Riku slots also remain native. Dark Aura, limits, party AI, special
commands and donor effect scripts are not added in this test build.

FIRST TEST
1. Fresh process: equip Dual C and native Guard. Try Guard, ground and aerial
   combos, then standard Glide. Dual C should keep the working Roxas attacks.
2. Equip Style: Single C. Confirm the other style switches off and there is
   only one equipped weapon. Test idle/run/jump and ground/aerial combos.
3. Test a native spell, Guard, an area change and unequipping Single C.
4. Startup should report:
   SINGLE C ASSETS READ ... primary_hand=... free_hand_metadata=...
   SINGLE C RIG MAP ADMITTED ... core_parts=17 ...
   SINGLE C DONOR LOADED ... ground_rows=... air_rows=...
   SINGLE C DATA ... playable final-battle Riku=true attack_adapter=true
The menu entry alone does not prove donor admission. Return the full fresh
log including startup if Riku stays native, a pose is wrong or it crashes.
Resource/map rejection logs an exact reason; no other moveset substitutes.

RETAINED
Seven exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed),
Dual C 121 (playable dual Roxas), Single C 120 (playable final-battle Riku).
Only the three Dual styles duplicate the currently equipped weapon.
A's actual Superglide finisher, B's Quick Run/Guard/Fire/FX, Single B Run .75,
Anti's aura/restrictions and the confirmed Glide fix remain.

INI defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Offhand-only testing affects Dual weapon contacts. Single C has no offhand.
To remove custom entries: set remove_dual_wield on; launch/load/save with
v30; close; disable the mod and Build again. Only our seven custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
488 tests pass across 31 suites (155 style tests). New coverage includes
seven-way exclusivity and uninstall, exact playable Riku profile/shared bank,
nonplayer/path rejection, free palms/weapon helpers, separate canonical Guard
and mapped combo outputs, row-11 preservation, primary-only ground/air contact
lifetime and no special-script/ability grants. The existing Win64 Guard bridge,
Glide, Fire and Quick Run tests remain. Windows x64 release, PE interface,
164 scope/preservation checks, 11 native anchors and seven protected-model
metadata checks pass. ZIP CRC, independent extraction and saved-copy hashes
are verified.

No live v30 game/GPU test or actual installed Riku asset execution was run
here. Synthetic fixtures do not prove that your Riku bank/map is admitted or
every pose renders correctly. Free-hand matching bounds are our inference
rules, not KH2 constants. The supplied build is ready for that game test.
Source patch, pinned upstream, credits/licences and validation receipts are
included. No game executable, recording, extracted asset or disassembly ships.

Data identity/format sources (OpenKH):
https://openkh.dev/kh2/dictionary/obj.html
https://openkh.dev/kh2/file/type/00objentry.html
https://openkh.dev/kh2/file/type/03system.html
Detailed rules/confidence: docs/combat-model.md Stage 369 in the source patch.
