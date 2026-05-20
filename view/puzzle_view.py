import flet as ft
from view import constants as const

class PuzzleView:
    def __init__(self, page: ft.Page, controller):
        self.page = page
        self.controller = controller
        self.controller.view = self
                
        self.buttons = {} 
        self.selected_btn = None                
        self.config_view()
        self.render()

    def config_view(self):
        self.page.title = "Puzzle MVC"
        self.page.window.width = 500
        self.page.window.height = 650
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_click_cell(self, e):        
        row, col = e.control.data
        self.controller.handle_click_cell(row, col)

    def view_boton_selected(self, row, col):        
        new_selected_btn = self.buttons[(row, col)]
                
        if self.selected_btn:
            self.selected_btn.style.bgcolor = const.AVAILABLE_MOVEMENT
            self.selected_btn.update()  
            if self.selected_btn.data == (row, col):                
                self.selected_btn = None
                return                                                                    
        self.selected_btn = new_selected_btn
        self.selected_btn.style.bgcolor = const.SELECTED
        self.selected_btn.update()    

    def view_selection_movements(self, movements: list[tuple[int, int]]):        
        for tuple in movements:            
            btn = self.buttons[tuple]
            btn.style.bgcolor = const.AVAILABLE_MOVEMENT   
            btn.update()         
        
    def build_grid(self):
        grid = ft.Column(spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                
        for r in range(self.controller.model.rows):
            row = ft.Row(spacing=10, alignment=ft.MainAxisAlignment.CENTER)
            for c in range(self.controller.model.columns):
                cell = self.controller.model.structure[r][c]
                is_empty = cell.value is None
                
                btn = ft.Button(
                    content=ft.Text(str(cell.value) if not is_empty else "X", size=20),
                    width=80, height=80,
                    data=(r, c),
                    on_click=self.on_click_cell,
                    style=ft.ButtonStyle(
                        bgcolor="cyan700" if is_empty else "blueGrey50",
                        shape=ft.RoundedRectangleBorder(radius=10),
                    )
                )
                self.buttons[(r, c)] = btn
                row.controls.append(btn)
            grid.controls.append(row)
        return grid

    def render(self):
        self.page.clean()
        self.page.add(
            ft.Text("Puzzle de Números", size=32, weight=ft.FontWeight.BOLD),
            self.build_grid()
        )
        self.controller.update_selection_movements()