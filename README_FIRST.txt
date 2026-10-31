KH1FM FIVE STYLES -- PROTOTYPE v20 (s359)

INSTALL -- REPLACES BROKEN v19
1. Fully close KH1FM. Disable v19, v18 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod. Enable ONLY v20, then Build and Run.
   Panacea is required. F1 cannot reload a native DLL.
3. Confirm s359 and PROTOTYPE v20 in kh1-dual-wield.log next to the game EXE.

The five IDs remain Dual A 126, Dual B 125, Single A 124, Single B 123,
Anti 122. All are 0 AP and exclusive. Only Dual styles duplicate the
currently equipped weapon. There is no second weapon menu or Drive state.
Keep old offhand/moveset Lua, duplicate model mods and the full KH2 Combat
overhaul disabled. Normal Sora and your installed KH2FM are required.
This mod goes in OpenKH, not the Lua scripts folder. No game assets supplied.

CORRECTIONS
v19 wrongly rejected actor +160 bit 100 hex. KH1 actually sets this bit
when it consumes a motion change; it is a first-frame notification, not a
special animation-bank selector. This could discard an accepted attack
and clear an observed cast before its KH2 pose/effect was admitted.

v20 permits that normal first frame through its shared field/cast scope
and removes the passive pose's one-frame blanking check too. Real actor/
body binding, event/script, movement, native ability priority, cast header/
clock and ownership lifetime guards remain. The native flag is never
patched. Accepted landing/interrupt attacks and the bounded cast recovery
bridge remain, with the incorrect notification gate removed.

v19 also added an early B Roll selector before actual native commitment.
That selector and its generic control override are removed. Both B styles
again start Quick Run only from the committed native Roll-start hook,
through the existing Single B host-action path. This restores the entry
route reported working for Single B before v19. Release, loaded finite
timing and the end clip remain. Native Dodge Roll eligibility still gates
the action; no Quick Run/growth ability is added to the save.

Dual B uses the same path and Wisdom 203/204 body data with both Final idle
blade tracks. Its native Roll symptom predates v19; the exact earlier
cause is not established without a fresh native log. The new build records
actual hook installation and action admission/start/fallback details so
that the next result can distinguish those paths. Do not treat the offline
checks as a verified in-game Dual B fix.

Retained: Anti's base KH2 Sora Glide/Superglide body pose and weaponless
Dodge Roll instead of intrinsic Anti Glide; finite combo Side Spin, aura,
and no magic/items/summons. Single B keeps base KH2 Sora's guard-press
animation with native blocking. A finisher Superglide, .75 Wisdom Run,
existing spell draw filtering, all native stats/party and style exclusivity
remain. No gauge, outfit, stat bonus, partner change or extra ability.

FIRST TEST
1. Test an ordinary ground and air attack, including immediately after
   landing. Native attack abilities still retain their native combo lane.
2. In Dual B and Single B cast Fire, Blizzard, Thunder and Cure, including
   repeated casts. Check KH2 poses/effects and normal MP/damage/healing.
3. Test Single B Quick Run separately: with native Dodge Roll equipped,
   move and tap Square, then hold and release it. Check completion and
   return to normal movement. Repeat after a style/map/menu change.
4. Repeat that test in Dual B. If it still rolls, or either Quick Run
   glitches, return the FULL fresh kh1-dual-wield.log from this run. It is
   next to KINGDOM HEARTS FINAL MIX.exe, not in the scripts folder.
   Include startup; do not restart the game before copying that log.

Useful log markers:
  STYLE COMMITTED ROLL HOOK: installed=true
  DUAL B ACTION DATA: quick_run_ready
  STYLE NATIVE ROLL ENTRY: style=Ranged or SingleB
  DUAL B QUICK RUN REQUEST / DUAL B QUICK RUN START
  SINGLE B QUICK RUN REQUEST / SINGLE B QUICK RUN START
  STYLE QUICK RUN ADMISSION FAILED / COMMITTED DODGE START FAILED
  STYLE KH2 CAST: ... motion_changed=true
  STYLE ACCEPTED ATTACK HANDOFF
A first-frame motion_changed=true is legitimate and must not discard a cast.
An old log does not establish which current DLL or action route ran.

SPELL COVERAGE / SETTINGS
KH2 effect packages cover Fire, Blizzard, Thunder and Cure at all three
native levels in Dual B/Single B. Gravity, Stop and Aero retain native FX.
Single A uses KH2 cast poses with native KH1 effects. KH1 spell logic,
damage, healing, costs and levels remain authoritative.

kh1-dual-wield.ini is next to the EXE and is preserved. Missing keys use:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Single B Run is fixed at .75. offhand_only_test isolates left imported
contacts in Dual styles; single/Anti contacts, spells and party damage
are unaffected. For uninstall, set remove_dual_wield on, launch/load/save
with v20, close, disable the mod and Build again. Only the five custom
entries are removed. Native DLL/INI changes require a full game restart.

VALIDATION / LIMITS
435 portable tests pass across 27 suites, including 134 style tests. New
fixtures cover native first-frame notifications through attack/cast/effect
admission and both B Quick Runs held/released through completion. Windows
x64 release, expected PE imports/exports, 43 source-scope checks and seven
additional native motion-update/notification anchors pass. Earlier native
action, renderer and spell-filter checks are retained. The source audit
explicitly rejects the discarded flag gate and early B Roll selector.

These are offline checks. No fresh game/GPU execution was performed. The
user's video/report identifies the live v19 regression; current animation,
spell, dodge and interruption behavior must be tested in a fresh process.
Source patch, provenance, licences and validation receipts are included;
no recording, game assets, executable or disassembly is distributed.
