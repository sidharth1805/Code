from collections import deque


class Tree_node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root: Tree_node) -> list:
        ans = []
        q = deque()
        q.append(root)
        while q:
            cur_ele = []

            for i in range(len(q)):
                x = q.popleft()
                cur_ele.append()

                if x.left:
                    q.append(x.left)

                if x.left:
                    q.append(x.left)

            ans.append(cur_ele)
