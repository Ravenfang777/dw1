KH1FM NINE STYLES -- PROTOTYPE v52 (s391)

IMPLEMENTED FOR SINGLE D
- Guard animation: former second ground attack, main clip30/request232.
- Second ground hit: former ground finisher, main clip28/request230.
Guard keeps KH1's original ability selection, blocking objects and timing.
This changes the body animation; it does not add a damaging Guard attack.
The working Single C jump remains.

NEW FINISHER AND AIR COMBO: SOURCE INSPECTION PENDING
Only three weapon attacks are verified in the captured main1160 bank.
Other tempting clips include a confirmed clash-recoil response. Additional
attack requests in the shared script are absent from the captured main bank.
The separate second-fight1580 bank has41 inventory entries, but its source
poses have not yet been available for inspection here.

This build exports that extra source automatically. It does NOT claim a new
finisher/air chain. Interim ground29/28/28 repeats28 in slots two and three;
air remains29/30/28. Return the new ZIP so the remaining choices can be checked.
The extra bank's rig, AI, scripts, events and poses are not installed/executed.

INSTALL
1. Fully close KH1FM. Disable v51 and every older Dual Wield prototype.
2. Import THIS ZIP through OpenKH, enable only v52, then Build and Run.
   Panacea and installed KH2FM resources are required. F1 cannot reload a DLL.
   Keep the full KH2 Combat overhaul, old offhand/moveset Lua and duplicate
   Sora model mods disabled. Existing INI/save settings remain.
3. Confirm s391 / PROTOTYPE v52 in kh1-dual-wield.log beside the game EXE.

TEST AND RETURN
Equip Style: Single D and the native Guard ability. Stand still and use Guard;
it should show the former second attack and still block normally. Test ground
hits one/two, jump, normal interruptions and a map change. Native attack ability
replacements retain priority; unequip them only to isolate the basic combo.

Wait for SINGLE D EXTRA SOURCE CAPTURE COMPLETE in the log. No battle or
special ability is needed for capture. Send BOTH files from the game folder:
  kh1-dual-wield-dark-riku-extra.zip
  kh1-dual-wield.log
The ZIP contains original xa_ex_1580.mdls/mset and diagnostics. Do not install
or extract it; just return it. If a different extra ZIP already existed, use
the timestamped path named by the capture-complete line. There is no automatic
upload. If capture fails, return the log; main1160 gameplay remains independent.

EXPECTED DIAGNOSTICS
STYLE NATIVE GUARD WITNESS: original row0x3D, actual resolved motion.
SINGLE D GUARD ACTIVE: source30/frame/native phase; original blocking retained.
SINGLE D BASIC COMBO ACTIVE: second ground source28. Existing native request
C8..CE -> bank98..104 admission is retained. A raw Square press/request number
cannot authorize a Guard overlay; stale/foreign/header-mismatched states retire.

RETAINED SCOPE
KH1 owns combo progression/repeats/modifiers/ability priority, movement, contacts,
damage, hit timing and native feedback. No boss damage/contact/projectile events
are imported. Same D solver, body map, hip alignment, held fall and skin guards.
One equipped weapon. Other styles, Quick Run, glide/Superglide finishers and
confirmed2x Aerial Dodge routes remain. Nine exclusive0-AP style abilities;
no new ability grants, gauge, stats, outfit or party changes.

VALIDATION
599 tests/31 suites pass (174 style,16 body map,15 D policy). Windows x64
release passes with the existing4 exports/8 imports.31 scope checks protect
283 other tracked files and exact working jump/solver/controllers/contacts.
New tests cover the committed Guard witness and independent extra ZIP decoding,
binary payload preservation, CRC and parse-failure diagnostics. Additional
source bytes and live Guard/blocking/timing still require your returned test.
Historical solver/map metrics in validation remain historical. The52-commit
source patch, ZIP CRC/extraction and each file hash are checked before delivery.
Restart after DLL/INI changes. Removal: set remove_dual_wield on, launch/load/
save with v52, close, disable the mod and Build again.
