def clone_graph_bfs(node):
    if node is None:
        return None

    visited = {node: Node(node.val)}
    queue = [node]

    while queue:
        current = queue.pop(0)
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            visited[current].neighbors.append(visited[neighbor])

    return visited[node]

cloned2 = clone_graph_bfs(node1)
print(cloned2.val)   # 1
