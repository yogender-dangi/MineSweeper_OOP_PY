from tkinter import *
from cell import Cell
import constant
import settings

root = Tk()
root.geometry(f'{constant.WIDTH}x{constant.HEIGHT}')
root.configure(bg="black")
root.title("MineSweeper Game")
root.resizable(False, False)

top_frame = Frame( 
    root,
    bg="black",
    width=settings.width_prct(100),
    height=settings.height_prct(25)
)

top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg="black",
    width=settings.width_prct(25),
    height=(constant.HEIGHT - 80)
)
left_frame.place(x=0, y=100)

center_frame = Frame(
    root,
    bg = "black",
    width=settings.width_prct(75),
    height=settings.height_prct(75)
)
center_frame.place(x=250, y=100)

for x in range(constant.GRID_SIZE):
    for y in range(constant.GRID_SIZE):
        c = Cell(x,y)
        c.create_cell_btn_object(center_frame)
        c.cell_btn_object.grid(
            row = y, column = x
        )

Cell.randomized_mines()

root.mainloop()