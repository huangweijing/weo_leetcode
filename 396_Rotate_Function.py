import math
from typing import List

class Solution:
    def __init__(self):
        self.dp = []
        self.sum_val = 0
        self.nums = []

    def f(self, k: int) -> int:
        if self.dp[k] != -1:
            return self.dp[k]
        if k == 0:
            self.dp[k] = sum([i * num for i, num in enumerate(self.nums)])
        else:
            self.dp[k] = self.f(k - 1) + self.sum_val - len(self.nums) * self.nums[-k]
        return self.dp[k]

    def maxRotateFunction(self, nums: List[int]) -> int:
        self.nums = nums
        self.dp = [-1] * len(nums)
        self.sum_val = sum(nums)
        result = -math.inf
        for k in range(len(nums)):
            result = max(result, self.f(k))
        # print(self.dp)
        return result

data_nums = [-1,-2,-32]
r = Solution().maxRotateFunction(data_nums)
print(r)