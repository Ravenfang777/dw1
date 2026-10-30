KH1FM FIVE STYLES -- PROTOTYPE v17 (s356)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v16 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v17, then Build and Run.
   Panacea is required. F1 cannot reload a native DLL.
3. Equip one style in Sora's abilities menu. Style: Anti is new, 0 AP,
   and starts disabled. Equipping a style disables the previous style.

Keep older integrated/offhand Lua, Synch/moveset routers, duplicate Sora
model mods and the full KH2 Combat overhaul disabled. Requires normal
Sora and KH2FM in the same installation. Runtime reads your own KH2
resources; no game assets are supplied. Do not copy this DLL into the
scripts folder or enable multiple prototype versions together.

THE FIVE STYLES
  Style: Dual A   (126): Valor, two copies of the equipped KH1 weapon.
  Style: Dual B   (125): Final, two copies of the equipped KH1 weapon.
  Style: Single A (124): ordinary KH2 Sora, one equipped KH1 weapon.
  Style: Single B (123): Wisdom, one equipped weapon, shots/Quick Run.
  Style: Anti     (122): Anti-form body animations and unarmed combat.

All are 0 AP. No second weapon selection, Drive gauge, timer, outfit,
recolour, bonus stats, partner removal or additional ability is added.
Single A/B never create a duplicate. Anti hides the equipped Keyblade
visually, keeping normal Sora's model/colour and his saved equipment.
Unequipping or changing a style retires its controller/pose/effects.

WHAT CHANGED
Single A now uses base KH2 Sora rather than Limit: matching movement,
attacks, magic poses, items, damage, jump/fall/landing and ledge donors.
Its Superglide starts one actual base Sora aerial finisher. Regular
Glide stays held/native as before. Missing visual matches fall back to
KH1. Existing KH1 attack abilities still retain their native combo
lane in the four weapon styles; no donor action ability is granted.

Anti uses its intrinsic ground/air combos, body hitboxes, authored
attack movement, Square Anti Glide and combo Side Spin where present.
Matching locomotion, damage, jump/landing, idle and ledge animations
use Anti data. Its original PAX body effects share the isolated FX
renderer. Magic, items, summons and physical special commands are
blocked in menus, targets/shortcuts and command dispatch before costs.
Field interactions stay usable. Native movement/collision/ability
gates remain in charge outside attack actions. This is the first live
prototype of Anti as an ability; exact retargeting still needs testing.

Dual B's moving spin uses the working native committed-dodge hook,
with real loaded hit metadata and base Sora movement numbers. It no
longer waits for the duplicate weapon resource to start the action.
Current drawn-blade geometry is still required for offhand damage.
Single B's working Quick Run and Dual A's real finisher are retained.

SPELL EFFECT OVERLAP
The native filter now captures Sora's actual spell-script work and
follows its asynchronous VM updates and effect descendants. v16 had
mistaken an effect-flag pointer for its caster. Only a cast whose KH2
visual script actually starts can hide the matching native rendering.
Native MP, healing, damage, effect simulation and audio still run.

The imported spell packages cover Fire, Blizzard, Thunder and Cure,
all three levels, in Dual B and Single B. Gravity, Stop and Aero keep
native effects. Single A has KH2 cast poses with native KH1 effects.
Unknown effects/casters and missing replacements retain native draws.
The new ownership path and complete remastered-layer suppression need
a fresh game test; local checks cannot prove their final appearance.

FIRST TEST
1. Wait for STYLE TABLE READY, donor data and KH2 SPELL EFFECTS READY.
2. Dual B: with Dodge Roll equipped, use Square plus direction. Check
   for DUAL B COMMITTED SPIN START and the moving blade spin; verify
   stationary Guard too. Test Fire/Blizzard/Thunder/Cure ground/air.
3. Single A: verify base Sora attacks/movement and actual finisher
   Superglide. Single B: confirm Quick Run and shots still work.
4. Anti: verify no weapon, ground/air combos, moving Square Anti Glide,
   Side Spin during a combo, jumping/falling/damage and ledge poses.
   Try Magic, Items and shortcuts: no cast, item or cost should occur.
5. Switch among all five styles, unequip, change map/weapon, take damage,
   and pause. Previous style effects and ownership should retire.

LOG / SETTINGS -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
kh1-dual-wield.log should contain s356 and PROTOTYPE v17.
Useful markers:
  SINGLE STYLE DATA: KH2_Sora_base / KH2_Sora_air_finisher
  DUAL B ACTION DATA / STYLE NATIVE ROLL ENTRY
  DUAL B COMMITTED SPIN START / STYLE COMMITTED DODGE START FAILED
  STYLE NATIVE SPELL OWNER / DUAL B NATIVE SPELL DRAW FILTERED
  ANTI STYLE DATA / ANTI STYLE READY / ANTI ACTION REQUEST
Return a fresh full log if B still rolls, a spell still doubles, or
Anti data/actions/poses fail; old version logs cannot identify v17.

Existing kh1-dual-wield.ini is preserved. Missing keys use defaults:
  dual_b_spell_fx = on
Off restores native drawing and removes imported B spell visuals;
Wisdom shots and Anti PAX remain. Casting animations are unchanged.
  idle_speed = 0.75
Supported combat/scene idle rate; .10..2.00, 1.0 = authored speed.
  offhand_only_test = off
On isolates left imported contacts in Dual styles only. Single and
Anti contacts keep their normal sources. Spells/party are unaffected.
  remove_dual_wield = off
For uninstall: set on, launch/load/save using v17, close, disable the
mod and Build again. Removes only the five custom entries. Restart
KH1 after every native DLL or INI change.

VALIDATION / LIMITS
420 local tests passed across 27 suites, including 119 style tests.
Windows x64 release cross-build and expected imports/exports passed.
Steam native factory/scheduler fields, whole prologues and draw gate
match the supplied executable. New spell ownership hooks are Steam
only; no Epic address is inferred. No Windows game/GPU test was run.
Source patch, provenance, licences and validation receipts are included.
