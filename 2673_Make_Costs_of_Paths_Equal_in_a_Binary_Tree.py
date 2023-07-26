from typing import List


class Solution:

    def __init__(self):
        self.longest_path = 0
        self.cost = []
        self.path = []

    def calc_longest_path(self, root: int, length: int):
        length += self.cost[root]
        if root * 2 + 1 < len(self.cost):
            self.calc_longest_path(root * 2 + 1, length)
        else:
            self.longest_path = max(self.longest_path, length)
            self.path[root] = length

        if root * 2 + 2 < len(self.cost):
            self.calc_longest_path(root * 2 + 2, length)
        else:
            self.longest_path = max(self.longest_path, length)
            self.path[root] = length

    def minIncrements(self, n: int, cost: List[int]) -> int:
        self.cost = cost
        self.path = [0] * n
        self.calc_longest_path(0, 0)
        increment_arr = [0] * n
        for i in range(n // 2, n):
            increment_arr[i] = self.longest_path - self.path[i]
        layer = n.bit_count() - 1
        while layer > 0:
            # print((1 << (layer - 1)) - 1, (1 << layer) - 1)
            for i in range((1 << (layer - 1)) - 1, (1 << layer) - 1):
                min_incr = min(increment_arr[i * 2 + 1], increment_arr[i * 2 + 2])
                increment_arr[i * 2 + 1] -= min_incr
                increment_arr[i * 2 + 2] -= min_incr
                increment_arr[i] = min_incr
            layer -= 1
        return sum(increment_arr)

data = [
   15
   , [764,1460,2664,764,2725,4556,5305,8829,5064,5929,7660,6321,4830,7055,3761]
]
r = Solution().minIncrements(* data)
print(r)