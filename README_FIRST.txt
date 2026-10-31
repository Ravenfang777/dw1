KH1FM FIVE STYLES -- PROTOTYPE v22 (s361)

INSTALL
1. Fully close KH1FM. Disable v21 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v22, then Build and Run.
   Panacea and your installed KH2FM are required. This is a native DLL mod,
   not a Lua script. F1 cannot reload it; always restart the game.
3. Confirm s361 / PROTOTYPE v22 in kh1-dual-wield.log beside the game EXE.

Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
Sora model mods disabled. Use normal Sora. No game assets are included.
The ZIP contains the install files, licences, source patch and validation.

CHANGES IN THIS TEST
Dual B Quick Run: the current v21 log finally identifies a Guard/Roll
collision. Wisdom data and the Roll hook load, but Guard takes the press
first; the older roll handler then tries a native Roll while Guard already
owns Sora. v22 selects Guard after KH1 prepares the current direction and
prevents that committed press from falling through to another action.
Moving Square still goes through KH1's actual native Roll selection and
then the existing Wisdom Quick Run replacement. Native Dodge Roll must be
equipped. No extra movement ability is granted. The dedicated Wisdom dodge
profile and both equipped-weapon copies are retained.

Fire endings: the KH2 cast now recognizes the authored native recovery
from its actual request and matching animation header, including a reused
header buffer. An old header cannot advance the cast. Both phases share
one animation clock/effect identity, while a real new Fire starts its own
cast normally. Native costs, damage, targeting and recovery remain.
The recording confirms the flash; v21 did not log the exact retirement
reason. This repairs a fragile pointer assumption and adds concise phase
and exit notes so any remaining flash can be traced precisely.

Single B's working KH2 Guard retains its actual native Guard-row witness.
The raw Fire-recovery motion is still not treated as Guard. Attack-table
reports now log once per actor/style generation, reducing repeated IO;
all native reads used to choose damage rows remain current.

FIRST TEST -- FRESH GAME PROCESS
1. Dual B: with native Guard AND Dodge Roll equipped, stand still and
   tap Square for Guard spin. Hold a direction and tap Square for Wisdom
   Quick Run. Try holding/releasing Square, then a second Quick Run.
2. Single B: check its confirmed KH2 Guard and existing Quick Run.
3. Both B styles: cast Fire separately and repeatedly on the ground and
   in the air. Check the ending and return to idle/fall for a KH1 flash.
4. Recheck basic combos, native attack abilities, and style/map changes.

If a problem remains, send the FULL current kh1-dual-wield.log including
startup from beside KINGDOM HEARTS FINAL MIX.exe before another restart.
Useful new notes:
  STYLE PREPARED SQUARE HOOK: installed=true
  STYLE CAST REQUEST / STYLE CAST HANDOFF / STYLE CAST END
  STYLE FIRE RECOVERY: cast=... 0x36->0x3D (or 0x83->0x8A)
Existing dodge notes:
  STYLE NATIVE ROLL ENTRY / STYLE NATIVE DODGE REPLACED
  DUAL B QUICK RUN REQUEST / DUAL B QUICK RUN START
  STYLE QUICK RUN ADMISSION FAILED

RETAINED STYLES
Five exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed).
Only Dual styles duplicate the currently equipped weapon. There is no
second weapon choice, Drive gauge/state, outfit, stat bonus, extra ability
or partner removal. Native attack abilities keep their native combo lane.
A finisher Superglide, Single B .75 Run, Anti's weaponless base glide/roll,
body combat, darkness aura and magic/item/summon restrictions remain.

Both B styles retain KH2 Fire, Blizzard, Thunder and Cure effects at all
native levels and existing native visual filtering. Gravity/Stop/Aero
keep native effects. Native KH1 damage, healing, levels and costs remain.
Single A retains KH2 cast poses with native KH1 effects.

Your existing kh1-dual-wield.ini beside the EXE is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Single B Run uses .75 independently of idle_speed. Offhand-only testing
is for Dual styles; it does not isolate spells, companions or Single/Anti.
To uninstall custom entries: set remove_dual_wield on, launch/load/save
with v22, close the game, disable the mod and Build again. Only the five
custom entries are removed. DLL/INI changes need a full restart.

VALIDATION AND LIVE LIMIT
443 portable tests across 27 suites pass (142 style tests), as do the
Windows x64 release, PE interface, 10 new native selector anchors and
63 source-scope checks. Tests include Fire buffer reuse/publication lag,
repeated casts, pending Guard versus legacy Roll, Quick Run completion,
first-frame flags, Guard witnesses and the prior five-style regressions.
The archive has been CRC-checked, extracted and compared byte for byte.

No fresh v22 game/GPU execution was performed. These checks do not prove
that either remaining live symptom is resolved; run the test above.
Native input/visual handoffs remain the relevant live validation point.
The source patch, pinned upstream, credits and validation are included;
no game executable, recording, extracted assets or disassembly is shipped.
