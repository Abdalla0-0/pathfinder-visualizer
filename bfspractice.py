from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["F"],
    "E": ["F"],
    "F": [],
}


def bfs(graph, start, end):
    # make the queue with start in it
    # make visited with start in it
    # while the queue isn't empty:
    #     take the front, print it
    #     for each neighbor of it (graph[that item]):
    #         if not visited: add to visited, add to queue
    order = []
    queue = deque([start])
    visited = set({start})

    while queue:
        q = queue.popleft()
        order.append(q)
        if q == end:
            return order
        for i in graph[q]:
            if i not in visited:
                visited.add(i)
                queue.append(i)

    return "Not Found"


print(bfs(graph, "A", "C"))
