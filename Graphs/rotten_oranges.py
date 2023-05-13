from collections import deque
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        fresh, time = 0, 0
        n = len(A)
        m = len(A[0])
        q = deque()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    fresh += 1
                elif A[i][j] == 2:
                    q.append([i, j])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        while q and fresh > 0 :
            