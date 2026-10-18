# Pathfinder Visualizer

A breadth-first search (BFS) pathfinder on a grid, with a tkinter window that animates the search and draws the shortest path. Built step by step as a Python learning project.

## Features

- Click or drag to draw walls (starting a drag on a wall erases)
- Set the start and end cells anywhere that isn't a wall
- Run BFS and watch the exploration, then the shortest path
- Reports the path length, or "No Path" when the end can't be reached
- Random walls button (never covers the start or end)
- Reset button (also cancels an animation in progress)

## Project structure

| File | What it does |
|------|--------------|
| `pathfinder.py` | The logic only: `get_neighbors`, `bfs`, `get_path`. Knows nothing about windows. |
| `gui.py` | The tkinter interface: drawing, mouse events, buttons, animation. Imports from `pathfinder.py`. |

Keeping them separate means the same BFS code can be reused with a text printout, a different GUI, or tests.

## How to run

Needs Python 3 only (tkinter ships with it). Keep both files in the same folder:

```
python gui.py
```

1. Pick **Walls** and click or drag on the grid to draw obstacles.
2. Use **Set Start** / **Set End**, then click a cell, to move the endpoints.
3. Press **Run** to animate the search.
4. **Random** fills the grid with random walls. **Reset** clears everything.

Grid size and cell size are the `ROWS`, `COLS` and `CELL` constants at the top of `gui.py`.

## How it works

1. **Queue and visited set.** BFS keeps a `deque` of cells to explore and a `set` of cells already seen. `popleft()` and `in` on a set are both fast, which keeps BFS linear in the number of cells.
2. **Exploring.** Take the cell at the front of the queue, look at its up/down/left/right neighbors that aren't walls or off the grid, and queue any not yet visited.
3. **`came_from`.** Each time a cell is queued, record which cell discovered it: `came_from[neighbor] = current`.
4. **Rebuilding the path.** Start at the end, repeatedly jump to `came_from[cell]` until you reach the start, then reverse the list. Because BFS explores in order of distance, this is a shortest path.
5. **Animation.** The GUI does not loop with `sleep` (that would freeze the window). It uses `root.after` to schedule one step at a time.

## How it was built

1. **Queue/dequeue basics**, then BFS on a small dictionary graph (`"A"` to `"F"`).
2. **BFS on a grid.** Replaced the dictionary with a 2D list where `0` is open and `1` is a wall, and wrote `get_neighbors`.
3. **Text visualizer.** `show` prints the grid with each cell's visit number, `#` for walls and `.` for unexplored cells.
4. **Shortest path.** Added `came_from` and `get_path`, then marked the path with `*`.
5. **Edge cases.** `bfs` now returns `(order, came_from)` on every exit so callers never unpack the wrong shape. The end being unreachable prints "No Path" instead of crashing. Start equal to end gives a one-cell path. Walls on the start or end are rejected.
6. **Custom layout.** Replaced random walls with a wall list, and made start and end variables.
7. **tkinter GUI.** Grid of rectangles, click and drag walls, set start/end, animated exploration and path, reset.
8. **Split into two files**, logic and GUI.
9. **Random walls button.**

## Known limits and ideas

- Random walls don't guarantee a path exists, so "No Path" shows up sometimes.
- Walls are scattered, not a true maze with corridors. A maze generator (for example randomized DFS) would be a good next step.
- Only BFS is implemented. Adding Dijkstra or A* would let you compare algorithms on the same grid.
- Might try/implement Bi-directional BFS and see the diiference between BFS and Bidirectional BFS
- Diagonal moves and weighted cells are not supported. Weighted and Diagonals are going to be implemented after understanding the logic behind it.