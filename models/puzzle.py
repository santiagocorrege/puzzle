from typing import Any
from pydantic import BaseModel
from models.cell import Cell
from models.events.select_events import EventSelectCell 
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
        self.update_available_movements()

    def select_cell(self, row: int, col: int) -> tuple[EventSelectCell, list[tuple[int, int]]] | None:
        if self.structure is not None:                
            if((row, col) in self.available_movements):
                new_selected_cell = self.structure[row][col]
                if self.selected_cell == new_selected_cell:
                    self.swap_cells(new_selected_cell)
                    return (EventSelectCell.SWAPPED_CELLS, [()])                                           
                else:
                    self.selected_cell = new_selected_cell                                                             
        return None        
         
    def swap_cells(self, new_selected_cell: Cell):        
        if self.selected_cell:
            self.selected_cell.value, new_selected_cell.value = new_selected_cell.value, self.selected_cell.value                    

    def update_available_movements(self):
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
        
        self.available_movements = lst_movements
        
    def get_available_movements(self):
        return self.available_movements