from typing import Any
from pydantic import BaseModel
from models.cell import Cell
import random

class Puzzle(BaseModel):
    rows: int
    columns: int
    structure: list[list[Cell]] | None = None
    selected_cell: Cell | None = None
    empty_cell: tuple[int, int] | None = None
    # Es buena práctica inicializar esto como lista vacía para Pydantic
    available_movements: list[tuple[int, int]] = []

    def model_post_init(self, context: Any) -> None:
        if self.structure is None:
            total_cells = self.rows * self.columns
            numbers = [
                Cell(value=n) if n != total_cells else Cell(value=None) 
                for n in range(1, total_cells + 1)
            ]
            random.shuffle(numbers)
            
            for i, cell in enumerate(numbers):
                if cell.value is None:
                    self.empty_cell = (i // self.columns, i % self.columns)
                    break
                  
            self.structure = [
                numbers[i * self.columns : (i + 1) * self.columns]
                for i in range(self.rows)
            ]

    def select_cell(self, cell: Cell) -> None:        
        self.selected_cell = cell        
        self.available_movements = self.get_available_movements()

    def get_available_movements(self) -> list[tuple[int, int]]:
        lst_movements: list[tuple[int, int]] = []
                
        if self.empty_cell is not None:
            row, column = self.empty_cell
            
            if column > 0:
                lst_movements.append((row, column - 1))
            if column < self.columns - 1:
                lst_movements.append((row, column + 1))
            if row > 0:
                lst_movements.append((row - 1, column))
            if row < self.rows - 1:
                lst_movements.append((row + 1, column))
        
        return lst_movements