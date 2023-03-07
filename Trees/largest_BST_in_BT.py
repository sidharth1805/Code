class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def solve(self, A):
        def dfs(root):
            nonlocal result
            if not root:
                return [True, float("inf"), float("-inf"), 0]
            l_isBST, leftMin, leftMax, leftSize = dfs(root.left)
            r_isBST, rightMin, rightMax, rightSize = dfs(root.right)
            if l_isBST and r_isBST and root.val > leftMax and root.val < rightMin:
                result = max(result, leftSize + rightSize + 1)
                leftMin = root.val if leftMin == float("inf") else leftMin
                rightMax = root.val if rightMax == float("-inf") else rightMax
                return [True, leftMin, rightMax, leftSize + rightSize + 1]
            else:
                return [False, float("inf"), float("-inf"), 0]

        result = 0
        dfs(A)
        return result
