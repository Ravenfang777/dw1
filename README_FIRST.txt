KH1FM NINE STYLES -- PROTOTYPE v48 (s387)

SINGLE D JUMP CORRECTION
Restores the jump takeoff from before v47 (main1160 source3). Only the rising
and falling portion uses the previous falling clip (source6), playing once
then holding its end until landing/interruption. Takeoff does not start or
consume the airborne clock. Landing remains source7. v47's leg/hip correction,
checked secondary rest and skin validation remain.

INSTALL
1. Fully close KH1FM. Disable v47 and all older Dual Wield prototypes.
2. Import THIS ZIP through OpenKH, enable only v48, then Build and Run.
   Requires Panacea and installed KH2FM resources. F1 cannot reload a DLL.
   Keep full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
   Sora model mods disabled. Existing INI/save settings remain in use.
3. Confirm s387 / PROTOTYPE v48 in kh1-dual-wield.log beside the game EXE.

TEST
Equip Style: Single D. Check standing/moving jumps: takeoff should animate
again, followed by the airborne falling pose, held until landing. Repeat
jumps, walk off a ledge and change map. Check that v47's improved stance stays.
No new source capture is needed. Return the fresh log if a transition fails.
Expected MOVEMENT ACTIVE: takeoff source_slot=3; rise/fall source_slot=6.
These diagnostics log once per action kind, not every frame of a held pose.

SCOPE
Idle0, walk1, run2, takeoff3, rise/fall6 once then held, landing7.
Takeoff retains the original native phase and source timing. The separate
pause-aware airborne clock starts on rise/fall, survives their transition,
and holds its end. Repeated drawing/pauses do not advance it. Native landing,
interruption, style/actor/binding/map handoffs still reset the interval.
Native jump height, movement controls, collision and action admission remain.
Single D combat/magic/items/Guard/Roll/damage/ledges/glides still use the native
KH1 actions during this movement-mapping test. One equipped weapon remains.
Hair/cloth/keychain keep checked rest during mapped Single D movement.
All other styles, contacts/effects, combos, Quick Run, Superglide/finishers
and confirmed2x Aerial Dodge routes remain. Nine exclusive0-AP abilities;
no extra abilities, gauge, stats, outfit, partner or weapon selection.
Existing INI options remain. Restart the game after DLL/INI changes.

VALIDATION
591 tests/31 suites pass, including173 existing style tests,16 map tests and
9 Dark Riku policy/clock tests. Windows x64 release passes with the same
4 exports and8 imports.21 scope checks protect287 other tracked files.
The complete map and source solver are byte-identical to v47; its2139-pose
mapping proof is retained as labelled historical evidence, not rerun here.
New coverage verifies restored takeoff sampling, no airborne-clock progress
before rise, then shared rise/fall playback and held endpoints.
The cumulative48-commit source patch, licences and receipts are included.
ZIP CRC/extraction and every file hash checked before delivery.
Actual v48 in-game transition/skin validation still needs your fresh test.
No original game executables/assets or raw pose streams ship.

Removal: set remove_dual_wield on, launch/load/save with v48, close the game,
disable the mod and Build again.
