import tkinter as tk

ROWS, COLS = 15, 25
CELL = 30

root = tk.Tk()
canvas = tk.Canvas(root, width=COLS * CELL, height=ROWS * CELL)
canvas.pack()

rects = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        x1, y1 = c * CELL, r * CELL
        x2, y2 = x1 + CELL, y1 + CELL
        rect = canvas.create_rectangle(x1, y1, x2, y2, fill="black", outline="gray")
        row.append(rect)
    rects.append(row)
canvas.itemconfig(rects[7][3], fill="green")
root.mainloop()
