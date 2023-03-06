class Tree_Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def delete_Node(self, root, key):
        if not root:
            return root
        elif root.val > key:
            root.left = self.delete_Node(root.left, key)
        elif root.val < key:
            root.right = self.delete_Node(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root.left
            while cur.right:
                cur = cur.right
            root.val = cur.val
            root.left = self.delete_Node(root.left, root.val)

        return root
