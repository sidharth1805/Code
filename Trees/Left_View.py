from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def left_view(self, root):
        q = deque()
        q.append(root)
        level_traversal = []
        ans = []

        while q:
            temp_result = []
            for i in range(len(q)):
                temp_node = q.popleft()
                temp_result.append(temp_node.val)
                if temp_node.left:
                    q.append(temp_node.left)
                if temp_node.right:
                    q.append(temp_node.right)

            level_traversal.append(temp_result)

        print(level_traversal)

        for level in range(len(level_traversal)):
            first_element = level_traversal[level][0]
            ans.append(first_element)

        return ans
