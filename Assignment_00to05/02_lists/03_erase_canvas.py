"""Implement an 'eraser' on a canvas.
The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
 We then create an eraser rectangle which, when dragged around the canvas, sets all of the 
 rectangles it is in contact with to white."""



import tkinter as tk

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.cell_size = 30
        self.rows = 20
        self.cols = 20

        self.cells = []
        self.create_grid()

        self.eraser_size = 60
        self.eraser = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, outline="black", fill="white")

        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
                row_cells.append(cell)
            self.cells.append(row_cells)

    def move_eraser(self, event):
        x, y = event.x, event.y
        self.canvas.coords(self.eraser, x, y, x + self.eraser_size, y + self.eraser_size)
        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        for row in self.cells:
            for cell in row:
                x1, y1, x2, y2 = self.canvas.coords(cell)
                if self.is_overlapping(x, y, x + self.eraser_size, y + self.eraser_size, x1, y1, x2, y2):
                    self.canvas.itemconfig(cell, fill="white")

    def is_overlapping(self, x1, y1, x2, y2, cx1, cy1, cx2, cy2):
        return not (x2 < cx1 or x1 > cx2 or y2 < cy1 or y1 > cy2)

if __name__ == "__main__":
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()


# run command (python 03_erase_canvas.py)
