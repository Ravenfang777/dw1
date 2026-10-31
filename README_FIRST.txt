KH1FM FIVE STYLES -- PROTOTYPE v21 (s360)

INSTALL
1. Fully close KH1FM. Disable v20 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod. Enable ONLY v21; Build and Run.
   Panacea is required. F1 cannot reload a native DLL.
3. Check s360 / PROTOTYPE v21 in kh1-dual-wield.log next to the game EXE.

Five exclusive 0-AP IDs remain: Dual A 126, Dual B 125, Single A 124,
Single B 123, Anti 122. Only Dual styles duplicate the equipped weapon.
Normal Sora and your installed KH2FM are required; no game assets supplied.
Keep old offhand/moveset Lua, duplicate Sora model mods and the full KH2
Combat overhaul disabled. This mod goes in OpenKH, not the scripts folder.

WHAT CHANGED
Single B Guard after Fire: the old code confused native Guard ROW 0x3D
with MOTION 0x3D, which is also Fire recovery. That raw map is removed.
An observer now records the actual native Guard row start and the motion
its original code requests. Only that exact, current witness can draw
KH2 Sora's guard press. Native blocking, context, effects and eligibility
remain. The same correction applies to Single A. No Guard ability is added.

Fire endings: ground Fire is natively 0x36 then 0x3D; air Fire is 0x83
then 0x8A. Both phases now share one continuous KH2 donor cast timeline,
using the installed native durations/FPS. They keep one cast/effect ID,
so the follow-up does not restart a spell or its effects. Other motions
and spells are not linked. Actor, scene, header, pointer, repeat and
lifetime guards remain. Native costs, damage, targeting and recovery stay.

Dual B Quick Run: a standalone Wisdom dodge profile now supplies the
actual 203/204 body animation, controller clips and movement parameters.
It no longer relies on Final combo/Guard adapter admission. Both equipped
Keyblades remain represented by Final idle blade tracks (or standard bind
pose fallback if an optional idle track is absent). No attack/shot/cast
events or hitboxes run during this dodge, and no growth ability is granted.
It still enters only after native Dodge Roll is committed. Single B's
working entry path is retained. This is a new live test of that independent
Wisdom route; offline checks do not prove the earlier Dual B admission cause.

FIRST TEST
1. Single B: with native Guard equipped, stop moving and press Square.
   Check KH2 guard press and actual blocking. It must not appear after Fire.
2. Single B and Dual B: Fire on the ground and in the air, including
   repeated casts. Check smooth cast endings and return to idle/fall.
3. Dual B: with native Dodge Roll equipped, hold a direction and tap
   Square, then hold/release it. Check Wisdom Quick Run, both blades,
   completion, normal movement and a second independent dodge.
4. Repeat after menu/style/map changes. Recheck basic combos and Single B
   Quick Run. Native attack abilities still retain their native combo lane.

If a problem remains, include the FULL fresh kh1-dual-wield.log, including
startup, from beside KINGDOM HEARTS FINAL MIX.exe before another restart.
Useful markers:
  STYLE GUARD ROW HOOK: installed=true
  STYLE NATIVE GUARD WITNESS: row=0x3D resolved_motion=...
  STYLE FIRE SEQUENCE: 0x36->0x3D or 0x83->0x8A
  DUAL B WISDOM DODGE DATA: adapter=true growth=true
  STYLE COMMITTED ROLL HOOK / STYLE NATIVE ROLL ENTRY
  DUAL B QUICK RUN REQUEST / DUAL B QUICK RUN START
  STYLE QUICK RUN ADMISSION FAILED / COMMITTED DODGE START FAILED

RETAINED
A finisher Superglide; Anti weaponless base KH2 Sora glides/Dodge Roll,
body combat, aura and no magic/items/summons; Single B .75 Run; all five
styles/exclusivity; native stats and party. No Drive state, gauge, outfit,
stat bonus, extra ability or second weapon selection.

KH2 effect packages cover Fire, Blizzard, Thunder and Cure (all native
levels) in both B styles. Gravity/Stop/Aero retain native effects. Single A
uses KH2 cast poses with native KH1 effects. Native spell logic, damage,
healing, costs and levels remain authoritative. Existing effect filtering
is retained; this update does not claim new target-effect suppression.

kh1-dual-wield.ini next to the EXE is preserved. Missing keys use:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Single B Run is fixed at .75. Offhand-only testing affects left imported
contacts in Dual styles, not singles/Anti, spells or party damage.
For uninstall: remove_dual_wield on, launch/load/save with v21, close,
disable mod and Build again. Only the five custom entries are removed.
Native DLL/INI edits require a full game restart.

VALIDATION / LIMITS
440 portable tests pass across 27 suites (139 style tests). Windows x64
release, PE interface, 55 source-scope checks and 12 new native row/Fire
anchors pass. New tests cover Guard versus Fire identity, both phases,
rates, header publication lag, interruption/repeat rejection and Wisdom
movement without Final combo rows, events, contacts or saved growth.

No fresh game/GPU execution was performed. Fire release/FX synchronization,
actual Guard and Dual B dodge behavior need the fresh-process test above.
Source patch, provenance, licences and validation receipts are included.
No game assets, executable, recording or disassembly is distributed.
