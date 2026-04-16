from src.models.character import Character
from src.repositories import characters_repository

def get_all_characters(data: list[Character]) -> list[Character]:
    return characters_repository.get_all_characters(
        data=data,
    )

def get_character_by_id(id_character: int, data: list[Character]) -> Character:
    return characters_repository.get_character_by_id(
        id_character=id_character,
        data=data,
    )
