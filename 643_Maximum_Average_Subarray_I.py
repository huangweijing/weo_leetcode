from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum4 = sum(nums[:k])
        max_sum4 = sum4
        for i in range(k, len(nums)):
            # print(sum4)
            sum4 = sum4 - nums[i - k] + nums[i]
            max_sum4 = max(sum4, max_sum4)
        return max_sum4 / k

data_nums = [1,12,-5,-6,50,3]
r = Solution().findMaxAverage(data_nums, 4)
print(r)