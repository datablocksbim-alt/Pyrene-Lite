# Pyrene Lite

Pyrene Lite is the clean successor project for lightweight Pyrene development.
It starts independently and intentionally contains no Pyrene Mini source,
generated files, private saves, credentials, or imported legacy assets.

## Development

1. Install Godot 4.7 or a compatible Godot 4 release.
2. Open `project.godot` in the Godot editor.
3. Run the project with <kbd>F6</kbd> or <kbd>F5</kbd>.
4. Run the repository contract tests with:

   ```powershell
   python -m unittest discover -s tests -v
   ```

The first milestone should define the player experience and supported devices
before legacy concepts or assets are introduced.

## Repository policy

- Keep private credentials, saves, model data, and generated exports out of Git.
- Add dependencies deliberately and document their licences.
- Do not copy code or assets from Pyrene Mini without an explicit provenance and
  licence review.
- Use feature branches and keep `main` releasable.

No public software licence has been selected yet. Add one before distributing
source or builds.

