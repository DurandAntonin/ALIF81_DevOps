from pydantic import BaseModel, Field

class Character(BaseModel):
    id: int
    pseudo: str
    level: int = Field(ge=0)
    health: float = Field(ge=0)
    damage: float = Field(ge=0)
