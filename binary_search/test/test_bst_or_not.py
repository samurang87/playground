import unittest
from binary_search.src.bst_or_not import node, insert, checkBST


class TestBinaryOrNot(unittest.TestCase):

    def test_insert(self):

        root = node(7)
        insert(root, 8)
        insert(root, 6)
        insert(root, 5)
        insert(root, 9)

        self.assertEqual(root.left.data, 6)
        self.assertEqual(root.left.left.data, 5)
        self.assertEqual(root.right.data, 8)
        self.assertEqual(root.right.right.data, 9)

    def test_checkBST_happy(self):

        root = node(7)
        insert(root, 8)
        insert(root, 6)
        insert(root, 5)
        insert(root, 9)

        self.assertTrue(checkBST(root))

    def test_checkBST_empty(self):

        root = node(7)

        self.assertTrue(checkBST(root))

    def test_checkBST_sad(self):

        root = node(7)

        root.left = node(6)

        root.right = node(8)

        root.right.right = node(4)

        self.assertFalse(checkBST(root))

    def test_checkBST_sad_2(self):

        root = node(3)

        root.left = node(2)

        root.left.left = node(1)

        root.left.right = node(4)

        root.right = node(6)

        root.right.left = node(5)

        root.right.right = node(7)

        self.assertFalse(checkBST(root))