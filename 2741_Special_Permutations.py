from functools import cache
from typing import List

class Solution:
    MOD = 10 ** 9 + 7

    def __init__(self):
        self.special_mat = []
        self.nums = []

    @cache
    def my_sol(self, last_idx: int, mask: int):
        n = len(self.nums)
        if mask == (1 << n) - 1:
            return 1

        ans = 0
        for i in range(len(self.nums)):
            if mask & (1 << i) == 0 and self.special_mat[last_idx][i]:
                ans += self.my_sol(i, mask | (1 << i))
                ans = ans % Solution.MOD
        return ans

    def specialPerm(self, nums: List[int]) -> int:
        self.nums = nums
        n = len(nums)
        self.special_mat = [[False] * n for _ in range(n)]
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num % num2 == 0 or num2 % num == 0:
                    self.special_mat[i][j] = True
        ans = 0
        for i in range(n):
            ans += self.my_sol(i, 1 << i)
            ans = ans % Solution.MOD
        return ans

data = [1,4,3]
r = Solution().specialPerm(data)
print(r)