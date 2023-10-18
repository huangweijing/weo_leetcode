from typing import List
import math


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        real_target = target % sum_nums
        if real_target == 0:
            return len(nums) * (target // sum_nums)
        prefix_sum = 0
        prefix_sum_arr = [0] * len(nums)
        sum_idx_dict = dict[int, int]()
        sum_idx_dict[0] = -1
        ans = math.inf
        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_sum_arr[i] = prefix_sum
            if prefix_sum - real_target in sum_idx_dict:
                ans = min(ans, i - sum_idx_dict[prefix_sum - real_target])
            sum_idx_dict[prefix_sum] = i
        # print(prefix_sum_arr, real_target, sum_idx_dict)
        # print(ans)

        sum_idx_dict = dict[int, int]()
        suffix_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            sum_idx_dict[prefix_sum_arr[i]] = i

        for i in range(len(nums) - 1, -1, -1):
            suffix_sum += nums[i]
            if real_target - suffix_sum in sum_idx_dict:
                ans = min(ans, len(nums) - i + sum_idx_dict[real_target - suffix_sum] + 1 )
        if ans == math.inf:
            return -1
        return ans + (target // sum_nums) * len(nums)


data = [
    [1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6]
    , 56
]
r = Solution().minSizeSubarray(*data)
print(r)



