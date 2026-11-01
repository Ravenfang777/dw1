KH1FM NINE STYLES -- PROTOTYPE v49 (s388)

SINGLE D: SINGLE C JUMP AND FIRST DARK RIKU COMBOS
The jump now borrows Single C's actual KH2 playable Riku jump, paired native
takeoff/rise timing and matching source-layout retarget. It has a separate
calibration, so it does not replace the Dark Riku movement/body map.

Initial basic combo animation map:
Ground:18 ->19 ->20. Air:18 ->19 ->21. The native first-ground variants C8/CA
both use18. These are candidate sword swings identified from solved poses;
their original boss script names/order and contact events are not verified.
KH1 still supplies combo selection/repeats, ability priority, hit timing,
damage, movement, swing/impact sounds and contact feedback. This is an initial
animation adapter, not a donor attack-event/contact importer. Hit/HP loss does
not establish authored Dark Riku hit timing or exact blade contact alignment.

INSTALL
1. Fully close KH1FM; disable v48 and every older Dual Wield prototype.
2. Import THIS ZIP in OpenKH, enable only v49, then Build and Run.
   Requires Panacea and installed KH2FM resources. F1 cannot reload the DLL.
   Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
   Sora model mods disabled. Existing INI/save settings remain.
3. Confirm s388 / PROTOTYPE v49 in kh1-dual-wield.log beside the game EXE.

TEST
Equip Style: Single D on normal Sora. Check a standing/moving jump first,
then basic ground and aerial combos on one enemy. Look for all three swings,
weapon grip, effects/contact timing and normal return to idle/fall. Repeat
jumps and attacks, interrupt with magic/Guard/damage, change map and re-equip.
Native attack-replacement abilities still take priority; temporarily unequip
those only if you want to isolate the basic mapped motions for this test.
No new source capture is needed; the original Dark Riku bank is already here.
Return the fresh log and describe which step, animation or hit looked wrong.

EXPECTED LOG
SINGLE D SOLVER READY and MAP READY for original Dark Riku movement/combos.
SINGLE D SINGLE C JUMP READY when the borrowed jump is first sampled.
SINGLE D BASIC COMBO ACTIVE: ground first/second/finisher and air equivalents,
showing current native slot, source slot/frame and native normalized phase.
Logs occur once per action kind, not once per hit. MAPPING WAIT can be normal
at script/control/landing handoffs. MAP UNAVAILABLE, MAPPING POSE REJECTED or
FINAL POSE REJECTED should be returned with the complete log.

PRESERVED
D idle0/walk1/run2, held fall6 and landing7; corrected hip/leg frame, own bone
lengths/scales, checked secondary rest and final skin-basis guard. Source
travel is removed. Hair/cloth/keychain remain more rigid in mapped D poses.
The borrowed jump avoids feeding raw Riku joints into base-Sora secondary or
effect consumers. Other D actions (magic, items, Guard, Roll, damage, ledges
and glides) remain native pending later mapping. One equipped weapon remains.
All other styles, actual combo/contact/FX controllers, Quick Run, Superglide
and finishers, including Dual A, remain. Confirmed regular Glide replacements
retain2x Aerial Dodge travel at original timing. Nine exclusive0-AP entries;
no extra blade for Singles, ability grant, gauge, stats, outfit or party change.
Restart after DLL/INI changes. Removal: set remove_dual_wield on, launch/load/
save with v49, close the game, disable the mod and Build again.

VALIDATION
594 tests/31 suites pass:174 style,16 body map and11 D policy/clock tests.
Windows x64 release passes with the same4 exports/8 imports.25 source checks
protect285 other tracked files. No new native hooks, addresses or dependencies.
All2139 source poses/31 clips solve again;232 sampled poses cover18..21.
The source solver and Dark Riku body map are unchanged from their validated
versions. Historical v47 target-matrix proof is labelled and not rerun here.
Fresh nonincremental tests without debug symbols avoid a corrupt cached test
executable; no assertion was weakened. ZIP CRC/extraction/file hashes and
49-commit exact source-tree reconstruction are checked before delivery.
Actual v49 in-game jump/attack/contact alignment still needs your test.
No original game assets/executables or raw pose streams ship.
