KH1FM SEVEN STYLES -- PROTOTYPE v36 (s375)

INSTALL
1. Fully close KH1FM. Disable v35 and every older Dual Wield prototype.
2. Import this ZIP into OpenKH, enable ONLY v36, then Build and Run.
   Panacea and your installed KH2FM are required. F1 cannot reload a DLL.
3. Confirm s375 / PROTOTYPE v36 in kh1-dual-wield.log beside the game EXE.

Keep the full KH2 Combat overhaul, older offhand/moveset Lua and duplicate
Sora model mods disabled. Use normal Sora. Existing INI/save style entries
are preserved. This is a native OpenKH DLL mod; no game assets ship.

WHY v35 FELL BACK TO KH1
Your s374 log confirms that Vicinity Break failed startup qualification, which
set Single C attack_adapter=false for both ground and air. Riku loaded, and
193 aerial casting still created its native guard objects.

v36 separates named Sora strikes from generic Riku melee discovery. Real
Strength- or Magic-scaled damage records and valid body/primary weapon shapes
are admitted for these specifically requested Sora clips. Source power/stat,
geometry, root and timing are preserved; no invented hitbox or added spell.
Heals, invalid/missing geometry, scripts and donor spell events stay excluded.
The original generic Riku filter and native contact backend are unchanged.

Ground and air now qualify independently. If one source still cannot qualify,
only that lane keeps native control and logs why; it cannot disable the other.
There is no automatic substitution of a different attack. Startup now logs
actual Sora source geometry and ATKP stat/kind/power instead of a generic error.
The previous log did not identify which predicate failed for Vicinity Break;
valid Magic/body-source cases are covered by new regression fixtures.

SINGLE C -- REVISED MAPPING
Ground step 1: Riku 152
Ground step 2: Riku 151
Ground finisher: KH2 base Sora Vicinity Break
Air step 1: KH2 base Sora first air combo hit (181)
Air step 2: KH2 base Sora Horizontal Slash
Air finisher: Riku 182, ending ten frames early

This uses the user's revised air list. Horizontal Slash is the second Attack
press in the combo. The former Triangle 195/194 commands are fully removed;
Triangle again follows native behavior. There is no custom aerial Square
action. Existing grounded Dodge Roll -> Wisdom Quick Run remains.

Vicinity Break and Horizontal Slash resolve from actual KH2 ability-180/99
source rows, with their real body/primary weapon contacts. Neither ability is added or
separately equipped. Vicinity Break fills the finisher slot rather than its
original surrounded-foe opening condition. Donor scripts/events do not run.
Existing native trail, impact/contact feedback and source attack records remain.

Combo Plus/Air Combo Plus alternate the two base choices before the finisher.
Each continuation needs a new Attack press in its late input window. Native
KH1 attack abilities keep priority; temporarily unequip relevant native attack
modifiers if needed to isolate this listed base sequence.

Riku 182 is 148 frames in the admitted bank. Its host finisher now ends at
138, preserving the source playback speed, root prefix and all five contact
windows (the last ends at 122). Only the final ten frames are omitted. The
original animation bank and all other source clips are unchanged. Unexpected
source data that would lose a hit is rejected. This first ten-frame cut still
needs a visual check to confirm it removes the drop-off you noticed.

Sora's three combo slots use his own rig, equipped-weapon pose and battle
records, with separate body mapping. Riku's other steps use his rig. No foreign
bone channels are relabelled; old collision sweeps retire when the rig changes.
No animation files need manual installation.

CASTING AND OTHER PRESERVED FEATURES
Aerial Cure/Stop/Aero/Gravity still use Riku 193 with the v35 actual-draw/cast-
scoped native guard/parry/deflection path. Native attack/projectile clash rules
still decide what can be blocked. Ground versions keep Riku item-use pose 9.
Sora fallback casts/Guard/ledge/Glide poses and matching KH2 spell effects
remain. Native KH1 costs, healing, damage, levels and ability gates remain.
Gravity/Stop/Aero keep native effects, as no direct Sora KH2 counterpart was
selected. The existing dual_b_spell_fx option controls matching effect swaps.

All other six styles remain, including confirmed Glide attachment/colors,
Dual A's actual Superglide attack finisher, Dual B/Single B Quick Run and Guard,
Fire recovery, Wisdom shots and playable dual Roxas. This update adds no gauge,
model/costume change, extra ability/command, fixed weapon or stat bonus.
Only Dual A/B/C duplicate the currently equipped weapon; Single C has one.

FIRST TEST
1. Confirm SINGLE C COMBO MAP shows ground_ready=true and air_ready=true.
   Equip Style: Single C. Check ground 152 -> 151 -> Vicinity Break.
2. Check air Sora first hit -> Horizontal Slash -> Riku 182, then normal fall.
   Watch the transition into 182 and whether its shortened ending fixes the drop.
3. Tap Triangle standing and airborne: no custom 195/194 action should start.
4. Check aerial 193 casts/parries and normal grounded item casts still work.
5. If something fails, return the full fresh kh1-dual-wield.log from startup.
   Look for SINGLE C COMBO MAP, trimmed_tail=10, binding source labels and any
   UNAVAILABLE message. Include SINGLE C SORA SOURCE and SINGLE C LANE
   UNAVAILABLE lines if either readiness flag is false. The map includes source IDs.

IDs (exclusive, 0 AP): Dual A 126, Dual B 125, Single A 124, Single B 123,
Anti 122, Dual C 121, Single C 120. Unequipping restores native behavior.
INI defaults: dual_b_spell_fx=on, idle_speed=0.75, offhand_only_test=off,
remove_dual_wield=off. DLL/INI changes require a full game restart.
To remove our entries, set remove_dual_wield on; launch/load/save with v36;
close; disable the mod and Build again.

VALIDATION AND LIMITS
510 tests pass across 31 suites (161 style tests). Windows x64 release build,
four exports/eight imports, 103 source/preservation checks, 11 native anchors
and seven protected model metadata checks pass. Both test and Windows builds
use RUSTFLAGS=-C codegen-units=1 for this local toolchain. Package checks cover
ZIP CRC, independent extraction, every entry hash and saved-copy bytes/identity.

New fixtures cover valid Magic/body-based named strikes, missing-lane isolation,
all-failed atomicity, invalid/heal geometry rejection and qualified-alias-only
body contacts. The valid-Magic fixture failed on v35 before the fix.
Synthetic fixtures also exercise source selection, distinct Riku/Sora rigs and
weapon pose identity, full root/contact preservation except the requested
182 tail, native combo modifiers, finite/no-input termination and rejection
of missing/invalid source data before output mutation. The measured five-hit
148-frame fixture ends at 138 without resampling or losing any hit.

No actual v36 game/GPU test or installed animation playback was run here.
Live visual transitions and the exact tail cut need your fresh-process test.
The v35 aerial guard/contact/cast/effect runtime is unchanged. Source patch
(36 derivative commits), pinned upstream, credits/licences and validation
receipts are included. Rules/confidence: docs/combat-model.md Stage 374.
No game executable, extracted asset, recording or disassembly ships.
