

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

"""
def checkBST(root): # can't change function name because of test runner



    if root == None:

        return True


    elif root.left == None and root.right == None:

        return True

    else:

        check = []

        try:

            check.append(root.right.data > root.data)

        except AttributeError:

            pass

        try:
            check.append(root.left.data <= root.data)

        except AttributeError:

            pass

        if False in check:

            return False

        else:

            return all([checkBST(root.left), checkBST(root.right)]) == True

"""

def checkBST(root):

    def is_bst(node, min_val=root.data, max_val=root.data):

        if node == None:
            return True

        if node.data < min_val or node.data > max_val:
            return False

        return is_bst(node.left, min_val, node.data -1) and is_bst(node.right, node.data + 1, max_val)

    return is_bst(root, root.data, root.data)

