# Styles v73 / s412: nine Overdrives, hand follow and footsteps

## Catalogue and future-effect descriptions

Replace the five test rows with nine mutually exclusive, zero-AP visual
Overdrives. Show them in the user's order using the existing eight-row native
viewport/scrollbar. Each row has matching Drain/value boxes with measured
centering, and the footer has the exact requested future-effect description.

| Name | Color | RGB hex | Drain | Future-effect description |
| --- | --- | --- | --- | --- |
| Control | Dark Blue | #00008B |5| Doubles the range of all magic |
| Will | Purple | #800080 |3| Doubles all magic damage/healing done |
| Talent | Neon Pink | #FF10F0 |5| No MP Cost |
| Might | Deep Red | #8B0000 |3| Doubles all physical damage done |
| Vigor | Burnt Orange | #CC5500 |5| Increases speed by 10% |
| Resistance | Yellow | #FFFF00 |3| Halves all damage taken |
| Immunity | Forest Green | #228B22 |5| Invincibility |
| Prowess | Pale White | #F5F5FF |10| Doubles all damage done, No MP cost, Invincibility |
| Spite | Gray Black | #202020 |1| Heals 1 HP upon dealing damage to an enemy |

These are descriptions of intended future functions. This version does not
implement their buffs, healing, damage modifiers, resource drain, invincibility
or free magic. Drain remains metadata. Selection remains independent of Stance
and native ability slots, and active-row confirmation turns it off. Customize,
Appearance and Passives AP behavior stay as in v72; no Overdrive AP Used footer.

Exact hex shades are implementation choices for the user's color names. The
requested order/names/Drain/help are authoritative; all shades are configurable.
Add percent/comma glyph encoding for the exact Vigor/Prowess descriptions.
Sources: user request and existing native menu/description/scroll helpers.
Confidence high for catalogue/state/layout policy; final glyph appearance and
the chosen shade/intensity remain live visual checks.

## Saved choices and color upgrade

Retain old selection IDs to avoid reinterpreting existing settings: Might1
(former Power), Will2, Resistance3, Prowess4 (former Brilliance), Spite5 (former
Rage). New IDs are Control6, Talent7, Vigor8, Immunity9. Display order maps to
IDs6/2/7/1/8/3/9/4/5, rather than assuming ID equals row plus one.

The old settings file can contain generated blue Will/white Brilliance defaults.
Without a migration those would override the user's newly requested palette.
palette_version2 applies the requested nine-color set on startup for an older
file; the next selection save writes version2 and all nine canonical colors.
It retains the selected ID and unrelated keys/comments. This deliberately
replaces old palette fields once. After that, custom version2 colors persist
through selection changes; explicit current keys override old name aliases.

Canonical keys are control_color, will_color, talent_color, might_color,
vigor_color, resistance_color, immunity_color, prowess_color, spite_color.
Version2 also accepts strength_color/power_color as Might, brilliance_color
as Prowess and rage_color as Spite aliases. Restart after manual color edits.
Spite's near-black tint uses alpha/luminance masks so it remains a dark effect
instead of an almost invisible additive glow. Saturated dark blue/red retain
the normal colored additive highlights. Existing textures remain unchanged.

Sources: user palette change plus current persistent settings/read/write path.
Confidence high for migration, preserved identity and exact configured values.

## Hand follow during quick movement

The received28.54-second video shows glows tracking at rest and separating
slightly during running/rapid air movement. v72 places roots during the physics
effect tick, before the actual draw. The witnessed body pose can update after
that, leaving bound glows behind the hand until the next tick.

For Overdrive clones only, re-read the latest exact-binding witnessed pose at
draw time and refresh visible continuously bound roots immediately before
building their triangles. Preserve the existing base-rig wrist/palm alignment
and anchored actor placement. If no fresh pose is available, omit that owned
draw rather than invent an origin. Do not read phase-ambiguous raw skin palettes.

Effects::refresh_bindings changes bound placement only: it never ticks the
effect, advances particles/RNG, changes fade/alpha or consumes pending advances.
It ignores detached, bind-until-start, camera-space and script-anchored effects.
World-space particle/trail history remains authored; the wind is retained.
The helper is opt-in and only this Overdrive draw route calls it.

Sources: received video, effect tick/draw order, existing witnessed pose path
and particle root/binding code. Confidence high for clock/history isolation
and current-draw root refresh; moderate for the visual diagnosis. Actual hand
tracking through every fast transition still needs game/GPU verification.

## Footsteps

The user's follow-up requests all footstep sounds removed because attacking
also produces a step. Install the existing checked native material-step entry
(Epic RVA2939B0, Steam295B40) and suppress it for all actors/kinds while the
mod is active. The supplied Steam executable matches its full10-byte prologue.
This removes walking/running and the stop/jump/landing material-step sounds
that share that routine. It does not hook the similarly named293C70 push/
contact routine or the general audio, weapon, impact, voice or music players.

Legacy imported walk-step calls use the same mute instead of bypassing it
through the original pointer. Also reject known imported walking/running
sound IDs300/301/302/503032 at the existing sound-event boundary. Retain jump/
dodge, weapon, magic and impact IDs. Removal mode routes the native routine
and imported sound dispatch normally again.

Sources: user follow-up; docs/kh2-sound.md's prior executable/motion analysis;
the existing build-mapped address/signature and current supplied executable.
Confidence high for checked entry and identified sound-event scope; complete
audible results and any sounds introduced by another mod remain live checks.

## Validation and retained scope

660 Rust tests across30 nonempty suites,123 shared final-PE checks and49 E
final-PE checks pass. The Windows x64 release retains4 exports/8 imported DLLs.

Rust checks cover all stable IDs/colors, palette upgrade/custom settings,
near-black drawing, exact source filtering, draw-time translation with no
time/RNG/alpha advance and detached/script-anchor preservation. Native PE
checks cover all nine names/Drain/help, comma/percent text output, exclusive
selection/persistence without save/AP writes, centered metadata and real native
scrolling to Spite and wrapping back. Existing E/F/G and numbered tests remain.

Both private generated animation headers remain byte exact to v72. No combat
controller, animation, damage/contact, movement or ability-slot behavior is
changed. Delivery includes exact counts, Windows x64 export/import checks,
the footstep-entry witness, full73-commit source reconstruction and file hashes.
No Windows loader, game/GPU or native audio session was executed here. The PE
harness uses Win64 ABI/API mocks; it does not execute Rust startup/rendering.
