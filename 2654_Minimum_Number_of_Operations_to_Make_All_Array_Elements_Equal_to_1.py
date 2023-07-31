import math
from typing import List
from functools import reduce

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        gcd_all = reduce(math.gcd, nums)
        if gcd_all != 1:
            return -1
        smallest_sub_arr_len = len(nums)
        for i, num in enumerate(nums):
            gcd_part = nums[i]
            if gcd_part == 1:
                smallest_sub_arr_len = 1
                break
            for j, num2 in enumerate(nums[i + 1: ], start=2):
                gcd_part = math.gcd(gcd_part, num2)
                if gcd_part == 1:
                    smallest_sub_arr_len = min(smallest_sub_arr_len, j)
                    break
        if smallest_sub_arr_len == 1:
            return len([ele for ele in nums if ele != 1])
        return len([ele for ele in nums if ele != 1]) - 1 + smallest_sub_arr_len - 1

r = Solution().minOperations([1, 1])
print(r)
