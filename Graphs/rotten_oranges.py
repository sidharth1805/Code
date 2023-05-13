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
            for i in range(len(q)):
                r, c = q.popleft()
                for row, column in dir:
                    nr = r + row
                    nc = c + column
                    if(nr > 0 and nr != n and nc > 0 and nc != c and A[nr][nc] == 1):
                        q.append([nr, nc])
                        A[nr][nc] == 2
                        fresh -= 1
            time += 1
        if fresh == 0 :
            return time
        else:
            return -1