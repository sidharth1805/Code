import heapq


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        heapq.heapify(A)
        min_cost = 0
        while len(A) > 1:
            a = heapq.heappop(A)
            b = heapq.heappop(A)
            build_cost = a + b
            min_cost += build_cost
            heapq.heappush(A, build_cost)
        return min_cost


sol = Solution()
A = [5, 17, 100, 11]
sol.solve(A)
