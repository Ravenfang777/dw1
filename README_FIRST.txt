KH1FM FIVE STYLES -- PROTOTYPE v18 (s357)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v17 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v18, then Build and Run.
   Panacea is required. F1 cannot reload a native DLL.
3. Equip one style. The five existing IDs/states remain: Dual A 126,
   Dual B 125, Single A 124, Single B 123 and Anti 122. All are 0 AP.
   Enabling a style disables the previously equipped style.

Keep older integrated/offhand Lua, Synch/moveset routers, duplicate Sora
model mods and the full KH2 Combat overhaul disabled. Requires normal
Sora and your installed KH2FM in the same installation. No game assets
are supplied. The DLL belongs to this OpenKH mod, not the scripts folder.

WHAT CHANGED
Dual B now uses Quick Run, through the same committed native-dodge path
that works for Single B. Wisdom Quick Run/Quick Run End body motions
203/204 are ported into the Final donor, with both Final idle weapon
tracks retained. No moving-spin hitboxes or growth ability is granted.
Native Dodge Roll eligibility/input still gates the replacement. Guard
keeps the stationary keyblade spin; normal Final combos stay in place.

Single B's running animation plays at 75% on its own continuous clock.
Native clip wrap and repeated render passes cannot reset/accelerate it.
This changes the pose rate, leaving movement speed and Quick Run alone.
Dual A's configured idle speed and the other styles' run rates remain.

Spell target impacts now inherit the original cast's native draw tag.
The prior filter followed the caster VM; native contacts create target
sparks separately. The shared attack constructor records the actual
Sora/canonical spell/cast identity, then the original impact creation
runs in that scope. Its particles can be hidden by the existing draw
filter after the same cast's KH2 replacement starts. Every original
contact, hit record, spark creation, target binding and audio still runs.
Other actors, melee, unknown/unadmitted effects and missing replacements
retain native drawing. No native HP/MP or effect-state patch is added.
This is a fresh live test of target-impact coverage, not a verified
claim that every remastered visual layer is gone.

Anti darkness uses actual looping, body-bound effects named by Anti's
idle/arrival PAX triggers. They start while Style: Anti is equipped and
retire on unequip, actor/weapon/room generation or invalid scene scope.
The one-shot transformation bursts and motion-specific effects are
excluded. Sora keeps his normal model/colour. Attack effects have a
separate bounded lifetime; aura triggers cannot double on every attack.
No gauge, timer, outfit, stat bonus, partner change or extra ability.
If the installed donor has no matching persistent effect, the log says
which elements were found; no arbitrary effect ID is guessed.

Anti Glide is restored: its real row 11 has no hitbox, which v17's
filter incorrectly excluded. Square can use its authored movement,
no-gravity and initial invulnerability. Body attacks and Side Spin
remain. Anti still blocks magic, items, summons and physical specials.

FIRST TEST
1. Wait for STYLE TABLE READY, data and KH2 SPELL EFFECTS READY.
2. Dual B: equip Dodge Roll, hold a direction and press Square. Check
   for Quick Run and DUAL B QUICK RUN START in the log. Test release,
   stationary Guard, both blades, interruption and map transitions.
3. Dual B and Single B: hit a target with Fire/Blizzard/Thunder, then
   test Cure. Look for STYLE NATIVE SPELL TARGET FX and DRAW FILTERED.
   Check that damage/healing/MP still work and target visuals no longer
   double. Return the fresh full log if overlap remains.
4. Single B: hold Run and confirm its animation is slower while travel
   speed stays the same. Verify Quick Run and shots still work.
5. Anti: stand idle, run and attack. Check for the darkness particles,
   ANTI DARKNESS AURA DATA/START, and Square Anti Glide. Unequip and
   change styles/maps: the aura should disappear. Try Magic/Items and
   shortcuts: no cast, item use or cost should occur.

SPELL COVERAGE
KH2 effect packages cover Fire, Blizzard, Thunder and Cure, all three
native levels, in Dual B and Single B. Gravity, Stop and Aero retain
native effects. Single A uses KH2 cast poses with native KH1 effects.
Native KH1 damage, healing, costs and levels remain authoritative.

LOG / SETTINGS -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
kh1-dual-wield.log should show s357 and PROTOTYPE v18.
Useful new markers:
  DUAL B ACTION DATA: quick_run_ready
  DUAL B QUICK RUN REQUEST / DUAL B QUICK RUN START
  STYLE NATIVE SPELL TARGET FILTER READY / SPELL TARGET FX
  ANTI DARKNESS AURA DATA / ANTI DARKNESS AURA START

Existing kh1-dual-wield.ini is preserved; missing keys use defaults:
  dual_b_spell_fx = on
Off removes B imported spell visuals/filtering. Wisdom shots, Anti
PAX and casting animations remain.
  idle_speed = 0.75
Supported idle/scene-idle rate, .10..2.00. Single B Run is fixed at .75.
  offhand_only_test = off
On isolates left imported contacts in Dual styles only. Single/Anti
contacts, native spells and party damage are unaffected.
  remove_dual_wield = off
For uninstall: set on, launch/load/save using v18, close, disable this
mod and Build again. Removes only the five custom entries. Restart KH1
after native DLL or INI edits.

VALIDATION / LIMITS
426 local tests passed across 27 suites, including 125 style tests.
Windows x64 release build and expected imports/exports passed. Nine
new native constructor/target-spark anchors match the supplied Steam
executable; all originals are preserved. New spell filter hooks are
Steam only, with no inferred Epic addresses. No game/GPU test was run.
Darkness appearance, Quick Run blade placement and complete target
visual suppression need a fresh game test. Missing metadata and
unsupported rendering programs are logged. Source patch, provenance,
licences and validation receipts are included; no game assets/dumps.
