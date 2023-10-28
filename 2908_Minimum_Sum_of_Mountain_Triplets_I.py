from typing import List
import math


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_val = math.inf
        min_arr_left = []
        min_arr_right = [math.inf] * len(nums)
        for i, num in enumerate(nums):
            if i > 0:
                min_val = min(nums[i - 1], min_val)
            min_arr_left.append(min_val)
        min_val = math.inf
        for i, num in enumerate(reversed(nums)):
            if i > 0:
                min_val = min(nums[len(nums) - 1 - i + 1], min_val)
            min_arr_right[len(nums) - 1 - i] = min_val
        ans = math.inf
        # print(min_arr_left)
        # print(min_arr_right)
        for i in range(1, len(nums)):
            num = nums[i]
            if min_arr_left[i] < num and min_arr_right[i] < num:
                ans = min(ans, num + min_arr_left[i] + min_arr_right[i])
        if ans == math.inf:
            return -1
        return ans


data = [6,5,4,3,4,5]
r = Solution().minimumSum(data)
print(r)
