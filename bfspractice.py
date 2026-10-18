import random
from collections import deque

# graph = {
#     "A": ["B", "C"],
#     "B": ["D"],
#     "C": ["D", "E"],
#     "D": ["F"],
#     "E": ["F"],
#     "F": [],
# }


rows, colms = 5, 6

grid = [[0] * colms for _ in range(rows)]


placed = 0
while placed < 5:
    r = random.randint(0, 4)
    c = random.randint(0, 5)
    if grid[r][c] == 0:
        grid[r][c] = 1
        placed += 1
# print(grid)


def get_neighbors(grid, r, c):
    neighbors = []
    nr, nc = r - 1, c  # up
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
        neighbors.append((nr, nc))

    nr, nc = r + 1, c  # down
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
        neighbors.append((nr, nc))

    nr, nc = r, c - 1  # left
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
        neighbors.append((nr, nc))

    nr, nc = r, c + 1  # right
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
        neighbors.append((nr, nc))

    return neighbors


def bfs(grid, start, end):
    # make the queue with start in it
    # make visited with start in it
    # while the queue isn't empty:
    #     take the front, print it
    #     for each neighbor of it (graph[that item]):
    #         if not visited: add to visited, add to queue
    order = []
    came_from = {}
    queue = deque([start])
    visited = set({start})

    while queue:
        q = queue.popleft()
        order.append(q)
        r, c = q
        if q == end:
            return order, came_from
        for i in get_neighbors(grid, r, c):
            if i not in visited:
                visited.add(i)
                queue.append(i)
                came_from[i] = q

    return order, came_from


def get_path(came_from, start, end):
    path = []
    cell = end

    while cell != start:
        path.append(cell)
        cell = came_from[cell]

    path.append(start)
    path.reverse()

    return path


def show(grid, order, path):
    # 1. make a text grid: "#" for walls, "." for open cells
    # 2. loop over order and put each step number in its cell
    # 3. print it row by row
    rows, colms = 5, 6

    textGrid = [[0] * colms for _ in range(rows)]

    for r in range(rows):
        for c in range(colms):
            if grid[r][c] == 0:
                textGrid[r][c] = "."
            else:
                textGrid[r][c] = "#"

    for step, (r, c) in enumerate(order):
        textGrid[r][c] = step + 1
    for r, c in path:
        textGrid[r][c] = "*"

    for row in textGrid:
        line = ""
        for r in row:
            line += str(r).rjust(3)
        print(line)


order, came_from = bfs(grid, (0, 0), (4, 5))

path = []

if (4, 5) in came_from:
    path = get_path(came_from, (0, 0), (4, 5))
else:
    print("\033[4;1;31mNo Path\033[0m")


show(grid, order, path)


# print(bfs(grid, (0, 0), (4, 5)))
