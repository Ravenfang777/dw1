# Keyblade visual effects: candidates and current readiness

This historical v74 inventory helped choose candidates. Styles v75 adds the KH2
preview selector in Passives66..104; see styles-v75.md for current playback. Effect IDs belong to their own package. Use visual-only
hosts for previews without starting their attacks/damage/command scripts.

## KH1

| Candidate | Source / identification | Readiness |
| --- | --- | --- |
| Native blade swing trail | Current weapon's native trail/effect data; existing swing_fx/offhand route | Existing native visual path; no new format conversion |
| Hit/guard/wall sparks | Attack/weapon effect table at weapon object+0x18, kind/effect-bit lookup and native spark routine | Existing traced contact route; IDs depend on weapon/contact kind |

Sources: docs/kh1-clash.md, docs/kh1-weapon-second.md and existing swing/contact
code. Confidence high for native routes. This inspection adds no native effect
spawner and does not change contacts.

## KH2

| Candidate | Package | Elements | Notes |
| --- | --- | --- | --- |
| Weapon appearance/disappearance-style flash | obj/W_EX010.a.us |0| Existing weapon-flash renderer; blade bone2,13 effect ticks and turning glint. Original game caller not traced. |
| Last Arcanum blade glow | obj/P_EX100_KH1F.a.us |35/36| Weapon root/tip glow. Some lightning programs in36 remain unsupported; preview is partial. |
| Strike Raid spinning-blade ribbon | obj/P_EX100_KH1F.a.us |32| Existing script-bound blade trail; preview particle independently of the throw. |
| Valor finisher weapon bursts | obj/P_EX100_BTLF.a.us |13/14| Mapped weapon-point elements; attach to the current blade for preview. |
| Final Form weapon-point bursts | obj/P_EX100_ULTF.a.us |20,42..47,101/102| Mapped right/left anchors; earlier user log lacked this form's effect archive. Check runtime availability. |
| Sora attack flashes/swirls | obj/P_EX100.a.us |30/31/32,33/34,35..38| Guard Break, Finishing Leap and Aerial Finish families; preview without the attack. |

The KH2 interpreter already reads these formats and has weapon-root/tip paths.
Archives load from the user's installed KH2 resources; complete weapon/form
archives are not in the local captures inspected here. Missing archives and
skipped programs must be reported rather than assigned an invented visual.
Sources: win/kh2fx.rs weapon_vanish/form_bone; docs/kh2-effects.md sections12.3/
12.4 and docs/drive-model.md's limit trace. Confidence high for mappings/code
paths; final appearance, attachment/scale and partial programs need game tests.

## BBS: actual received sources

Read-only inspection of 184 distinct ARC files found one embedded FEP, one EAD
and two AAC files; there are also 12 distinct loose Aqua EADs. Most captured
resources are animations/models.

| Resource | Evidence | Limitation |
| --- | --- | --- |
| EX_C_AQA_KEY0_0 | Literal reference in p02ex00001a.ead, p02ex00018a.ead and p02ex20204a.ead | Aqua Keyblade effect candidate; matching particle payload and visual role unverified. |
| d_dp_407.fep | arc/etc/dp06TU003.arc;56192 bytes; header reports4 effect records,6 textures,10 models; string C_CHR_AQA0_0 | Scene/character candidate, not confirmed as a weapon effect; no FEP playback in this mod. |
| x30ex_000.ead | arc/pc/xcs14ve.arc | Attachment data, not standalone particles. |

PMO/PAM were enough for movesets, but a BBS particle preview needs matching
FEP and attachment resources plus a decoder/renderer or validated conversion.
Received HD EADs have EAD magic; OpenKH documents a BDD header, so do not apply
that layout blindly. No BBS effect index/appearance is claimed from names.
OpenKH identifies FEP as particle data, EAD as object/weapon attachment data,
and ABC as collision/effect-reference data. There is no demonstrated drop-in
FEP-to-KH1/PAX route here.

Primary sources:

- [BBS file types](https://openkh.dev/bbs/file-type.html)
- [FEP](https://openkh.dev/bbs/file/type/fep.html)
- [EAD](https://openkh.dev/bbs/file/type/ead.html)
- [ABC](https://openkh.dev/bbs/file/type/abc.html)
- [ARC](https://openkh.dev/bbs/file/type/arc.html)

Confidence high for local membership/names/headers; provisional for unrendered
roles. Delivery includes metadata only, not copied BBS payloads.

## First demo group

Start with KH1 trails/sparks, KH2 W_EX010 flash0 and Limit Form glow35 plus the
supported portion of36: a trail, short flash and sustained blade glow through
existing visual paths. Add Strike Raid32 after checking attachment. BBS remains
a separate resource/renderer investigation. This order reflects implementation
readiness, not a live comparison of effects on the user's PC.
