from collections import deque


def get_neighbors(grid, r, c):
    neighbors = []
    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 1:
            neighbors.append((nr, nc))

    return neighbors


def bfs(grid, start, end):
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
