class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root):
        if root is None:
            return 0
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
