from typing import Any
from models import Puzzle

class PuzzleController:
    def __init__(self, model : Puzzle) -> None:
        
        self.model : Puzzle =  model
        self.view: Any = None        

    def handle_click_cell(self, row: int, col: int):        
        if self.model.structure is None:
            return
        
        cell_tuple = self.model.select_cell(row, col)
                
        if cell_tuple is not None and self.view is not None:
            self.view.view_boton_selected(row, col)            
    

    def update_selection_movements(self):
        movements = self.model.get_available_movements()
        if movements is not None:
            self.view.view_selection_movements(movements)
    
        