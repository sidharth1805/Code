from collections import defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def dfs(self, node, vis_arr, adj_list, stack):
        vis_arr[node] = 1
        for element in adj_list[node]:
            if vis_arr[element] != 1:
                self.dfs(element, vis_arr, adj_list, stack)
        stack.append(node)

    def solve(self, A, B):
        adj_list = defaultdict(list)
        for i in range(len(B)):
            adj_list[B[i][0]].append(B[i][1])
        vis_arr = [0] * (A + 1)
        stack = []
        for i in range(1, A + 1):
            if vis_arr[i] != 1:
                self.dfs(i, vis_arr, adj_list, stack)
        print(stack)
