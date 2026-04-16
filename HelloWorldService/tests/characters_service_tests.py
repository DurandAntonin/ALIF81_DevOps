from unittest.mock import AsyncMock, patch

import pytest

from src.models.character import Character
from src.services.characters_service import get_all_characters, get_character_by_id


@pytest.fixture
def character() -> Character:
    return Character(id=1, pseudo="TestCharacter", level=15, health=450.5, damage=75.2)

@pytest.fixture
def characters_mock() -> list[Character]:
    return [
        Character(id=1, pseudo="TestCharacter1", level=1, health=1.5, damage=1.2),
        Character(id=2, pseudo="TestCharacter2", level=2, health=2.5, damage=2.2)
    ]


class TestCharactersService:

    def test_get_all_characters(self, characters_mock: list[Character]):
        with patch(
            "src.services.characters_service.get_all_characters",
            return_value=characters_mock,
        ):
            result = get_all_characters(characters_mock)

            assert len(result) == len(characters_mock)
            for i in range(len(result)):
                assert result[i].model_dump() == characters_mock[i].model_dump()

    def test_get_character_by_id_found(self, characters_mock: list[Character]):
        with patch(
            "src.services.characters_service.get_character_by_id",
            new_callable=AsyncMock,
            return_value=characters_mock[0],
        ):
            result = get_character_by_id(1, characters_mock)

            assert result.model_dump() == characters_mock[0].model_dump()

    def test_get_character_by_id_not_found(self, characters_mock: list[Character]):
        with patch(
            "src.services.characters_service.get_character_by_id",
            new_callable=AsyncMock,
        ):
            with pytest.raises(IndexError):
                get_character_by_id(-1, characters_mock)