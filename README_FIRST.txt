KH1FM SEVEN STYLES -- PROTOTYPE v33 (s372)

INSTALL
1. Fully close KH1FM. Disable v32 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v33, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s372 / PROTOTYPE v33 in kh1-dual-wield.log beside the game EXE.

Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
Sora model mods disabled. Use normal Sora. Existing INI/save style entries
are preserved. This is an OpenKH native DLL mod; no game assets ship.

SINGLE C MAPPING
Ground combo: keep the working Riku 151 -> 152 -> 182 routing.
Aerial combo: use the full Riku 181 sequence on each aerial combo step.
  All thirteen original weapon-contact windows and the real pose/root remain.
  Each continuation requires an Attack press near the end of the sequence;
  it never automatically starts all three combo steps. Air Combo Plus remains.
Air Square: tap Square from a normal jump/fall to play Riku 193 once.
  No attack combo or held repeat. Holding Square cannot automatically start
  native Glide afterward; release the button to rearm. Native field, can-act,
  menu, shortcut and deep-water gates still apply. It does not cancel an
  already owned attack or native scripted action.
Ground dodge: committed native Dodge Roll is replaced by Wisdom Quick Run
  and its end animation. Native Dodge Roll selection/ability rules remain;
  no Quick Run ability, Wisdom shot or second weapon is granted.
Cure, Gravity, Stop, Aero: RIKU item-use animation 9, on ground and in air.
Fire, Blizzard, Thunder: KH2 BASE SORA casting animations.
Guard, ledge hang/climb, normal Glide/Superglide, missing heavy reactions:
  KH2 BASE SORA animations, on their existing native KH1 actions.
Other admitted Riku movement, ordinary item/damage and idle poses remain.

SPELL EFFECTS
Fire, Blizzard, Thunder and Cure use KH2 BASE SORA spell effects at the
matching native spell level. Existing ownership-scoped native-visual filtering
prevents the replaced KH1 caster/target visuals from doubling the effects.
The rendered Sora pose supplies correct base-Sora effect anchors even when
Riku supplies the item-cast animation. Cure's visual release is normalized to
that item pose; spell execution, damage/healing and MP remain native KH1.

Base KH2 Sora has no direct Gravity, Stop or Aero spell counterpart. Their
Riku item-cast poses are changed; their existing KH1 spell effects remain.
No Magnet/Reflect substitute or different spell behavior is silently added.
The existing dual_b_spell_fx INI switch also controls these matching C effects.

193's visual action name is still unidentified. Its actual physical body
contact is admitted only if the real collision shape and STR normal/piercing
ATKP record qualify. Otherwise its valid animation can play without a contact.
No special script, projectile, extra spell or synthetic damage is created.
This body-contact exception applies only to the explicit 193 action; the
ordinary sword combo still rejects unrelated body/kick contacts.

FIRST TEST
1. Equip Style: Single C. Check movement and ground combo first.
2. Jump and tap Attack: watch the complete 181 aerial sequence. Test another
   Attack near its end to continue. Native attack abilities retain priority;
   temporarily unequip relevant modifiers if isolating the base sequence.
3. From a fresh normal jump/fall, tap Square once to test 193. Hold/release it
   separately to check that it ends and does not restart or enter Glide.
4. Dodge with the native Dodge Roll ability/selection, then release Square:
   check actual Quick Run movement and its finite end.
5. Test all seven spells on ground and in air, then Guard and a ledge.
   Single C's Glide/Superglide should show base Sora while retaining native
   movement/ability logic. Dual A's working Superglide finisher is unchanged.
6. If anything fails, send the full fresh kh1-dual-wield.log including startup.
   Useful lines: SINGLE C AIR COMBO, SINGLE C AIR SQUARE DATA/REQUEST/START,
   SINGLE C MELEE ADAPTER, SINGLE C QUICK RUN REQUEST and STYLE KH2 CAST.

PRESERVED
Other styles, seven exclusive 0-AP IDs, weapon/equipment, native attack ability
priority and the core controllers remain. Complete offhand Glide/color draw,
Dual A's actual Superglide finisher, Dual B actions/FX, Wisdom shots and Roxas
loading/combos/Guard are protected by preservation checks and regressions.

IDs: Dual A 126 (Valor), Dual B 125 (Final), Single A 124 (base Sora),
Single B 123 (Wisdom), Anti 122, Dual C 121 (dual Roxas), Single C 120 (Riku).
Only Dual A/B/C duplicate the equipped weapon. Single C keeps Sora's appearance
and one equipped KH1 weapon. No gauge, donor costume, fixed weapon, second
weapon choice, stat bonus or extra equipped ability is added.

INI defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Uninstall custom entries: set remove_dual_wield on; launch/load/save with v33;
close; disable the mod and Build again. Only our seven entries are removed.
DLL/INI changes require a full restart.

VALIDATION AND LIMITS
505 tests pass across 31 suites (160 style tests). Windows x64 release, PE
interface, 98 source/preservation checks, 11 native anchors and seven protected
model metadata checks pass. No new native hook site is introduced. ZIP CRC,
independent extraction and saved-copy hashes are verified.

New tests reproduce the observed 181 strike intervals and 193 body trigger,
verify pose alias identity/ground preservation, input-driven combo counting,
finite one-shot and Quick Run actions, and all seven spell-pose routes.
Fixtures are synthetic; no live v33 game/GPU test or actual installed Riku
clip execution was run here. The user's v32 test is the admitted baseline.
A fresh game test must verify appearance, Square input, contacts and spell FX.

Source patch (33 derivative commits), pinned upstream, original credits/
licences and validation receipts are included. No executable, extracted asset,
recording or disassembly ships. Behavior/confidence: docs/combat-model.md
Stage 372 in the source patch.
