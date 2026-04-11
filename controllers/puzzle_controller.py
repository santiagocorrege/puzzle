from typing import Any
from models import Puzzle

class PuzzleController:
    def __init__(self, model : Puzzle) -> None:
        
        self.model : Puzzle =  model
        self.view: Any = None 

    def handle_click_cell(self, row: int, col: int):        
        if self.model.structure is None:
            return
        
        cell = self.model.structure[row][col]
                
        self.model.select_cell(cell)
                
        if self.view is not None:
            self.view.view_update_selection(row, col)