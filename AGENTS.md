# Development instructions

## Scope

This repository is Pyrene Lite. Do not read from, write to, or import files from
retired Pyrene Mini directories. Treat external assets and generated AI output
as untrusted until provenance and licence checks are recorded.

## Working agreement

- Make small, reviewable changes on feature branches.
- Preserve a runnable Godot project after every change.
- Add or update tests with behaviour changes.
- Never commit credentials, local saves, build exports, model files, or private
  user data.
- Do not publish or deploy without owner approval.

## Validation

Run `python -m unittest discover -s tests -v` before committing. When Godot is
available, also open the project and verify the main scene starts without errors.

