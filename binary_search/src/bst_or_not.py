

class node: # can't change the class name because of test runner
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root == None:
        return node(data)
    else:
        if data <= root.data:
            cur = insert(root.left, data)
            root.left = cur
        else:
            cur = insert(root.right, data)
            root.right = cur
    return root


def checkBST(root):

    def is_bst(node, min_val, max_val):

        if node is None:
            return True

        if node.data < min_val or node.data > max_val:
            return False

        return is_bst(node.left, min_val, node.data -1) and is_bst(node.right, node.data + 1, max_val)

    return is_bst(root, 0, float('inf'))
