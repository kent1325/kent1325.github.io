from pathlib import Path
import yaml
from pydantic import BaseModel, ConfigDict, field_validator
from typing import Any


class ProfileLinks(BaseModel):
    model_config = ConfigDict(extra="forbid")

    linkedin: str
    github: str

    @field_validator("github")
    @classmethod
    def github_must_be_valid(cls, value: str) -> str:
        value = value.strip()
        rule: str = "https://github.com/"
        if not value.startswith(rule):
            raise ValueError(f"The 'github' profile field must start with {rule} but was '{value}'")
        return value

    @field_validator("linkedin")
    @classmethod
    def linkedin_must_be_valid(cls, value: str) -> str:
        value = value.strip()
        rule: str = "https://www.linkedin.com/in/"
        if not value.startswith(rule):
            raise ValueError(
                f"The 'linkedin' profile field must start with {rule} but was '{value}'"
            )
        return value


class Profile(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    avatar: str
    hero_lines: list[str]
    links: ProfileLinks

    @field_validator("name")
    @classmethod
    def name_must_exist(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("The 'name' profile field must not be empty")
        return value

    @field_validator("avatar")
    @classmethod
    def avatar_must_be_asset_path(cls, value: str) -> str:
        value = value.strip()
        rule: str = "/assets/"
        if not value.startswith(rule):
            raise ValueError(f"The 'avatar' profile field must start with {rule} but was '{value}'")
        if ".." in value:
            raise ValueError("avatar must not contain '..'")
        return value

    @field_validator("hero_lines")
    @classmethod
    def hero_lines_must_be_valid(cls, value: list[str]) -> list[str]:
        value_cleaned = [line.strip() for line in value]
        if not value_cleaned:
            raise ValueError("The 'hero_lines' profile field must contain at least one item")
        for index, line in enumerate(value_cleaned):
            if not line:
                raise ValueError(f"The 'hero_lines[{index}]' must not be empty")
        return value_cleaned


def load_profile(root_path: Path) -> Profile:
    yaml_file_path: Path = root_path / "content" / "profile.yaml"
    raw_profile: dict[str, Any]
    if not yaml_file_path.is_file():
        raise FileNotFoundError(f"YAML file not found: {yaml_file_path}")

    with yaml_file_path.open("r", encoding="utf-8") as f:
        raw_profile = yaml.safe_load(f)

    if raw_profile is None:
        raise ValueError(f"YAML file is empty: {yaml_file_path}")

    if not isinstance(raw_profile, dict):
        raise ValueError(f"YAML root must be a mapping/object: {yaml_file_path}")

    profile: Profile = Profile.model_validate(raw_profile)
    _validate_avatar_exists(root_path, profile.avatar)
    return profile


def _validate_avatar_exists(root_path: Path, avatar_path: str) -> None:
    path: Path = root_path / avatar_path.removeprefix("/")
    if not path.is_file():
        raise FileNotFoundError(
            f"Avatar file not found: {path} from profile avatar path: {avatar_path}"
        )
