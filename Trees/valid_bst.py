class Tree_Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def valid_bst(self, root):
        def is_valid(root, left, right):
            if not root:
                return True

            if not ((left < root.val) and (root.val < right)):
                return False

            return is_valid(root.left, left, root.val) and is_valid(
                root.right, root.val, right
            )

        if is_valid(root, float("-inf"), float("inf")):
            return 1
        else:
            return 0
