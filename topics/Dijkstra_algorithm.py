import heapq

def dijkstra(graph, start):
    # graph: {node: [(neighbor, weight), ...]}
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    heap = [(0, start)]   # (distance, node)
    visited = set()

    while heap:
        current_dist, node = heapq.heappop(heap)

        if node in visited:
            continue   # already finalized with a shorter distance
        visited.add(node)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 1), ('B', 2), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

print(dijkstra(graph, 'A'))
# {'A': 0, 'B': 3, 'C': 1, 'D': 8}
