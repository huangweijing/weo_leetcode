from typing import List
from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def my_sol(left: int, right: int, start: int, end: int) -> int:
            ret = 0
            for i in range(start, end + 1):
                # print(nums[i] * left * right)
                coin = nums[i] * left * right
                left_part, right_part = 0, 0
                if i > start:
                    left_part = my_sol(left, nums[i], start, i - 1)
                if i < end:
                    right_part = my_sol(nums[i], right, i + 1, end)
                # print(coin, left_part, right_part)
                ret = max(ret, coin + left_part + right_part)
            return ret
        return my_sol(1, 1, 0, len(nums) - 1)
    

data = [3,1,5,8]
r = Solution().maxCoins(data)
print(r)
                