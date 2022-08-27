from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        num_sum = []
        sum_val = 0
        for num in nums:
            sum_val += num
            num_sum.append(sum_val)
        if num_sum[-1] < target:
            return 0

        left = 0
        right = 0
        while right < len(num_sum) and num_sum[right] < target:
            right += 1
        # print(nums[:right + 1])
        min_len = right - left + 1
        while right < len(num_sum):
            while left <= right and num_sum[right] - num_sum[left] >= target:
                min_len = min(min_len, right - left)
                # print(nums[left + 1:right + 1])
                left += 1
            while right < len(num_sum) and num_sum[right] - num_sum[left] < target:
                right += 1

        return min_len

data_target = 7
data_nums = [2,3,1,2,4,3]
r = Solution().minSubArrayLen(target=data_target, nums=data_nums)
print(r)
