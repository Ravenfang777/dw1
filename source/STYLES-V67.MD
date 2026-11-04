# Styles v67 / s406: Type G dispatch and switching recovery

## Observed failures

The supplied s405 log confirms Type G profile2 applied in Olympus and its
native blade contacts ran. Each330/410 start then ended with zero movement
ticks. Later, a fresh G entry rejected request71 (physical Olympus37) at
admission stage24: the flags stream for held Glide75. The video shows default
Glide and normal attacks after attempts to change stances. The user confirms
the numbered Passives worked and that unequipping G could block other styles.

Source inspection identifies two separate defects, with high confidence:

- The actual Rust regular-Glide and Superglide callbacks dispatched the C
  suppression checks only for Terra. Main G reached the same native C air
  controller, but its native constructors could immediately replace the action.
- Optional Glide75 belonged to the shared all-record admission transaction.
  Failure there blocked all G body writes. A failed initial entry, despite
  changing no bodies, still required that same bank to admit before exit.

The attachment does not reveal what changed/unmapped the Glide flags stream.
v67 does not assume that an unknown stream is safe to overwrite or relax the
admission of combat/body records to accommodate it.

## Changes

Both main native-air styles (F and G) now use the same actual Rust constructor
gates. Superglide is suppressed for their replacement; ordinary Glide is
suppressed only during a finite action. Numbered previews retain native input.

The37 reversible body records, all37 profiles and four G variants retain their
exact v66 payloads. Held Glide038 is evaluated from a separate immutable copy
of the already converted native clip using the existing authored-pose reader.
It is scoped to main G, an admitted body binding, current regular request71,
native state21 and the exact field Sora instance. Its native clock supplies
the loop phase. Only the displayed matrices change; native Glide streams,
handles, headers, events, entry/exit and travel are not patched. A foreign or
unavailable live Glide record cannot block the37 body records or their exit.
Leaving Glide/G stops the visual without a data-restoration dependency.

A separate ownership bit records successful body publication. Entry rejection
does not acquire ownership. Exit after such a rejection releases the style
without attempting to restore data that was never admitted or changed. A
successfully applied profile still requires complete verified restoration at
idle before another style owns the body; the corruption safeguards remain.

The existing final model-queue hook refreshes reverse grip for the exact field
instance immediately before native submission. The post-motion and skeleton
passes remain. Palm101 and grip280 offsets now always come from immutable bind
geometry: unskinned live helpers can contain stale affine matrices, which a
finite/determinant test alone cannot identify. The skinned wrist100 supplies
the current attachment; children281..292 retain native local motion with the
existing bind fallback. Grip writes stay in280..292 and remain idempotent.
This addresses a plausible remaining flicker path; its appearance is not yet
confirmed live. No new hook or replacement game handle is allocated.

All requested v66 mappings, cast recovery, contact windows/damage, per-airtime
budgets, shortcut exclusion, working Ventus/Dark Riku previews and Customize
menus remain. No new donor scripts, abilities, inventory or save flags are added.
Bounded cancellation diagnostics record reason, state, request and queued action
if an air action is interrupted, rather than reporting only zero movement.

## Validation

- 647 Rust tests in30 nonempty suites pass. One new test compiles and executes
 the actual Windows Rust Glide callbacks with inert platform dependencies,
 covering all15 runtime style codes, both constructors, suppression and release.
 It detects the missing G branch that the isolated C PE tests could not cover.
 New grip tests cover stale but affine palm/grip helpers and fixed ownership.
- 115 shared-adapter and48 Aqua final-PE checks pass. New cases reproduce changed
 live Glide flags in both banks, exercise G entry/restore/F entry/restore, and
 prove an unrelated corrupted failed entry cannot hold native control hostage.
 The embedded038 container matches the converted source byte for byte.
- 131 immutable038 samples on293 bones agree with the independent Python
 evaluator: maximum position difference0.000063 and basis difference0.000001.
- Every shared profile/variant part matches v66; all35 Ventus test profiles and
 E's private payload remain exact. Dark Riku test implementation is unchanged.
- Windows x64 release builds. Delivery checks verify4 public exports,8 imported
 DLLs, source reconstruction, archive CRC and file hashes.

The PE harness replaces Windows APIs and rendering. The Rust callback regression
executes only constructor routing; it does not run the full live actor pipeline.
No Windows/game/GPU session was executed here. Check G combos, both finite air
actions, held038, grip transitions and G→unequipped→other stance in game. Added
contact alignment and combat feel retain their previous provisional live status.
