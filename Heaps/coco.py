import heapq


class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        print(B)
        B = [i * -1 for i in B]
        heapq.heapify(B)
        print(B)
        ans = 0
        for i in range(A):
            max_ele = (-1) * heapq.heappop(B)
            ans += max_ele
            heapq.heappush(B, (-1) * (max_ele // 2))
            print(B)
        print(ans % (10**9 + 7))


sol = Solution()
A = 10
b = [2147483647, 2000000014, 2147483647]
sol.nchoc(A, b)
