import heapq

def network_delay_time(times, n, k):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in times:
        graph[u].append((v, w))

    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    heap = [(0, k)]
    visited = set()

    while heap:
        current_dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    max_dist = max(distances.values())
    return max_dist if max_dist != float('inf') else -1


times = [[2,1,1], [2,3,1], [3,4,1]]
n = 4
k = 2
print(network_delay_time(times, n, k))   # 2
