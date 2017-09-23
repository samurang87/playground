

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