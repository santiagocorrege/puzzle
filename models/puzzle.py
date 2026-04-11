from typing import Any
from pydantic import BaseModel
from models.cell import Cell
import random

class Puzzle(BaseModel):
  rows : int
  columns: int
  structure : list[list[Cell]] | None = None
  selected_cell : Cell | None = None
  idx_empty_cell : int | None = None
  
  def model_post_init(self, context: Any) -> None:
    if self.structure is None:
        
        total_cells = self.rows * self.columns
        numbers = [n if n != 16 else None for n in range(1, total_cells + 1)]                
        random.shuffle(numbers)
        self.idx_empty_cell = numbers.index(None)
        
        
        it = iter(numbers)
        self.structure = [
            [Cell(value=next(it)) for _ in range(self.columns)]
            for _ in range(self.rows)
        ]
            

  def select_cell(self, cell : Cell) -> None:
    self.selected_cell = cell
        
      