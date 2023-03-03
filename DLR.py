# Definition for a binary tree node
class Tree_Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root : root node of tree
    # @return a list of integers
    def preorderTraversal(self, root):
        ans = []
        stack = []
        stack.append(root)
        while len(stack) != 0:
            cur_node = stack.pop()
            ans.append(cur_node.val)
        if cur_node.right:
            stack.append(cur_node.right)
        if cur_node.left:
            stack.append(cur_node.left)
        return ans


# generate a list
