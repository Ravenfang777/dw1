KH1FM FIVE STYLES -- PROTOTYPE v23 (s362)

INSTALL
1. Fully close KH1FM. Disable v22 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH. Enable ONLY v23, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s362 / PROTOTYPE v23 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not a script. Keep the full KH2 Combat
overhaul, old offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied.

WHAT THE CURRENT LOG SHOWED
Dual B: v22 captured eight Square attempts as Guard and never reached
its native Roll hook. Single B Quick Run still worked five times. v23
removes Dual action selection from that early hook. KH1 now finishes its
own movement callback and Guard-versus-Roll decision. The imported Guard
starts only from the actual selected Guard branch. Moving Square takes
the native Roll route and the existing Wisdom Quick Run replacement.
The early selector retains only Anti's existing unarmed override.

The new Guard bridge admits one imported action or resumes native Guard
with its original arguments. An admitted replacement creates no native
Guard context, motion, voice or blocking flag. Single B's confirmed KH2
Guard still observes its actual native Guard row. The older Square
fallback cannot reinterpret a committed Guard/Quick Run/finisher press.
Dual B Guard/Quick Run retain native Guard/Dodge Roll ability gates;
no ability is granted by the style.

Fire: the new log records the exact clock failure. Recovery's header
appears while the old startup clock is still present, then KH1 resets
that clock to zero. v22 treated this as a reversal and dropped the KH2
pose. v23 holds the last donor sample until the recovery request leaves
the native queue, then starts its recovery clock. Both phases keep one
cast/effect identity. Actual repeat casts still get a fresh identity.
The handoff is bounded and retains header, scene, binding and time guards.

KH2 FIRE COMBO STAGES
The current style overlay uses the first KH2 ground/air Fire cast clip.
It does not yet advance through KH2's spell-combo stages or finisher.
That needs separate combo tracking and donor selection. This update
repairs the recorded recovery-clock failure; it does not add new casts,
spell finishers or finisher damage. KH1 still owns costs, damage, levels,
acceptance and repeated-cast timing.

FIRST TEST -- FRESH GAME PROCESS
1. Dual B: equip native Guard and Dodge Roll. Stop and tap Square for
   Guard spin. Hold a direction and tap Square for Wisdom Quick Run.
   Check hold/release, completion, movement and a second independent run.
2. Single B: check its confirmed KH2 Guard and existing Quick Run.
3. Both B styles: cast Fire separately and repeatedly, on ground and in
   air. Check the recovery and return to idle/fall for any KH1 flash.
4. Recheck basic combos, native attack abilities and map/style changes.

If something remains wrong, send the FULL current kh1-dual-wield.log
including startup from beside KINGDOM HEARTS FINAL MIX.exe before the
next restart. New/updated markers:
  STYLE COMMITTED GUARD BRANCH: installed=true
  STYLE NATIVE ROLL ENTRY / STYLE NATIVE DODGE REPLACED
  DUAL B QUICK RUN REQUEST / DUAL B QUICK RUN START
  STYLE FIRE RECOVERY: native_clock=... queued=...
  STYLE CAST REQUEST / STYLE CAST HANDOFF / STYLE CAST END

RETAINED
Five exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed).
Only Dual styles duplicate the currently equipped weapon. No second weapon
selection, Drive state/gauge, outfit, stat bonus, extra ability or partner
removal. Native attack abilities keep their native combo lane. A finisher
Superglide, Single B .75 Run and Anti's weaponless base movement, body
combat, darkness aura and magic/item/summon restrictions remain.

Both B styles retain KH2 Fire/Blizzard/Thunder/Cure effects at native
levels and existing native visual filtering. Gravity/Stop/Aero retain
native effects. Single A retains KH2 cast poses with native KH1 effects.
Native KH1 damage, healing, levels and costs remain authoritative.

Your existing kh1-dual-wield.ini beside the EXE is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Single B Run uses .75 independently. Offhand-only testing is for Dual
styles, not spells, companions or Single/Anti. To remove custom entries,
set remove_dual_wield on, launch/load/save with v23, close the game,
disable the mod and Build again. Only the five custom entries are removed.
DLL/INI changes require a full restart.

VALIDATION AND LIVE LIMIT
446 tests pass across 27 suites (144 style tests). The new Guard bridge
executes both branches in a Win64 ABI harness using the native frame
layout; restored arguments, callback/fallback counts and returns pass.
The new Fire replay covers the recorded old-clock -> zero sequence,
multiple model passes, both families, buffer reuse and retirement guards.
Windows x64 release, PE interface, 14 native anchors and 70 source-scope
checks pass. ZIP CRC, extraction and saved-copy hashes are verified.

No fresh v23 game/GPU execution was performed. Native action selection,
Fire presentation and synchronization still need the live check above.
Source patch, pinned upstream, credits, licences and validation receipts
are included. No game executable, recording, extracted asset or
disassembly is distributed.
