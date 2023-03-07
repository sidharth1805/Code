class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def morris_traversal(self, root):
        ans = []
        curr_node = root
        while curr_node:
            if curr_node.left is None:
                ans.append(curr_node.val)
                curr_node = curr_node.right
            else:
                temp_node = curr_node.left

                while temp_node.right and temp_node.right != curr_node:
                    temp_node = temp_node.right

                if temp_node.right is None:
                    temp_node.right = curr_node
                    curr_node = curr_node.left

                if temp_node.right == curr_node:
                    temp_node.right = None
                    ans.append(curr_node.val)
                    curr_node = curr_node.right
        return ans
