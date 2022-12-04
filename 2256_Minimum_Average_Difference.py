from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left_sum, sum_all = [], 0
        for num in nums:
            sum_all += num
            left_sum.append(sum_all)
        mad = sum_all
        ans = 0
        for i, num in enumerate(nums):
            if i + 1 == len(nums):
                ad = int(left_sum[i] / (i + 1))
            else:
                ad = abs(int(left_sum[i] / (i + 1)) - int((sum_all - left_sum[i]) / (len(nums) - i - 1)))
            # print(i, ad)
            if ad < mad:
                mad = ad
                ans = i
        return ans

data = [4,2,0]
r = Solution().minimumAverageDifference(data)
print(r)