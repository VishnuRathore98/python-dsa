def inorder(node, result=None):
    if result is None:
        result = []
    if node:
        inorder(node.left, result)
        result.append(node.data)
        inorder(node.right, result)
    return result

def preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.data)
        preorder(node.left, result)
        preorder(node.right, result)
    return result

def postorder(node, result=None):
    if result is None:
        result = []
    if node:
        postorder(node.left, result)
        postorder(node.right, result)
        result.append(node.data)
    return result

print(inorder(bst.root))     # [20, 30, 40, 50, 60, 70, 80] — sorted!
print(preorder(bst.root))    # [50, 30, 20, 40, 70, 60, 80]
print(postorder(bst.root))   # [20, 40, 30, 60, 80, 70, 50]
