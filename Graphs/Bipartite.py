from collections import defaultdict, deque


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):
        adj_list = defaultdict(list)
        for i in range(len(B)):
            adj_list[B[i][0]].append(B[i][1])
        print(adj_list)
        q = deque()
        color_arr = A * [0]
        q.append(0)
        color_arr[0] = 1
        while q:
            print(q)
            for i in range(len(q)):
                element = q.popleft()
                element_color = color_arr[element]
                for nod_ele in adj_list[element]:
                    if color_arr[nod_ele] == 0 and element_color == 1:
                        color_arr[nod_ele] = 2
                    elif color_arr[nod_ele] == 0 and element_color == 2:
                        color_arr[nod_ele] = 1
                    elif (
                        color_arr[nod_ele] != 0 and element_color == color_arr[nod_ele]
                    ):
                        return 0
                    else:
                        pass
                    q.append(nod_ele)
        return 1
