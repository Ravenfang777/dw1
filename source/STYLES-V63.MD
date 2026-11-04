# Styles v63 / s402: spent AP and Ventus source preparation

## Result

Passives and Limits show `AP Used <spent> / <maximum>` in the lower information
area. Both use Sora's current native AP budget; Limits has no separate budget
or entries yet. Equipping or removing a normal passive updates the display on
the same draw. Numbered zero-AP abilities and stances do not consume AP.
Stance and Outfits keep their previous presentation without this AP display.

Spent AP is maximum minus native available AP. Available AP at or above the
maximum yields zero spent, and the original native query clamps an exhausted
or overspent budget to zero available. This avoids unsigned underflow. Native
cost checks, direct Sora selection, scrolling and save commits are unchanged.

All eleven existing stances, all51 numbered test slots, seven built-ins and the
requested partner-ability removal remain. Both generated animation payloads
and E/F action controllers are unchanged from v62.

## Ventus Type G: source dependency

Type G is not playable or listed in this build. The original Ventus model and
animation banks were not present in the received source archives or current
project files. The existing Aqua and Terra rigs cannot establish Ventus's
animation mappings, body transforms or contact timing. No other moveset is
relabeled as Ventus, and no numbered ability ID is repurposed in v63.

The package includes `Ventus_Source_Locator/RUN_ME.cmd`. Run it on Windows and
select the broad extracted BBS data folder, including both `arc` and `chara`,
then return the generated `Ventus_Source_Capture_....zip`. Selecting only
`pc_ven` misses the shared main bank and standard model.

The read-only collector copies the standard `p01ex00.pmo`, `p01base.arc`,
`p01ex_*.arc` and `xaa*ve.arc`/`xaa*vx.arc` families, and can discover other
archives through internal non-event p01ex/p01base PAM member names. It includes
relative paths, header inventory, copied-file hashes and read/size-limit notes.
No bone count from Aqua or Terra is imposed on Ventus. Original files are not
modified, no upload occurs and old capture folders are skipped. Copies are
limited to40MiB per source and200MiB total; skipped candidates are listed.

Once returned, the actual skeleton and motion channels must be inspected,
retargeted onto Sora and matched to native KH1 action/event timing before Type G
can be added. The existing7-bit ID limit also requires promoting a numbered
placeholder into the stance catalogue with explicit settings migration.

## Sources and confidence

- Primary behavior source: the user's current request for spent/max AP in
  Passives and Limits and Ventus as Type G.
- AP source: delivered v62's native cost/free-AP integration and the supplied
  Steam Global executable. Free AP uses0x2e8660 for member0; the root menu's
  existing stat cache provides maximum AP at0x2e942c4. These helpers and their
  admission remain unchanged. See styles-v62.md for the cache producer.
- Drawing uses the same native glyph-only helper0x2ebcd0 as the previous AP
  budget. A single shared formatter serves both categories, at x159/y366,
  font12. It does not add another framed panel or alter the row AP boxes.
- Ventus source names are grounded in the user's BBS_File_List.txt from the
  earlier Aqua capture: the p01ex00 model, p01base archive, p01ex archives in
  shared pc and pc_ven, and ve/vx command banks. Filename evidence is a source
  selection lead, not proof of an individual animation's action.
- The collector derives from the previously successful Aqua collector's
  bounded ARC/PAM metadata reader. Its new identity filters do not assume a
  Ventus bone count. The new script has not run on a Windows host here.

Confidence is high for offline AP query/render behavior. Actual GPU placement,
Windows startup and gameplay still require the user's game test. Ventus motion
conversion is blocked on the returned source; no playable Type G is claimed.

## Validation

631 Rust tests pass across30 nonempty suites. Windows x64 release builds with
the existing4 exports and8 imported DLLs. All139 final-PE adapter checks pass:
92 F/menu/ability checks and47 E regressions.

New checks exercise the actual final PE formatter/controller using native AP
queries: zero spending,3/30 then5/30 after toggles, unchanged spending for a
numeric ability, matching Limits totals, removal back to0/30, an exhausted
3/3 budget and0/0. They confirm that Stance and Outfits omit the budget.
Existing insufficient-AP rejection, numeric flags, full lists, partner bounds,
native paging and both combat adapters continue to pass.

The harness substitutes rendering submission, Windows APIs and shared Rust
dispatch. It does not run the game or the new PowerShell collector. Those
limits are separate from the passed final-PE native helper execution checks.
