DARK RIKU TO SORA BODY MAP -- v50

The source solver, geometric hip frame, body map and secondary/skin guards are
unchanged. This fixes combo admission only: v49 treated native requestsC8..CE
as bank indices; the regular request table actually resolves them to98..104.

D resolves the requested basic bank record, verifies every existing current
header field, then requires exact current/requested record equality and the
native field/binding/lane/scene/script/hold gates. Nonbasic locomotion keeps
its known signature aliases. Other actions cannot borrow an old attack pose.
No global request decoder, signature map or native gameplay callback changes.

Ground bank98/100,99,101 -> source18,19,20. Air102,103,104 ->18,19,21.
Same native phase/clamp and actual source lengths. Working Single C/Riku jump
route, matching calibration, paired clock and raw-pose isolation are exact.
All native combo selection/ability/contact/damage and other style code remain.
Original boss contact windows are not imported by this animation adapter.

Apply source/NineStyles_v50.patch to the pinned upstream with git am.
validation/log_findings_v50.json contains plain extracted observations only;
the raw log is not distributed. Current scope/test/PE receipts cover this fix.
Source/geometry receipts named v44/v45/v47/v49 remain labelled history. No new
v50 native-CPU, GPU/skin or boss contact parity is claimed. Rules/confidence:
docs/combat-model.md Stage389; exact request/bank roles in SINGLE_D_COMBO_MAP.txt.
