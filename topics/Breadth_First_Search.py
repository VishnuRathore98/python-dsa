def bfs(graph, start):
    visited = set([start])
    queue = [start]
    order = []

    while queue:
        node = queue.pop(0)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

print(bfs(graph, 'A'))   # ['A', 'B', 'C', 'D']
