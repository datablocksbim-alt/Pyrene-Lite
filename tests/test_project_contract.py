from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ProjectContractTests(unittest.TestCase):
    def test_godot_project_and_main_scene_exist(self) -> None:
        self.assertTrue((ROOT / "project.godot").is_file())
        self.assertTrue((ROOT / "scenes" / "main.tscn").is_file())

    def test_main_scene_is_registered(self) -> None:
        project = (ROOT / "project.godot").read_text(encoding="utf-8")
        self.assertIn('run/main_scene="res://scenes/main.tscn"', project)

    def test_retired_project_is_not_a_runtime_dependency(self) -> None:
        text_files = [
            ROOT / "project.godot",
            ROOT / "scenes" / "main.tscn",
            ROOT / "scripts" / "main.gd",
        ]
        for path in text_files:
            contents = path.read_text(encoding="utf-8").lower()
            self.assertNotIn("pyrene mini", contents, path)


if __name__ == "__main__":
    unittest.main()

