class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node):
    if node is None:
        return None

    visited = {}   # maps original node -> cloned node

    def dfs(original):
        if original in visited:
            return visited[original]   # already cloned, avoid infinite loop

        clone = Node(original.val)
        visited[original] = clone   # register BEFORE recursing into neighbors

        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)


# Build a small graph: 1 -- 2
#                       |    |
#                       4 -- 3
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned = clone_graph(node1)
print(cloned.val)                                  # 1
print([n.val for n in cloned.neighbors])            # [2, 4]
print(cloned is node1)                              # False -> it's a true deep copy
