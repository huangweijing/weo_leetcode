from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.arr = []
        self.k = 0
        self.dp = []

    @cache
    def solve(self, n: int) -> int:
        if n == 1:
            return self.arr[0]
        if n <= 0:
            return 0
        result = 0
        for i in range(1, self.k + 1):
            if n - i >= 0:
                result = max(result, self.solve(n - i) + max(self.arr[n - i: n]) * i)
        return result

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.arr = arr
        self.k = k
        # self.dp = [-1] * len(arr) + 1
        return self.solve(len(arr))

data_arr = [1,15,7,9,2,5,10]
data_k = 3
r = Solution().maxSumAfterPartitioning(data_arr, data_k)
print(r)