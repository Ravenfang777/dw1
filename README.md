# KH1FM Styles v78 / s417

GitHub runtime package for OpenKH Mod Manager. The gameplay DLL is identical
to the full v78 release. This edition omits development/rebuild files and
historical validation folders so they cannot create deeply nested Windows paths.
The full v78 recovery archive remains separate.

## Updating your mod repository

1. Keep a backup of your existing repository outside its working folder.
2. Remove the old mod package's `validation` and `source` folders from the
   working folder. These optional development files are not used by Mod Manager.
   Keep your repository's `.git` folder and your own unrelated files.
3. Extract this ZIP's contents directly into the repository root. `mod.yml`
   and `kh1-dual-wield.dll` must sit together, not inside an extra subfolder.
   Include `.gitattributes` and `.gitignore`.
4. Commit the changes in GitHub Desktop and push normally.

The earlier failure was `Filename too long` inside repeatedly nested validation
history. LF/CRLF messages were warnings. This package uses shallow paths and
explicit LF text settings. If the repository itself has an unusually long
location, use a short working-folder path such as `C:/Mods/Styles`.

## Installing and testing

See `README_FIRST.txt` for requirements, installation, removal, and runtime
logs. Keep your existing KH2FM resource configuration. This package does not
overwrite your INI settings.

- Type G attacking air dash: Sonic Rave effect 27 and KH2 SE999027.
- Type F attacking air dash: Sonic Rave Finish effect 30 and KH2 SE999027.
- Overdrive activation: Infinity Tip Charge sound and one game second of
  the transformation animation before the aura begins.
- Sound auditions remain in Passives 66 through 110.

See `STYLES_V78.md`, `OVERDRIVES.txt`, and `SOUND_TESTS.csv` for details.
The retained validation applies to v78's unchanged DLL; this packaging fix has
not been tested in an actual Windows game session.
