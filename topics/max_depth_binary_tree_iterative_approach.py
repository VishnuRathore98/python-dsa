def max_depth_iterative(root):
    if root is None:
        return 0
    depth = 0
    queue = [root]
    while queue:
        depth += 1
        next_level = []
        for node in queue:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level
    return depth

print(max_depth_iterative(root))   # 3
