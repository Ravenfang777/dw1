KH1FM FIVE STYLES -- PROTOTYPE v19 (s358)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v18 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v19, then Build and Run.
   Panacea is required. F1 cannot reload a native DLL.
3. Equip one style. IDs/states remain: Dual A 126, Dual B 125,
   Single A 124, Single B 123 and Anti 122. All are 0 AP and exclusive.

Keep older integrated/offhand Lua, Synch/moveset routers, duplicate Sora
model mods and the full KH2 Combat overhaul disabled. Requires normal
Sora and your installed KH2FM in the same installation. The DLL belongs
to this OpenKH mod, not the scripts folder. No game assets are supplied.

WHAT CHANGED
Cast recovery: match the original native cast header rather than a
fragile slot range. Mask native motion-control bits before table lookup.
Keep the last KH2 pose during the brief request/header publication gap,
only while that same cast header remains visible (maximum 8 callbacks).
New header, attack, scene, binding or timeout ends it. No replayed cast,
spell events or additional FX. This addresses the KH1 Fire recovery flash.

Landing/interrupted attacks: an accepted native Attack now authorizes
style combo entry even if the preceding landing/cast pose is still up.
Retire that previous native action and start the imported controller;
retain field/body, scene, pause/time, damage and timeout guards. Landing
poses remain visible during the brief native input lock. Native attack
abilities still retain their original combo lane, as previously requested.
This change does not replace an intentionally native ability-selected row.

Dual B: intercept the native ground Roll selection before Roll starts,
using the same input/ability/direction predicate. Queue its existing
Wisdom Quick Run through the working Single B host path. The committed
Roll hook remains fallback; no offhand-readiness requirement is added.
Stationary Guard keeps the spin and Final basic combos remain.

Anti: remove intrinsic Square Anti Glide. Ground Square starts native
Dodge Roll movement with base KH2 Sora's roll pose and no visible weapon.
Both Glide and Superglide use base KH2 Sora's normal glide body pose;
movement and native glide ability gates stay KH1's. Only body tracks are
copied into Anti's zero-weapon rig. Anti body combat, finite combo Side
Spin, persistent darkness and no-magic/no-items/no-summons policy remain.

Single B: native Guard uses base KH2 Sora's guard-press animation and
right-weapon track. Native blocking/eligibility remains. It does not use
the guard-hit/repel reaction. No Guard ability or second blade is added.
Wisdom Quick Run, shots and the .75-rate running pose remain.

All five styles remain exclusive. Only Dual styles duplicate the current
equipped weapon. No second weapon menu, gauge, outfit, stat bonus, party
change or extra ability. Dual A/Single A real-finisher Superglide stays.

FIRST TEST -- FRESH PROCESS
1. Confirm log s358 / PROTOTYPE v19 and STYLE TABLE READY.
2. In Dual B, Single A and Single B: cast Fire on the ground and in the
   air. Check its final recovery, repeated casts and Attack interrupts.
3. For every style: jump/land then Attack immediately; interrupt another
   legal animation with Attack. Repeat after entering battle/changing maps.
   To isolate imported basic combos, use a lane without native attack
   abilities; an ability-selected native lane intentionally stays KH1.
4. Dual B: equip native Dodge Roll, hold a direction, press Square. Check
   Quick Run and STYLE QUICK RUN SELECTOR / DUAL B QUICK RUN START.
5. Anti: Square on the ground must roll, not perform Anti Glide. Test both
   glides, hidden weapon, body hits, aura and blocked Magic/Items. Unequip
   and change maps/styles to check retirement.
6. Single B: with native Guard equipped, stop moving and press Square.
   Check the KH2 guard-press pose and a real block; then Quick Run/shot.

LOG -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
kh1-dual-wield.log should show s358 and PROTOTYPE v19.
Useful markers:
  STYLE ACCEPTED ATTACK HANDOFF
  STYLE QUICK RUN SELECTOR / DUAL B QUICK RUN START
  ANTI LOCOMOTION DATA / ANTI DODGE ROLL START
  DUAL WIELD VISUAL ACTIVE: action=guard source=base Sora
If a fallback persists, return the fresh full log, including startup and
that action. An old log cannot establish which DLL or selector ran.

SPELL COVERAGE / EXISTING SETTINGS
KH2 effect packages cover Fire, Blizzard, Thunder and Cure, all three
native levels, in Dual B and Single B. Gravity, Stop and Aero retain
native effects. Single A uses KH2 cast poses with native KH1 effects.
Native KH1 damage, healing, costs and levels remain authoritative.
The per-cast target-spark filter and Anti darkness are retained from v18.

kh1-dual-wield.ini is next to the EXE and preserved. Missing keys use:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Single B Run is fixed at .75; idle_speed configures shared imported idle.
The offhand-only option isolates left imported contacts in Dual styles;
single/Anti contacts, native spells and party damage are unaffected.
For uninstall: set remove_dual_wield on, launch/load/save with v19, close,
disable the mod and Build again. Only the five custom entries are removed.
Restart KH1 after native DLL or INI edits.

VALIDATION / LIMITS
432 portable tests passed across 27 suites, including 131 style tests.
Windows x64 release build, expected PE imports/exports, 45 source-scope
checks and six additional native setter/control/roll anchor checks pass.
Earlier native action, renderer and spell-filter checks are retained.
The Linux test cache initially failed to link; the successful portable
run used a fresh cache with one codegen unit. No gameplay workaround is
based on that build-environment failure.

No fresh game/GPU execution was performed. Fire recovery, landing and
interrupt continuity, live Dual B Quick Run, Anti glide/roll placement,
and Single B Guard must be tested in-game. Native spell gameplay and
original filtering paths are retained; full target visual suppression
still needs live verification. Source patch, provenance, licences and
validation receipts are included; no game assets, executables or dumps.
