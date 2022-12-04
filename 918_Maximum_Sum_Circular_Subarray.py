import math
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prefix_sum_arr, prefix_sum = [], 0
        for num in nums:
            prefix_sum += num
            prefix_sum_arr.append(prefix_sum)
        ans = -math.inf
        lr_min = [math.inf] * len(prefix_sum_arr)
        rl_max = [-math.inf] * len(prefix_sum_arr)
        lr_max = [-math.inf] * len(prefix_sum_arr)
        rl_min = [math.inf] * len(prefix_sum_arr)
        for i in range(len(prefix_sum_arr) - 1, -1, -1):
            if i == len(prefix_sum_arr) - 1:
                rl_min[i] = rl_max[i] = prefix_sum_arr[-1]
            else:
                rl_min[i] = min(rl_min[i + 1], prefix_sum_arr[i])
                rl_max[i] = max(rl_max[i + 1], prefix_sum_arr[i])
        for i in range(len(prefix_sum_arr)):
            if i == 0:
                lr_min[i] = lr_max[i] = prefix_sum_arr[0]
            else:
                lr_min[i] = min(lr_min[i - 1], prefix_sum_arr[i])
                lr_max[i] = max(lr_max[i - 1], prefix_sum_arr[i])

        # print(prefix_sum_arr)
        # print(lr_max, lr_min, rl_max, rl_min)
        for i in range(len(prefix_sum_arr)):
            if i > 0:
                ans = max(rl_max[i] - lr_min[i - 1], ans)
            else:
                ans = max(rl_max[i], ans)
            if i > 0:
                ans = max(prefix_sum + lr_max[i - 1] - rl_min[i], ans)
        return ans

r = Solution().maxSubarraySumCircular([3,1,3,2,6])
print(r)