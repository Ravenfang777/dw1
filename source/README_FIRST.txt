KH1FM SEVEN STYLES -- PROTOTYPE v32 (s371)

INSTALL
1. Fully close KH1FM. Disable v31 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v32, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s371 / PROTOTYPE v32 in kh1-dual-wield.log beside the game EXE.

Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
Sora model mods disabled. Use normal Sora. Existing INI/save style entries
are preserved. No game assets ship; this is an OpenKH native DLL mod.

WHY SINGLE C DID NOT WORK
The supplied s370/v31 log confirms that the exact endgame Riku bank loaded:
  SINGLE C ASSETS READ ... bones=209 motions=29 rows=0 ... weapon_bones=12
  SINGLE C RIG MAP ADMITTED ... core_parts=17 ...
  SINGLE C DONOR UNAVAILABLE: Riku authored base ground/air melee rows missing
The imported Riku data has no Sora-style PTYA combo rows. V31 rejected the
whole donor at that point, including its already admitted passive poses.

V32 CHANGE
When the existing row-based adapter cannot run, inspect actual loaded Riku
motion triggers, collision shapes and ATKP records. Qualify physical primary
weapon strikes, including body-stored sword groups only when all their shapes
belong to the actual primary hand. Exclude root/body kicks, mixed groups,
second weapons, magic, reaction-command and ability-gated attack poses.

Construct host combo rows referencing those real Riku poses, root samples,
contact windows, damage records and weapon channels through unused aliases.
Use two alternating base choices and a finisher; each step requires input.
Native Combo Plus/Air Combo Plus extend the existing host controller.
Authored air choices and follow-up windows take priority. If no distinct air
lane exists, share admitted melee clips with an airborne host hold. If no
follow-up window exists, open input after the actual last strike. A missing
trail uses exactly the admitted strike window, never an always-on trail.

This ordering/follow-up policy is our host adaptation; it is not a recovered
original KH2 Riku combo script. Actual source clip selection still needs the
fresh game test. No hit timing, damage values, scripts, special commands,
magic, extra abilities or donor control class are invented or enabled.

Admitted passive Riku visuals no longer require a melee adapter. If real
contacts cannot qualify, retain native KH1 attacks and print the reason.
Missing visual slots, native KH1 spells and normal Glide/Superglide still
use the existing KH1 fallback. No Sora combo-table substitution is used.

FIRST TEST
1. Fresh game process. Equip Style: Single C and check idle/run/jump.
2. Test a basic ground combo and aerial combo. To isolate the base sequence,
   temporarily unequip attack abilities such as Slapshot/Blitz if necessary;
   their existing native priority is deliberately retained.
3. Expected startup progression:
   SINGLE C CLIP METADATA ... (bounded actual motion/contact inventory)
   SINGLE C MELEE ADAPTER ... bindings=[host<-source:...] ...
   SINGLE C DONOR LOADED ... attack_adapter=true ...
   SINGLE C DATA ... playable final-battle Riku=true attack_adapter=true
   Existing usable PTYA rows instead use the original row adapter.
4. If attacks remain native, a pose is wrong or it crashes, return the full
   fresh kh1-dual-wield.log including startup and clip/adapter diagnostics.
   The ability entry alone does not establish successful donor admission.

PRESERVED
The other six styles, ability IDs/exclusivity, native ability policy, core
controllers and native FX remain unchanged from v31. Preservation checks also
cover the complete Glide attachment/color path, Dual A's working Superglide
finisher, Dual B's Quick Run/Guard/Fire/magic and Dual C's KH2 Sora Guard.
Roxas data loading, rig reconstruction and combo adaptation remain unchanged.
Single C's primary trail reads its own admitted source strike windows.

Seven exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final), Single A 124
(base KH2 Sora), Single B 123 (Wisdom), Anti 122, Dual C 121 (dual Roxas),
Single C 120 (endgame Riku). Only the Dual styles duplicate the equipped weapon.
Single C retains Sora's appearance and one equipped KH1 weapon. No gauge,
second weapon choice, fixed donor weapon, stat bonus or extra ability is added.

INI defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
To remove custom entries: set remove_dual_wield on; launch/load/save with
v32; close; disable the mod and Build again. Only our seven custom entries
are removed. DLL/INI changes require a full restart.

VALIDATION AND LIMITS
498 tests pass across 31 suites (156 style tests), including zero-PTYA Riku
routing, three-step/input termination, Combo Plus, contact preservation,
hand-only collision admission and rejection of unsafe/gated/magic contacts.
Fixtures reproduce the observed 209/12-bone, zero-row case; these are synthetic
data tests, not a run of the user's installed Riku animation assets.
Windows x64 release, PE interface, 141 source/preservation checks, 11 native
anchors and seven protected-model metadata checks pass. ZIP CRC, independent
extraction and saved-copy hashes are verified.

No live v32 game/GPU test or actual installed Riku clip execution was run
here. Source patch, pinned upstream, credits/licences and validation receipts
are included. No game executable, recording, extracted asset or disassembly
ships. Detailed behavior/confidence: docs/combat-model.md Stage 371 in patch.
Format references:
  https://openkh.dev/kh2/file/anb/mset.html
  https://openkh.dev/kh2/file/type/00battle.html
