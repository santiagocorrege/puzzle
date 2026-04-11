import flet as ft
from models import Puzzle 

def main(page: ft.Page):
    page.title = "Puzzle Interactivo"
    
    page.window.width = 500
    page.window.height = 650
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    puzzle_data = Puzzle(rows=4, columns=4)

    def on_click_cell(e):
        btn = e.control
        
        # Actualizado de ElevatedButton a Button
        if not isinstance(btn, ft.Button): 
            return
            
        if btn.data:
            row, col = btn.data
            if puzzle_data.structure:
                valor = puzzle_data.structure[row][col].value
                print(f"Click en [{row}, {col}] | Valor: {valor}")
        
        btn.style = ft.ButtonStyle(
            bgcolor="amber300", 
            shape=ft.RoundedRectangleBorder(radius=10),
            color="black"
        )
        btn.update()

    def build_grid():
        grid = ft.Column(
            spacing=10, 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
        
        if not puzzle_data.structure:
            return grid

        for r in range(puzzle_data.rows):
            fila_controles = ft.Row(
                spacing=10, 
                alignment=ft.MainAxisAlignment.CENTER
            )
            for c in range(puzzle_data.columns):
                celda = puzzle_data.structure[r][c]
                es_vacio = celda.value is None
                
                # Actualizado de ElevatedButton a Button
                btn = ft.Button(
                    content=ft.Text(
                        value=str(celda.value) if not es_vacio else "X",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="black" if not es_vacio else "white"
                    ),
                    width=80,
                    height=80,
                    data=(r, c),
                    on_click=on_click_cell,
                    style=ft.ButtonStyle(
                        bgcolor={
                            ft.ControlState.DEFAULT: "cyan700" if es_vacio else "blueGrey50",
                            ft.ControlState.HOVERED: "cyan500",
                        },
                        shape=ft.RoundedRectangleBorder(radius=10),
                        padding=0
                    )
                )
                fila_controles.controls.append(btn)
            grid.controls.append(fila_controles)
        return grid

    grid_ui = build_grid()
    
    page.clean()
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Puzzle de Números", size=32, weight=ft.FontWeight.BOLD, color="blueGrey900"),
                    ft.Divider(height=30, color="transparent"),
                    grid_ui,
                ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            alignment=ft.Alignment(0, 0) 
        )
    )
    page.update()

if __name__ == "__main__":
    # Pasamos la función directamente
    ft.run(main)