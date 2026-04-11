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
        # 1. Generamos todos los números
        total_cells = self.rows * self.columns
        numbers = [n if n != 16 else None for n in range(1, total_cells + 1)]                
        random.shuffle(numbers)
        self.idx_empty_cell = numbers.index(None)
        
        # 3. Repartimos en la matriz usando "slicing" o un iterador
        it = iter(numbers)
        self.structure = [
            [Cell(value=next(it)) for _ in range(self.columns)]
            for _ in range(self.rows)
        ]
            

  def select_cell(self, cell : Cell) -> None:
    self.selected_cell = cell
    
  def print(self):
    if not self.structure:
        return

    # Configuramos el ancho de cada celda según el número más grande
    # (2 espacios para números de hasta 99, 3 para hasta 999, etc.)
    cell_width = len(str(self.rows * self.columns)) + 1
    
    # Línea decorativa superior
    line = "+" + ("-" * (self.columns * (cell_width + 1) + 1)) + "+"
    print(line)

    for row in self.structure:
        print("|", end=" ")
        for cell in row:
            if cell.value is None:
                # Usamos un color o un símbolo vacío (ANSI escape para Cyan)
                print(f"\033[96m{'X':>{cell_width}}\033[0m", end=" ")
            else:
                # Alineamos a la derecha para que el 9 y el 10 queden parejos
                print(f"{cell.value:>{cell_width}}", end=" ")
        print("|")

    print(line)
        
      