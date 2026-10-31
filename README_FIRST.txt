KH1FM NINE STYLES -- PROTOTYPE v44 (s383)

INSTALL
1. Fully close KH1FM. Disable v43 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v44, then Build and Run.
   Panacea and installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s383 / PROTOTYPE v44 in kh1-dual-wield.log beside the game EXE.
Use normal Sora. Keep the full KH2 Combat overhaul, older offhand/moveset Lua
and duplicate Sora model mods disabled. Existing INI/save settings are retained.

DARK RIKU SOLVER
This version implements the authored pose solver needed for Single D's main
bank, xa_ex_1160. It handles constant channels, native fixed-tick curves,
helper transforms, look-at/orientation constraints and one-/two-link limbs.
Those stages were missing from the old FK-only reader. The legacy reader is
preserved for existing styles; the new solver is an independent data path.

The Rust output was compared offline against KH1's original evaluator for
2139 poses across all 31 clips, covering every integer animation frame plus
fractional, endpoint and quantization cases. All 205 active bone matrices,
12 helper matrices and the separate root channel were checked in each pose.
Maximum observed joint-position difference: 0.0018071 game units.
This is authored animation validation, not a live game/GPU or floor-IK test.
A separate half-speed skeleton GIF shows the old reader and corrected solver.

CURRENT IN-GAME STATUS
Single D STILL USES NATIVE KH1 MOVES and one weapon. The source pose solver is
implemented; mapping those poses onto Sora and assigning actions/contacts are
next. No boss AI, raw animation pointers, attacks or extra abilities are added.

At startup a background worker reads your original main bank and checks all
1829 integer/end poses. Look for:
  SINGLE D SOLVER READY: source=xa_ex_1160 bones=247 motions=31 checked_poses=1829
The line also states that gameplay retarget/action routing is pending.
No battle, attacks or Single D equip are needed for this check.
If it reports SINGLE D SOLVER UNAVAILABLE, return the complete fresh log.
The original bank was already received; no additional source capture is needed.
Existing diagnostic CSV/source capture remains available. Its generated source
ZIP is NOT an OpenKH mod: do not install that capture ZIP.

PRESERVED FROM THE USER-CONFIRMED v43
Regular Glide remains the 2x-distance, normal-speed Aerial Dodge for Single A,
Single C, Dual C and Dual D. Single styles keep one weapon; Dual styles copy
what is equipped. All current Superglide routes remain, including the actual
Single A/Dual A finisher. Quick Run, Guard, magic, attacks, native attack-ability
priority and every other style's input/visual/contact behavior are preserved.
Menu order remains Single A/B/C/D, Dual A/B/C/D, Anti; all 9 exclusive, 0 AP.
No gauge, outfit, party, stat or other ability changes.

INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full restart.
To remove entries: set remove_dual_wield on; launch/load/save with v44;
close; disable the mod and Build again.

VALIDATION AND LIMITS
542 tests across 31 suites, 173 style tests and 11 new solver tests pass.
Windows x64 release, 4 exports/8 imports, 55 source-scope checks, 15 native anchors
and 7 model checks pass. No new game hook/address or Cargo/runtime dependency.
The DLL does not require Python, Unicorn, Ghidra or an external ZIP program.
Native comparison checked 7426608 float components. Root channel matched exactly;
maximum basis component difference 0.00003803, helper difference 0.00006676.
Nearly straight limbs produce the largest float-rounding differences.
See README_SOLVER.txt and validation/native_solver_validation.json for method,
limits and an optional reproducible reference harness.
Installer ZIP CRC, extraction and every entry hash are verified.
Source patch (44 derivative commits), credits/licences and validation included.
Rules/confidence: docs/combat-model.md Stage 383.
No original game executables, model/animation files, decompiler output or pose
streams ship in this installer. No actual v44 game/GPU/Sora-retarget test here.
