from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrderTraversal(self, root):
        q = deque()
        hm = {}
        ans = []
        q.append((root, 0))
        while q:
            x = q.popleft()
            temp_node, level = x[0], x[1]
            if level not in hm:
                hm[level] = [temp_node.val]
            else:
                hm[level].append(temp_node.val)
            if temp_node.left:
                q.append((temp_node.left, level - 1))
            if temp_node.right:
                q.append((temp_node.right, level + 1))

        first_level = min(hm)
        last_level = max(hm)

        for level in range(first_level, last_level + 1):
            ans.append(hm[level])

        return ans
