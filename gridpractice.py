import random

rows, colms = 5, 6

grid = [[0] * colms for _ in range(rows)]


placed = 0
while placed < 5:
    r = random.randint(0, 4)
    c = random.randint(0, 5)
    if grid[r][c] == 0:
        grid[r][c] = 1
        placed += 1


count = 0
visited = set()

for rs in range(rows):
    for cs in range(colms):
        if grid[rs][cs] == 0:
            visited.add((rs, cs))
            count += 1

print(count)
print(len(visited))
print(grid)
print()
print()


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


print(get_neighbors(grid, 1, 4))
