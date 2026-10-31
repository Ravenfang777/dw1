KH1FM SEVEN STYLES -- PROTOTYPE v31 (s370)

INSTALL
1. Fully close KH1FM. Disable v30 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v31, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s370 / PROTOTYPE v31 in kh1-dual-wield.log beside the game EXE.

Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
Sora model mods disabled. Use normal Sora. Existing INI/save style entries
are preserved. No game assets ship; this is an OpenKH native DLL mod.

WHY SINGLE C DID NOT WORK
The supplied s369/v30 log says:
  SINGLE C DONOR UNAVAILABLE: final-battle Riku object is not PLAYER
  SINGLE C DATA: playable final-battle Riku=false attack_adapter=false
The ability equipped, but Riku was rejected before any animation/rig read.
V30 required native object type zero. That was an incorrect condition for
this data-only importer. The actual type was nonzero; v30 did not print its
value, so the log does not establish which specific native class it uses.

V31 CHANGE
Admit the exact unique 2257/P_EH000_LAST body data profile independently of
its native object type. Apply the same data-only identity rule to exact
791/W_EH000 weapon geometry. No KH2 actor, control class, AI, script or
form is instantiated or changed. Other actor IDs/models remain rejected.

All bank/path/NeoMoveset, WMST/SKLT, one-weapon rig/attachment, anatomical
map/core-frame, motion and authored melee checks remain. There is no alternate
Riku/party/boss/Sora substitution, guessed bank/table, remapped gameplay or
new ability. Native type/subtype are retained as diagnostic metadata.

Startup now prints the raw profile before resource reads, including actual
type/subtype, original/resolved bank, NeoMoveset, SKLT and native form. Bad
bank/table errors include that context. After resources load, a bounded
combo summary reports row kinds/motions/air flags/abilities/sub-links and
hit-weapon masks before map/adapter admission. This will expose a later
resource/map/adapter rejection without assuming it has already happened.

FIRST TEST
1. Fresh game process. Stand idle briefly, then equip Style: Single C.
2. Check idle/run/jump, then a basic ground and aerial combo.
3. Expected startup progression:
   SINGLE C PROFILE READ ... native_type=... NeoMoveset=... SKLT=...
   SINGLE C ASSETS READ ...
   SINGLE C COMBO METADATA ...
   SINGLE C RIG MAP ADMITTED ... core_parts=17 ...
   SINGLE C DONOR LOADED ...
   SINGLE C DATA ... playable final-battle Riku=true attack_adapter=true
4. If still native, a pose is wrong or it crashes, return the full fresh
   kh1-dual-wield.log including startup. The entry alone is not admission.

The next resource/map/combo stage still needs actual installed-game testing.
V31 corrects the observed pre-resource rejection; offline tests do not prove
that every following asset/rig check will pass or every pose renders correctly.

PRESERVED
All gameplay policy, ability IDs/exclusivity, body maps/inference, controllers,
contacts, Roxas loading/combos, Dual C Sora Guard, complete offhand attachment
and Glide/color draw, A's actual Superglide finisher and B's Quick Run/Guard/
Fire/magic paths are byte-identical to v30. Only Riku data-profile admission,
bounded diagnostics and version labels change.

Seven exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final), Single A 124
(base KH2 Sora), Single B 123 (Wisdom), Anti 122, Dual C 121 (dual Roxas),
Single C 120 (endgame Riku). Only the Dual styles duplicate the equipped weapon.
Single C remains one equipped KH1 weapon, with matching Riku base melee/poses
when admitted; native KH1 spells, normal Glide/Superglide and missing slots.
No Riku costume, fixed weapon, gauge, stat bonus, special commands, extra
abilities or donor scripts are added. Native attack abilities keep priority.

INI defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
To remove custom entries: set remove_dual_wield on; launch/load/save with
v31; close; disable the mod and Build again. Only our seven custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
490 tests pass across 31 suites (155 style tests). Two new cases cover
nonzero native classifications on the exact Riku identity and raw metadata
in invalid-bank/table errors. Wrong actor/model, ambiguous records, unsafe
paths and missing tables still fail. Existing rig/Guard/Glide/Fire/Quick Run/
contact/controller tests remain. Windows x64 release, PE interface, 132
source/preservation checks, 11 native anchors and seven protected-model
metadata checks pass. ZIP CRC, independent extraction and saved-copy hashes
are verified.

No live v31 game/GPU test or actual installed Riku asset execution was run
here. Source patch, pinned upstream, credits/licences and validation receipts
are included. No game executable, recording, extracted asset or disassembly
ships. Detailed rules/confidence: docs/combat-model.md Stage 370 in the patch.
Object metadata layout: https://openkh.dev/kh2/file/type/00objentry.html
