from collections import deque, defaultdict
class Solution:
    def cycle_check(self, ele):
        visited[ele] = True
        dfs_visted[ele] = True
        for i in adj_list[ele]:
            if visited[i] == False:
                if self.cycle_check(i):
                    return True
            elif dfs_visted[i] == True:
                return True
        dfs_visted[ele] = False
        return False         
    def solve(self, A, B):
        global adj_list
        adj_list = defaultdict(list)
        #Nodes from 1 -> A
        for i in range(len(B)):
            adj_list[B[i][0]].append(B[i][1])
        global visited
        visited = [False] * (A+1)
        global dfs_visted
        dfs_visted = [False] * (A+1)
        for i in range(1,A):
            if visited[i] == False:
                if self.cycle_check(i):
                    return 1
        return 0
