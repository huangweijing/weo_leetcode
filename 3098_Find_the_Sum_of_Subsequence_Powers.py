import math
from typing import List
from functools import cache


class Solution:
    mod = 10 ** 9 + 7

    @cache
    def fact(self, k):
        if k == 1:
            return 1
        return k * self.fact(k - 1) % Solution.mod

    @cache
    def comb(self, n, k):
        if n == k or k == 0:
            return 1
        ret = 1
        for i in range(max(n - k, k) + 1, n + 1):
            ret *= i % Solution.mod
        return ret * self.fact(min(n - k, k)) % Solution.mod

    def sumOfPowers(self, nums: List[int], k: int) -> int:
        nums.sort()
        diff_list = []
        for i in range(1, len(nums)):
            diff = nums[i] - nums[0]
            diff_list.append(diff)
        diff_list.sort()

        ans = 0
        for i in range(len(diff_list) - k + 1):
            num = nums[i]
            # print(num)
            for j in range(i + 1, len(nums) - k + 2):
                res = abs(nums[j] - num) * self.comb(len(nums) - 1 - j, k - 2)
                ans += res
                print(num, nums[j], res, len(nums) - 1 - j, k - 2)
        return ans


data = [
    [1, 2, 3, 4]
    , 3
]
r = Solution().sumOfPowers(* data)
# print(Solution().comb(3, 3))
print(r)