from view import PuzzleView
from models import Puzzle
from controllers import PuzzleController
import flet as ft

def main(page: ft.Page):    
    puzzle_model = Puzzle(rows=4, columns=4)    
    controller = PuzzleController(model=puzzle_model)    
    app_view = PuzzleView(page, controller)

if __name__ == "__main__":
    ft.app(target=main)