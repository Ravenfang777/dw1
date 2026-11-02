# Single E / Aqua v21 — Styles v53

Single E is the main Aqua v21 profile under the existing Styles ability system.
Its ID is117 and its menu label is `Style: Single E`; AP cost is0. It starts
unequipped and switches exclusively with the existing nine entries. Their IDs
and style codes remain unchanged. Menu order is Singles A–E, Duals A–D, Anti.
The first65 native ability records are copied unchanged; a full save ability
list is never evicted to make space.

## Behavior

| Action | Aqua source / behavior |
| --- | --- |
| Ground chain | 300 /301 /366; second ends at source30, finisher starts15 |
| Air chain | 305 /407 /353 |
| Dodge in air | 504; fresh Circle/Jump tap; once per airtime |
| Dodge timing / travel | rate1.5;26 native ticks,546 horizontal units and29.25 lift at full travel |
| Jump / High Jump | native launch height multiplied1.25; arc time multiplied sqrt1.25 |
| Guard | 400, forward/reverse at source30fps; body capsule radius50; all-angle native deflection and12-tick grace |
| Glide | ordinary Glide replaced by the finite dodge; native Superglide usable |
| Magic | main v21 split ground/air poses; Blizzard Fire-body visual with native Blizzard events; Stop/Aero use Gravity poses |
| Effect origin | native keyblade tip |
| Other body poses | same main v21 fitted idle, movement, item and fall records |
| Damage / knockback | original KH1 Sora; KH2 reaction sources were not available |

The native KH1 controller owns combo selection, native ability priority,
collision, spell execution, item use and native hit feedback. Single E uses
one equipped weapon. It never enters the KH2 attack controller or passive
KH2 pose overlay, and does not duplicate an offhand weapon. Only main Aqua is
included; the standalone numbered testing abilities are not registered.

## Shared hooks and switching

The Rust style gate is the only ability-table writer. Its existing native
control and Guard-row callbacks dispatch to the Aqua adapter for Single E.
Its normal/Superglide constructors remain the sole hooks at those entries.
The adapter adds checked, independent native fall displacement, actor motion,
Guard angle/pool and jump-launch hooks. A mismatched required hook disables
Single E body publication; other styles retain their existing route.

Before entering, retire the old KH2 controller. While leaving, keep the native
Aqua lane until all mapped body records and the actor's cast-request pointer
are verified/restored at idle. Finishing an attack, landing and standing still
allows a pending switch to complete. The adapter's frame work is deduplicated
by the shared physics epoch across Panacea and native physics callbacks.
A fresh menu choice may be handled within the same epoch.

Normal and Olympus banks require37 and36 verified mapped records respectively
before any body write. Headers, capacities, encoded pointers and event
payloads retain native ownership. Native Superglide and damage records remain
original. A spent dodge budget persists through ability toggles, cache loss,
completion and Superglide; landing rearms it. Movement enters KH1 collision
through native displacement; no teleport/position writes are added.

## Rebuild

The pinned upstream is PM2CRAZY/KH2-Combat-in-KH1 at
4adb946b642f6b9bd84f83d12ec16944e0638b8b. Apply `TenStyles_v53.patch` with
`git am` on that checkout. The package includes the privately generated main
payload at `source/rebuild-inputs/aqua_data.h`; copy it to ignored
`local/single_e/aqua_data.h` in the checkout. Never add that header to Git.

Alternatively regenerate it from the Aqua v21 source tree:

```
python crates/kh1-hook/src/single_e/generate_data.py <aqua-v21-source> local/single_e
```

Use Rust with the x86_64-pc-windows-gnu target and MinGW GCC/binutils:

```
cargo test --workspace --exclude kh2-bevy --exclude kh2-combat-cli
cargo build -p kh1-hook --release --target x86_64-pc-windows-gnu
```

The release was built with `CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1`.
`SINGLE_E_CC`, `SINGLE_E_AR` and `SINGLE_E_DATA` optionally select the C compiler,
archiver and payload directory. No new Cargo dependency is required.
Rename `target/x86_64-pc-windows-gnu/release/dinput8.dll` to
`kh1-dual-wield.dll` for the supplied OpenKH mod manifest.

## Evidence and limits

Source: the user's Aqua v21 final package and Dual Wield v52 source patch;
Steam Global executable timestamp1721645006 and previously verified native
function anchors/record schemas. The v52 source tree reconstructed exactly to
e04af764002b7f760769174ae8dae110861f9bfa before changes. Confidence is high in
source/payload identity, policy isolation and offline native callback tests.
Only the new adapter is Steam-specific; older styles retain their Epic route.

All622 Rust tests in29 nonempty suites and46 focused PE checks pass.
The Windows x64 release retains4 exports and8 imported DLLs.
Validation executes the C adapter from the final combined Windows PE under
Win64 ABI/API mocks, including the real native event sampler, jump curve and
Glide constructors. Shared Rust dispatch is mocked there and checked through
Rust policy tests and source review. This is not a Windows loader or live
KH1 game test. In-game switching, Guard contacts, room transitions, animation
appearance and other mods still need the user's test. Do not enable the
standalone Aqua DLL alongside this integrated build.
