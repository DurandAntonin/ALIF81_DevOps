from src.models.character import Character


def get_all_characters(data: list[Character]) -> list[Character]:
    return data

def get_character_by_id(id_character: int, data: list[Character]) -> Character:
    for character in data:
        if character.id == id_character:
            return character

    raise IndexError(f"Character not found with id '{id_character}'")