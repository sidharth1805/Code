class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class solution:
    def get_path(self, root, key, ans):
        if root is None:
            return False
        if root.val == key:
            ans.append(root.val)
            return True

        if self.get_path(root.left, key, ans) or self.get_path(root.right, key, ans):
            ans.append(root.val)
            return True
        else:
            return False

    def solve(self, root, A, B):
        arr_A = []
        arr_B = []

        self.get_path(root, A, arr_A)
        self.get_path(root, B, arr_B)

        if len(arr_A) > len(arr_B):
            arr_A, arr_B = arr_B, arr_A

        idx_min = len(arr_A) - 1
        idx_max = len(arr_B) - 1

        while idx_min >= 0:
            if arr_A[idx_min] != arr_B[idx_max]:
                return arr_A[idx_min + 1]

            idx_min -= 1
            idx_max -= 1

        return arr_A[idx_min + 1]
