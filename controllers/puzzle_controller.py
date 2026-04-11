from typing import Any  # <--- IMPORTANTE: Soluciona el error de "Any"
from models import Puzzle

class PuzzleController:
    def __init__(self, model : Puzzle) -> None:
        # No necesitas ConfigDict si no heredas de BaseModel
        self.model : Puzzle =  model
        self.view: Any = None 

    def handle_click_cell(self, row: int, col: int):
        # 1. Verificación de seguridad para Pylance
        if self.model.structure is None:
            return
        
        cell = self.model.structure[row][col]
                
        self.model.select_cell(cell)
                
        if self.view is not None:
            self.view.update_selection(row, col)