from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from src.models.character import Character
from src.server import app


@pytest.fixture
def character() -> Character:
    return Character(id=1, pseudo="TestCharacter", level=15, health=450.5, damage=75.2)

@pytest.fixture
def characters_mock() -> list[Character]:
    return [
        Character(id=1, pseudo="TestCharacter1", level=1, health=1.5, damage=1.2),
        Character(id=2, pseudo="TestCharacter2", level=2, health=2.5, damage=2.2)
    ]

client = TestClient(app)


class TestCharactersRoute:

    def test_get_all_characters(self, characters_mock: list[Character]):
        with patch(
            "src.services.characters_service.get_all_characters",
            return_value=characters_mock,
        ):
            response = client.get("/characters/all")

            assert response.status_code == 200

            expected_data = [character.model_dump(mode="json") for character in characters_mock]
            assert response.json() == expected_data

    def test_get_character_by_id_found(self, characters_mock: list[Character]):
        with patch(
            "src.services.characters_service.get_character_by_id",
            return_value=characters_mock[0],
        ):
            response = client.get("/characters/1")

            assert response.status_code == 200
            assert response.json() == characters_mock[0].model_dump(mode="json")

    def test_get_character_by_id_not_found(self, characters_mock: list[Character]):
        with patch(
            "src.services.characters_service.get_character_by_id",
            side_effect=IndexError("Character not found with id '-1'"),
        ):
            response = client.get("/characters/-1")

            assert response.status_code == 404