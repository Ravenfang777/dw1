KH1FM SEVEN STYLES -- PROTOTYPE v34 (s373)

INSTALL
1. Fully close KH1FM. Disable v33 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v34, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s373 / PROTOTYPE v34 in kh1-dual-wield.log beside the game EXE.

Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
Sora model mods disabled. Use normal Sora. Existing INI/save style entries
are preserved. This is a native OpenKH DLL mod; no game assets ship.

SINGLE C -- REQUESTED MAPPING
Ground step 1: Riku 152
Ground step 2: Riku 151
Ground finisher: Riku 152
Air step 1: Riku 182
Air step 2: Riku 181
Air finisher: actual KH2 BASE SORA ability-free aerial combo finisher

Combo Plus/Air Combo Plus alternate the two base choices before the finisher.
Each continuation still needs a new Attack press in the late input window;
no entire combo is automatically queued. Native KH1 attack abilities retain
priority and can select their native combo lane. To isolate the listed base
sequence, temporarily unequip relevant native attack modifiers if needed.

The Sora finisher uses its own skeleton, weapon pose and battle data, not Riku
bone indices. The controller swaps the rig before sampling/contact geometry;
Sora's separate body retarget handles the transition. Real source root travel
and strike windows remain. No animation files need manual installation.

AERIAL CURE / STOP / AERO / GRAVITY
All four use Riku animation 193 while airborne. During a currently displayed,
accepted 193 cast, actual source collision shapes supply native pure-guard
objects for blocking/parrying and projectile deflection under KH1's native
clash rules. Guard objects deal no damage and grant no global invulnerability.
Unguardable attacks retain native rules. The guard retires on interruption,
cast end, missed/stale draw, teleport, owned action or style/binding change.

The whole finite visible 193 interval is the requested guard policy; it is not
claimed to be the original KH2 Riku script timing. An original 193 body attack
is NOT submitted by casting. Native KH1 spell execution, damage/healing, MP,
level and ability gates remain. Ground versions keep Riku item-use pose 9.

SQUARE AND TRIANGLE
The v33 aerial Square tap override and held latch are completely removed.
Free airborne Square again follows native KH1 selection, including Glide.
The existing ground Dodge Roll -> Wisdom Quick Run replacement remains.

Fresh Triangle in normal free gameplay:
  Ground: Riku 195 once.
  Air: Riku 194 once, held in air for its finite pose, then fall.
These are visual/root actions without added damage, spell/FX scripts, combo
chains or extra abilities. They do not cancel an already running native or
owned action. Native can-act/field/water, menu and shortcut gates remain;
scripted/context interactions retain their native path. Keyboard and pad
logical Triangle aliases are admitted. Holding Triangle does not queue repeats.

PRESERVED POSES, EFFECTS AND OTHER STYLES
Single C still uses base KH2 Sora for other spell-casting/Guard/ledge/Glide
fallback poses, and keeps its Riku movement/item/damage/idle poses. Fire,
Blizzard, Thunder and Cure keep their base Sora KH2 effects at native levels.
Gravity, Stop and Aero retain KH1 effects because base KH2 Sora has no direct
counterparts. Cure's visual release is normalized to 193 in air or 9 on ground.
The existing dual_b_spell_fx option controls the matching replacement effects.

The other six styles, IDs/exclusivity, equipped weapon/appearance and native
ability priority remain. Protected checks cover the complete offhand Glide/
color renderer, Dual A's working Superglide finisher, Dual B actions/FX,
Wisdom shots and Roxas loading/combos/Guard. No full hurt/Drive/spell takeover
hook or new native hook site is installed.

FIRST TEST
1. Equip Style: Single C. Check ground 152 -> 151 -> 152.
2. Check air 182 -> 181 -> Sora finisher, then normal return to fall/landing.
3. Tap/hold Square from a fresh jump: it should no longer select 193.
4. Cast aerial Cure, Stop, Aero and Gravity: check 193 and challenge its guard
   with a normally guardable melee attack or projectile. Test interruption/end
   too, so protection cannot linger after the cast. Compare grounded item casts.
5. Tap Triangle standing (195) and from a fresh jump/fall (194). Test menus,
   shortcuts and nearby field interactions separately; busy actions keep priority.
6. If a feature fails, return the full fresh kh1-dual-wield.log including startup.
   Useful diagnostics: SINGLE C COMBO MAP, SINGLE C CAST GUARD DATA/ACTIVE,
   SINGLE C TRIANGLE REQUEST/START, STYLE KH2 CAST and any UNAVAILABLE messages.

IDs (exclusive, 0 AP): Dual A 126, Dual B 125, Single A 124, Single B 123,
Anti 122, Dual C 121, Single C 120. Only the three Dual styles duplicate the
currently equipped weapon. Single C keeps Sora's appearance and one weapon.
No gauge, fixed donor weapon, second weapon choice, stat bonus or extra
ability/command entry is added. Unequipping the style restores native behavior.

INI defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
To remove our seven entries: set remove_dual_wield on; launch/load/save with
v34; close; disable the mod and Build again. DLL/INI changes need a full restart.

VALIDATION AND LIMITS
507 tests pass across 31 suites (161 style tests). Windows x64 release, PE
interface, 109 source/preservation checks, 11 native anchors and seven protected
model metadata checks pass. ZIP CRC, independent extraction, every packaged
entry hash and saved-copy identity/bytes are verified.

New synthetic fixtures cover exact ground/air order and native combo modifiers,
separate 209-bone Riku/237-bone Sora source identity, roots/contact preservation,
invalid source rejection, finite guard geometry with no damage, stale cast/
spell/generation rejection, 194/195 finite actions and all seven cast routes.
The native guard backend itself is unchanged; only a scoped wrapper calls it.

No actual v34 game/GPU test or installed clip execution was run here. Live
mixed-pose transitions, Triangle input and guard/projectile behavior need the
fresh-process game test. Existing v32 success is the admitted baseline.
Source patch (34 derivative commits), pinned upstream, credits/licences and
validation receipts are included. No game executable, extracted asset,
recording or disassembly ships. Rules/confidence: docs/combat-model.md Stage 373.
