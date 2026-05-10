from pathlib import Path

from portfolio.content import load_profile


def test_load_profile_from_content() -> None:
    root_path = Path(__file__).resolve().parents[1]

    profile = load_profile(root_path)

    assert profile.name == "Kent Vugs Nielsen"
    assert profile.avatar == "/assets/images/profile-picture.jpg"
    assert profile.hero_lines
    assert profile.links.github.startswith("https://github.com/")
    assert profile.links.linkedin.startswith("https://www.linkedin.com/in/")
