import random
import tkinter as tk

from pathfinder import bfs, get_path

ROWS, COLS = 15, 20
CELL = 24
DELAY = 15  # ms between animation steps

OPEN_COLOR = "#e2e8f0"
WALL_COLOR = "#0f172a"
START_COLOR = "#22c55e"
END_COLOR = "#ef4444"
VISITED_COLOR = "#93c5fd"
PATH_COLOR = "#facc15"

grid = [[0] * COLS for _ in range(ROWS)]
start = (ROWS // 2, 2)
end = (ROWS // 2, COLS - 3)


state = {"mode": "walls", "paint": 1, "run": 0, "searched": False}


root = tk.Tk()
root.title("Pathfinder")

canvas = tk.Canvas(root, width=COLS * CELL, height=ROWS * CELL)
canvas.pack()

rects = []
for r in range(ROWS):
    row = []
    for c in range(COLS):
        x1, y1 = c * CELL, r * CELL
        row.append(
            canvas.create_rectangle(
                x1, y1, x1 + CELL, y1 + CELL, fill=OPEN_COLOR, outline="#94a3b8"
            )
        )
    rects.append(row)

status = tk.Label(root, text="Draw walls, then press Run")
status.pack()


def base_color(r, c):
    if (r, c) == start:
        return START_COLOR
    if (r, c) == end:
        return END_COLOR
    return WALL_COLOR if grid[r][c] == 1 else OPEN_COLOR


def repaint(r, c):
    canvas.itemconfig(rects[r][c], fill=base_color(r, c))


def repaint_all():
    for r in range(ROWS):
        for c in range(COLS):
            repaint(r, c)


def clear_search():
    state["run"] += 1  # cancels any animation in progress
    state["searched"] = False
    repaint_all()
    status.config(text="Draw walls, then press Run")


def cell_at(event):
    r, c = event.y // CELL, event.x // CELL
    if 0 <= r < ROWS and 0 <= c < COLS:
        return r, c
    return None


def on_press(event):
    global start, end
    cell = cell_at(event)
    if cell is None:
        return
    if state["searched"]:
        clear_search()
    r, c = cell

    if state["mode"] == "start":
        if grid[r][c] == 0 and cell != end:
            old = start
            start = cell
            repaint(*old)
            repaint(r, c)
    elif state["mode"] == "end":
        if grid[r][c] == 0 and cell != start:
            old = end
            end = cell
            repaint(*old)
            repaint(r, c)
    else:
        state["paint"] = 0 if grid[r][c] == 1 else 1
        apply_wall(cell)


def on_drag(event):
    if state["mode"] != "walls":
        return
    cell = cell_at(event)
    if cell is not None:
        apply_wall(cell)


def apply_wall(cell):
    r, c = cell
    if cell == start or cell == end:
        return
    grid[r][c] = state["paint"]
    repaint(r, c)


canvas.bind("<Button-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)


def set_mode(mode):
    state["mode"] = mode
    status.config(text=f"Mode: {mode}")


def run():
    clear_search()
    token = state["run"]
    state["searched"] = True

    order, came_from = bfs(grid, start, end)
    found = end in came_from or start == end
    path = get_path(came_from, start, end) if found else []

    def draw_path(i=0):
        if token != state["run"]:
            return
        if i < len(path):
            if path[i] not in (start, end):
                canvas.itemconfig(rects[path[i][0]][path[i][1]], fill=PATH_COLOR)
            root.after(DELAY * 2, draw_path, i + 1)
        else:
            status.config(text=f"Path length: {len(path) - 1} steps")

    def explore(i=0):
        if token != state["run"]:
            return
        if i < len(order):
            cell = order[i]
            if cell not in (start, end):
                canvas.itemconfig(rects[cell[0]][cell[1]], fill=VISITED_COLOR)
            root.after(DELAY, explore, i + 1)
        elif found:
            draw_path()
        else:
            status.config(text="No Path")

    explore()


def reset():
    global start, end
    for r in range(ROWS):
        for c in range(COLS):
            grid[r][c] = 0
    start, end = (ROWS // 2, 2), (ROWS // 2, COLS - 3)
    state["mode"] = "walls"
    clear_search()


def random_walls(density=0.28):
    clear_search()
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in (start, end):
                grid[r][c] = 0
            else:
                grid[r][c] = 1 if random.random() < density else 0
    repaint_all()
    status.config(text="Random walls generated")


bar = tk.Frame(root)
bar.pack(pady=4)
tk.Button(bar, text="Walls", command=lambda: set_mode("walls")).pack(
    side="left", padx=2
)
tk.Button(bar, text="Set Start", command=lambda: set_mode("start")).pack(
    side="left", padx=2
)
tk.Button(bar, text="Set End", command=lambda: set_mode("end")).pack(
    side="left", padx=2
)
tk.Button(bar, text="Generate Maze", command=random_walls).pack(side="left", padx=2)
tk.Button(bar, text="Run", command=run).pack(side="left", padx=2)
tk.Button(bar, text="Reset", command=reset).pack(side="left", padx=2)

repaint_all()
root.mainloop()
