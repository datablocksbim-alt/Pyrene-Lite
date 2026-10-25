# Architecture

Pyrene Lite begins as a small Godot 4 application with one executable project,
one main scene, and repository-level contract tests.

## Initial boundaries

- `scenes/` owns scene composition.
- `scripts/` owns runtime behaviour.
- `assets/` will contain reviewed, project-owned source assets.
- `tests/` owns automated repository and gameplay checks.
- `docs/` records product, architecture, provenance, and release decisions.

The project has no runtime dependency on Ground Space, local AI agents, Pyrene
Mini, private user data, or cloud services. Ground Space may assist development,
but generated proposals must pass normal review and validation.

## Next design decisions

Before adding gameplay, document:

1. the core player loop;
2. desktop and mobile platform targets;
3. save-data and accessibility requirements;
4. asset provenance and licensing;
5. the first playable acceptance test.

