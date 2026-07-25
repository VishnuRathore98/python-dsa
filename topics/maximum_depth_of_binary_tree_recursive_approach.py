class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def max_depth(root):
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return 1 + max(left_depth, right_depth)


# Build a sample tree:
#         50
#        /  \
#      30    70
#      /\    /\
#    20 40 60 80
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print(max_depth(root))   # 3
