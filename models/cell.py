
from pydantic import BaseModel

class Cell(BaseModel):
  value: int | None
  is_moveable: bool = False    