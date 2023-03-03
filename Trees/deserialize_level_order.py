from collections import deque


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def solve(self, A):
        q = deque()
        top_root = TreeNode(A[0])
        q.append(top_root)
        idx = 1
        while q:
            root = q.popleft()

            if A[idx] != -1:
                root.left = A[idx]
            idx += 1

            if A[idx] != -1:
                root.right = A[idx]
            idx += 1

            if root.right:
                q.append(root.right)
            if root.right:
                q.append(root.right)

        return top_root
