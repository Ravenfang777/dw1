KH1FM STYLES v68 / s407 - TYPE G GRIP, AIR TRAVEL AND TWO BLADE PASSES

INSTALL
Close KH1. Disable v67 and older main Styles packages. Import this ZIP into
OpenKH Mod Manager, enable v68, Build and launch with Panacea. Keep the existing
KH2FM resources/settings required by the other stances. Standalone Aqua/Terra
and full KH2 Combat DLLs remain disabled. Confirm s407 / STANCES v68 in
kh1-dual-wield.log. This native adapter targets the supplied Steam Global build.

REVERSE GRIP
Reverse grip is now stored in the converted G animations, including the main
profile, all35 Ventus previews, body variants and held Glide038. The native
sampler carries one consistent grip through converted pose transitions. Remove
the separate runtime weapon-matrix correction that used a different attachment.
Body poses, hilt position, bone lengths, native helpers and travel are preserved.
Unmapped native actions keep their native records.

AIR DASH AND DODGE
Square330 and airborne Circle410 move at2x v67 speed over1.5x its distance:
468 unobstructed native units, previously312. The duration is29.25 native ticks,
previously39. Animation playback is4/3 its previous rate to fit that duration.
410's total lift is43.875 units, previously29.25. Type F remains unchanged.

Initial stick direction/facing stays locked and native collision remains active.
Each action is once per actual airtime; landing resets it. Release the ground
jump before an airborne Circle tap. L1 shortcuts, casting, damage and scripts
cannot start an action. Ordinary held038 Glide is available after completion.

TWO CONTACTS
379 (ground2),411 (ground finisher) and482 (air finisher) now have separate first
and second blade-contact windows. Original native hits and fallback contacts
share successful-hit tracking, avoiding duplicates in the same pass. Failed
attempts can retry. Earlier retiming also collapsed some on/off windows; those
now keep positive width after the second swing. Damage/defenses stay native;
the actual blade must reach the target. First finisher contact flinches and
the second can use native finisher knockback.330 retains one contact per target.
The log labels pass1/pass2 and native witnesses for testing.

TYPE G MAPPING RETAINED
Ground combo:300,379,411. Air combo:305,306,482.
Ground and air item:395. Held ordinary Glide:038.
Ground Cure/Aero/Thunder/Stop:390. Air:508.
Ground Fire/Blizzard/Gravity:416. Air:417.
Source spans/durations are in VENTUS_ANIMATIONS.csv.

PASSIVES AND OTHER STANCES
Ventus66..100 retain their187 source-clip assignments and body curves; only the
grip changes. Dark Riku101..104 remain unchanged. Tests and stances stay mutually
exclusive. Other stance mappings, menus, normal AP, white AP Used/max and seven
slot-free built-ins remain. IDs and native48-byte capacity are unchanged.
As requested previously, non-Sora ability lists remain cleared; saving persists
that removal and uninstall does not reconstruct those partner abilities.

CHECK IN GAME
After leaving the menu, stand idle for a safe data handoff. Move between idle,
run, jump, fall and both combos to check the grip. Check both air actions and
two contacts on reachable enemies/objects. Then check G -> unequip -> another
stance, plus numbered preview switching.

647 Rust tests/30 nonempty suites and166 final-PE checks pass. These include the
actual Rust contact coordinator with mocked native dependencies and the actual
shared native motion hook.324 converted records/2268 poses preserve body/travel
and agree with rigid reverse-grip geometry. Source, hashes and validation are
included; see source/STYLES-V68.MD for scope and exact limitations.

No Windows/game/GPU session was run here. Live transition appearance, contact
alignment, finalized HP damage and combat feel still need your game check.

UNINSTALL
Set remove_dual_wield=on in kh1-dual-wield.ini; load/save using v68, close KH1,
disable the package and Build. The hidden stance token is removed. Built-in
normal entries restore where capacity permits without eviction (Sora entries
off, shared movement on). Partner ability lists stay removed; numbered flags
stop applying when the mod is removed.
