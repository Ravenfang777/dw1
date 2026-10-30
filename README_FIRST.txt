KH1FM DUAL STYLES -- PROTOTYPE v14 (s353)

INSTALL / UPDATE
1. Fully close KH1FM. Disable v13 and every older Dual Wield prototype.
2. Install this ZIP as one OpenKH mod, enable v14, then Build and Run.
   Panacea is required. F1 does not reload a native DLL.
3. Equip Style: Dual A or Style: Dual B. Existing names/IDs, AP,
   learned/equipped state and mutual exclusion are preserved.

Keep older integrated/offhand Lua, Synch/moveset routers, duplicate
Sora-model mods and the full KH2 Combat overhaul disabled. Normal Sora
and KH1FM/KH2FM in the same PC 1.5+2.5 installation are required.
Donor animations come from your KH2FM files. No game assets ship.
Use the included manifest; do not replace the shared dinput8.dll.

CHANGES IN v14

Style: Dual A -- Valor finisher Superglide
- Superglide repeats Valor's base aerial-combo finisher animation while
  native Superglide is active. The motion is read from actual Valor
  combo data, with real rig/clip admission, rather than guessed.
- This is an animation replacement. KH1 still controls Superglide's
  speed, steering, collision, ability gate and ending when released.
- Donor root travel, hit windows, events and voices are not executed.
  No Superglide attack damage or finisher spell/effect is added.
- Body and both weapon tracks use the finisher. The old native-glide
  attachment refresh cannot overwrite the admitted finisher's offhand.
- Regular Glide keeps its native held pose and live-hand refresh.
  Missing finisher data retains the native Superglide pose/duplicate.

Style: Dual B -- stationary Guard and moving Dodge Roll spins
- Guard keeps one cycle of the previous Final idle-body/Keyblade spin.
  The extra native attack voice is suppressed. Swing/trail sounds and
  native hit impact/audio remain; ordinary attack voices are unchanged.
- Dodge Roll now performs a MOVING version of that same spin, replacing
  v13's Master aerial dodge. Use directional input to move/steer during
  its one cycle. It uses Final's normal walk/run movement parameters.
- Sora keeps Final's looping idle body while both blades spin, just as
  during Guard. The blade contact windows are identical to Guard's.
- There is no Master hop, new airborne input, follow-up combo window,
  Aero spell/effect, MP cost or invulnerability grant. Master data is
  no longer loaded. Moving over an edge permits normal falling.
- Guard and Dodge Roll still require their respective native equipped
  abilities. Native tilt chooses between them when both are equipped.
  Missing/invalid roll-spin data retains native Dodge Roll.

DUAL B MAGIC -- KH2 ANIMATIONS
B already targeted Final Form's KH2 casting animations in v13; this
version retains that route for all seven KH1 spells, on ground and air.
The log now identifies those casts explicitly as DUAL B KH2 CAST.
  Fire             -> Final Fire family      (56 / 58)
  Blizzard         -> Final Blizzard family  (59 / 61)
  Thunder/Gravity  -> Final Thunder family   (62 / 64)
  Cure/Stop/Aero    -> Final Cure family      (65 / 67)
KH1 still owns MP, spell levels, spell release/projectiles/effects,
damage and movement. The animation donor never runs a KH2 spell event.
The v10 Fire invalid-read fix remains. Dual A casting stays default KH1.

RETAINED
Dual A uses Valor combat. Dual B uses Final's actual base ground/air
combo selector with three slots plus Combo Plus/Air Combo Plus. Both
styles retain native attack-ability priority for an entire affected lane.
Disable native ground action attacks (Vortex, Counterattack, Blitz,
Slapshot, Sliding Dash, Ripple Drive, Stun Impact, Gravity Break,
Zantetsuken) or air action attacks (Aerial Sweep, Hurricane Blast) to
test an isolated imported base combo. Combo Plus alone retains that combo.

B retains regular-Glide floor hover and its prior Superglide behavior.
To test regular Glide, unequip Superglide, which has native priority.
Each style duplicates the equipped KH1 weapon with no second selection
or inventory copy. Unequipping removes the duplicate/restores native KH1.
No Drive gauge, drain/timer, transformation, costume, stats/AP bonus or
extra native ability is added. Existing INI settings are preserved.

FIRST TEST
1. A: equip Superglide and check the repeating Valor aerial finisher,
   both blades, turning and button-release ending. Regular Glide should
   still be held normally. Check map and weapon changes for stale poses.
2. B: equip Guard, use neutral stick and check one stationary spin with
   no attack voice, MP loss or Aero effect. Check weapon/hit sounds.
3. Equip Dodge Roll. Use directional input to start a moving spin; steer
   during it and confirm it ends once. Compare both blade contacts near
   a single enemy; exclude party damage when attributing enemy HP loss.
4. Cast each spell from idle and from the air. Check Final's KH2 cast
   animation and native spell effects/MP. Casting should not add another
   spell, use Master animations or automatically start an attack.
5. Check damage interruptions, collision, landing, style/weapon changes,
   map transitions and unequipping. Check native attack-ability priority.

SETTINGS / LOG -- NEXT TO KINGDOM HEARTS FINAL MIX.exe
kh1-dual-wield.ini (existing file preserved; restart after edits):
  idle_speed = 0.75
Combat/supported scene-idle rate, including both spin body tracks.
1.0 is authored idle speed; accepted range .10..2.00.
  offhand_only_test = off
On isolates left imported contacts. Native spells/items/party remain.
  remove_dual_wield = off
Uninstall only: set on, launch/load/save with v14, close, disable the mod
and Build again. It removes only both custom style entries.

kh1-dual-wield.log: look for s353, PROTOTYPE v14, DUAL A SUPERGLIDE DATA,
DUAL B MOVING SPIN REQUEST, DUAL B ACTION DATA and DUAL B KH2 CAST.
Return this NEW log and a short recording if animation, movement or
contact is wrong. Data logs report whether the real donor was admitted.

VALIDATION
330 local tests passed across 18 suites, including 101 Dual Wield tests.
They check the finisher route/fallback, attachment ownership, identical
Guard/roll contact timing, steerable finite movement without a hop or
extra ability, scoped voice suppression, all seven ground/air cast
routes and retained combo/input/geometry behavior.
Windows x64 release cross-build and PE imports/exports passed. No new
native hook/address; retained Steam checks are labelled as historical.
ZIP CRC/extraction/all-entry hashes verified. Cumulative source patch,
recovery evidence, original credits and licenses included. No live game
execution or installed donor appearance/contact validation here.
Keep v13 if you need to revert.
