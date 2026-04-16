from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends

from src.data.seed import characters
from src.models.character import Character
from src.services import characters_service

route = APIRouter(
    prefix="/characters",
    tags=["characters"],
    responses={404: {"description": "Not found"}},
)

def get_characters() -> list[Character]:
    return characters

@route.get(
    "/all",
    status_code=status.HTTP_200_OK,
    response_model=list[Character],
)
def get_all(data: Annotated[list[Character], Depends(get_characters)]) -> list[Character]:
    return characters_service.get_all_characters(
        data=data,
    )

@route.get(
    "/{id_character}",
    status_code=status.HTTP_200_OK,
    response_model=Character,
)
def get_by_id(
    id_character: int,
    data: Annotated[list[Character], Depends(get_characters)]
) -> Character:
    try:
        return characters_service.get_character_by_id(
            id_character=id_character,
            data=data,
        )
    except IndexError as exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exception),
        ) from exception