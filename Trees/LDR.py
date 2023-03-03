class Tree_Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.right = None
        self.left = None


class Inorder_Traversal:
    def Inorder_traversal(self, root) -> list:
        stack = []
        ans = []
        curr_ele = root

        while curr_ele or len(stack) > 0:
            # Left
            while curr_ele:
                stack.append(curr_ele.val)
                curr_ele = curr_ele.left
            curr_ele = stack.pop()
            # Data
            ans.append(curr_ele)
            # Right
            curr_ele = curr_ele.right

        return ans
