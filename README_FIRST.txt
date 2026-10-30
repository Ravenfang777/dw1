KH1FM FOUR STYLES -- PROTOTYPE v16 (s355)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v15 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v16, then Build and Run.
   Panacea is required. F1 does not reload a native DLL.
3. The abilities menu now has four 0-AP, mutually exclusive styles.
   New Single entries start disabled. Existing Dual IDs/equipped state stay.

Keep old integrated/offhand Lua, Synch/moveset routers, duplicate Sora
model mods and the full KH2 Combat overhaul disabled. Requires normal
Sora and KH1FM/KH2FM in the same PC 1.5+2.5 installation. Use this mod's
manifest; do not replace the shared dinput8.dll. KH2 data is read from
your own install at startup; no game animation/model/effect assets ship.

FOUR EXCLUSIVE PASSIVE STYLES
- Style: Dual A (126): Valor. Existing working real-finisher Superglide
  retained, with its movement, native blade contacts and fall handoff.
- Style: Dual B (125): Final. Native-selected Dodge Roll starts its
  moving idle-body blade spin explicitly, without needing a second
  Square press or a later control pulse. Guard is the stationary spin.
  The original native roll motion/flags/voice are skipped when admitted.
- Style: Single A (124): Limit. One equipped KH1 weapon. Base ground/air
  attacks; matching movement, jumping, falling, landing, item, damage,
  ledge/hang/climb and idle/scene-idle tracks. Native Guard/Roll use
  matching Limit visual slots. Glide keeps the held-weapon pose as in A.
  Superglide starts ONE real Limit base aerial finisher; release and
  press again to repeat. Existing Glide/Superglide ability gates remain.
- Style: Single B (123): Wisdom. One equipped KH1 weapon. Wisdom base
  shooting combos and matching movement/jump/item/damage/ledge/idle
  tracks. Native-selected Dodge Roll starts actual Wisdom Quick Run,
  followed by Quick Run End. Release Square to end the dash. Dodge Roll
  must still be equipped; no Quick Run growth ability is granted.

Enabling any style disables the previous style in place. Single styles
never display a duplicate or require its resource. All four retain
native attack-ability lane priority, as Dual A does; disable equipped
KH1 attack abilities if you specifically want to inspect the donor's
base ground/air combos. Combo Plus/Air Combo Plus remain native choices.
Unequipping restores ordinary KH1 behavior. No Drive gauge, drain,
timer, costume/recolour, stat/AP bonus, partner removal, extra inventory
weapon, second weapon selection or additional ability reward is added.

MAGIC
- Dual B uses Final casting tracks and spell subs. Single B uses
  Wisdom's. Fire/Blizzard/Thunder/Cure at their native levels now show
  the real KH2 MAG/BDX/PAX effects, with owned KH1 visual drawing hidden.
- Native effect creation, simulation, audio and KH1 spell damage,
  healing, MP, targeting and levels continue. KH2 spell-script damage
  and heal events remain visual-only, so there is no extra spell damage.
- The draw filter is scoped to Sora's corresponding accepted cast and
  its native effects/children. A loaded file alone cannot hide a spell.
  Missing packages, failed/unadmitted KH2 scripts or unknown ownership
  retain native drawing. No effect/spell state or resource is patched.
  The new render filter is verified for the supplied Steam executable;
  other builds retain native visuals if their filter is unavailable.
- Gravity, Stop and Aero retain native effects, using the selected B
  style's compatible casting tracks. Native audio remains for spells.
- Limit has no ordinary Magic command in KH2. Single A's missing or
  non-cast magic slots use verified compatible base KH2 Sora cast tracks;
  no Limit command or special is substituted. Native KH1 spells remain.
- Unknown native actions, unsupported models and missing exact donor
  animation matches retain their current native poses. Dedicated event
  gestures, swim/flight and unrelated actions are not guessed by ID.

WISDOM SHOTS
Actual Wisdom base attack Effect triggers run its model BDX/PAX script.
Only that object's projectile attack shapes submit new native contacts,
using its ATKP power/re-hit data and native hit feedback. Released shots
can finish after the combo. All shot/visual state retires on style,
weapon, actor or map changes. No direct HP or MP write is added. No
Drive arrival or persistent form aura is started. This is the first
in-game test of the Single styles and the isolated Wisdom shot runtime.

FIRST TEST
1. Wait for STYLE TABLE READY, donor data and KH2 SPELL EFFECTS READY.
2. Dual B: equip Dodge Roll and use Square with a direction. Look for a
   moving blade spin and DUAL B COMMITTED SPIN START. Verify stationary
   Guard too. The log now separates native Roll entry, admission and
   action start, so a fallback has a specific stage to diagnose.
3. Dual B: cast Fire/Blizzard/Thunder/Cure on ground and in air. Confirm
   KH2 effects with the matching native visuals hidden and the same
   MP/healing/damage. Native-only Gravity/Stop/Aero should remain visible.
4. Switch to Single A, then Single B: only one blade should remain, and
   the previous style should disable. Inspect movement, ground/air
   attacks, jumps/fall/landing, damage, items, ledges and magic.
5. Single A: test held Glide and one-shot finisher Superglide. Single B:
   test Wisdom shots with/without a target and Quick Run with Dodge Roll.
6. Check map/weapon/style changes, unequip, pause/menus and interruption.
   Dual A's already-working finisher should remain the same.

SETTINGS / LOG -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
Existing kh1-dual-wield.ini is preserved. Missing keys use defaults.
  dual_b_spell_fx = on
KH2 visuals/native draw filtering for both B styles' four matching
spells. Off restores native spell drawing and removes the imported
spell visual layer; Wisdom shots and casting animations remain.
  idle_speed = 0.75
Combat/supported scene-idle rate, .10..2.00; 1.0 = authored speed.
  offhand_only_test = off
On isolates left imported contacts in Dual styles. Single styles keep
their one weapon. Native spells/items/party are not isolated by this.
  remove_dual_wield = off
Uninstall only: set on, launch/load/save with v16, close, disable mod,
then Build again. It removes only all four custom style entries.
Restart the game after INI edits.

kh1-dual-wield.log: check s355 and PROTOTYPE v16. Useful new markers:
  STYLE NATIVE ROLL ENTRY / STYLE NATIVE DODGE REPLACED
  DUAL B COMMITTED SPIN START / STYLE COMMITTED DODGE START FAILED
  SINGLE STYLE DATA / SINGLE STYLE READY / SINGLE B QUICK RUN START
  SINGLE B WISDOM SHOT / SINGLE B WISDOM SHOT CONTACT
  STYLE B REAL KH2 SPELL FX / DUAL B NATIVE SPELL DRAW FILTERED
If something remains native or an effect is missing, return the NEW
log and the affected action/style. A short recording helps appearance.

VALIDATION / LIMITS
412 automated tests passed across 27 suites, including 111 style tests.
Windows x64 release cross-build, PE imports/exports, native hook anchors
and FX scope checks passed. Original/saved ZIP CRC, extraction and entry
hashes are verified. Actual v16 gameplay/GPU rendering and installed
Limit/Wisdom donor availability require this fresh-process game test.
User reports confirm the prior v15 A finisher and KH2 spell layer; they
do not establish the new v16 roll fix, draw filtering or Single styles.
Keep v15 if you need to revert. Source patch, credits/licenses and
validation receipts are included; no game bytes/dumps are included.
