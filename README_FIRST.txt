KH1FM FIVE STYLES -- PROTOTYPE v24 (s363)

INSTALL
1. Fully close KH1FM. Disable v23 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v24, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s363 / PROTOTYPE v24 in kh1-dual-wield.log beside the game EXE.

This is an OpenKH native DLL mod, not a script. Keep the full KH2 Combat
overhaul, older offhand/moveset Lua and duplicate Sora model mods disabled.
Use normal Sora. No game assets are supplied.

VISUAL CHANGES
Dual A regular Glide: the duplicate now follows a hand rebuilt from the
native body's current root and parent-local joints, instead of trusting
a cached/blended helper hand-world matrix. This avoids applying the actor
placement twice and refreshes the held attachment before the body queue.
The duplicate keeps a hand-local calibration, with actor/model/weapon and
current-frame guards. A rejected sample is not drawn at a stale location.
Sora's native body and glide movement are not rewritten. A's actual
finisher Superglide retains its imported attack poses and contacts.

Dual B Quick Run: the current log shows 40 successful starts and 28
put-away calls while Dual B is active. Wisdom's field movement rule was
stowing the weapon during Quick Run/end, which also removed the duplicate
and requested a colored vanish effect. Owned Dual actions now keep both
real equipped meshes out through that movement and its ending. The
primary grip renderer uses the same visibility result. The dodge's body,
movement, timing and lack of hitboxes stay as in the working v23 path.

Passive weapon admission now uses KH1's normal show-weapon routine when
needed, restoring its normal colour/alpha along with its visibility flag.
No palette, texture or weapon appearance file is replaced. Both blades
remain copies of the weapon currently equipped.

FIRST TEST -- FRESH GAME PROCESS, NO ENEMIES NEEDED
1. Dual A: use regular Glide straight, then turn both ways repeatedly.
   Check the offhand stays in the palm without jumping or disappearing.
   Land, repeat, change map and try again. Check Superglide still starts
   A's actual finisher normally.
2. Dual B: outside battle, Quick Run with short taps, holds/releases and
   repeated direction changes. Check TWO normally textured Keyblades
   through the run and its ending, with no colored put-away outline.
3. Check one Guard and Fire cast afterward, retaining v23's working
   action selection and smooth Fire recovery.

If a visual issue remains, send the FULL fresh kh1-dual-wield.log including
startup, from beside KINGDOM HEARTS FINAL MIX.exe, before another restart.
Relevant notes:
  DUAL A GLIDE ATTACHMENT: current native root/local hierarchy...
  DUAL B QUICK RUN REQUEST / DUAL B QUICK RUN START
  Keyblade put away: ... (should not occur during Dual B Quick Run)
  STYLE COMMITTED GUARD BRANCH / STYLE FIRE RECOVERY
A short recording of the same turn/dodge helps match the visual sample.

RETAINED
Five exclusive 0-AP IDs: Dual A 126 (Valor), Dual B 125 (Final),
Single A 124 (base KH2 Sora), Single B 123 (Wisdom), Anti 122 (unarmed).
Only Dual styles duplicate the equipped weapon. Native attack abilities
keep their native combo lane. No second weapon choice, Drive state/gauge,
outfit, stat bonus, extra ability or party removal. Single B .75 Run and
Guard, A finisher Superglide, Anti's weaponless movement/body combat/aura
and magic/item/summon restrictions remain. Native ability gates remain.

Both B styles retain KH2 Fire/Blizzard/Thunder/Cure effects at native
levels and the existing native visual filter. Gravity/Stop/Aero retain
native effects; Single A retains KH2 cast poses with native KH1 effects.
Native KH1 damage, healing, levels, acceptance and costs remain. The v23
Fire queue/clock handoff is retained; KH2 spell-combo stage chaining is
still not part of the isolated native-cast overlay.

Your existing kh1-dual-wield.ini beside the EXE is preserved. Defaults:
  dual_b_spell_fx = on
  idle_speed = 0.75
  offhand_only_test = off
  remove_dual_wield = off
Single B Run uses .75 independently. Offhand-only testing is for Dual
styles, not spells, companions or Single/Anti. To remove custom entries,
set remove_dual_wield on, launch/load/save with v24, close, disable the
mod and Build again. Only the five custom entries are removed.
DLL/INI changes require a full restart.

VALIDATION AND LIVE LIMIT
449 tests pass across 27 suites (147 style tests), including the real
Win64 Guard bridge test retained from v23. New fixtures cover 80 turning/
translated native roots, root-local duplication, invalid hierarchies and
the real Quick Run/end lifecycle with its donor field-stow classification.
Windows x64 release, PE interface, eight native appearance anchors and
80 source-scope checks pass. ZIP CRC/extraction and saved-copy entry
hashes are verified.

No fresh v24 game/GPU rendering test was performed. These checks do not
prove the two visual symptoms resolved; use the live checks above.
Source patch, pinned upstream, credits, licences and validation receipts
are included. No game executable, recording, extracted asset or
disassembly is distributed.
