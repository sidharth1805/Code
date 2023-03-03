class Tree_Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.right = None
        self.left = None


class Postorder_traversal:
    def postorder_traversal(self, root) -> list:
        ans = []
        stack = []
        curr_ele = root

        while curr_ele and len(stack) > 0:
            # Go to Left-Most
            while curr_ele:
                stack.append(curr_ele)
                curr_ele = curr_ele.left
            # Move to right
            temp = stack[-1].right
            # If right is null back track
            if temp is None:
                temp = stack.pop()
                ans.append(temp)

                while stack and temp == stack.pop().right:
                    temp = stack.pop()
                    ans.append(temp)
            else:
                curr_ele = temp
        return ans
