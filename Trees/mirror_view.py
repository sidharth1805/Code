from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirror_view(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            temp_node = q.popleft()
            temp_node.left, temp_node.right = temp_node.right, temp_node.left
            if temp_node.left:
                q.append(temp_node.left)
            if temp_node.right:
                q.append(temp_node.right)
        return root
