from typing import List
import bisect

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # print(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                c = abs(nums[i] - nums[j])
                idx = bisect.bisect_right(nums[:j], c)
                # print(nums[:j], idx, c)
                if idx >= j:
                    continue
                return nums[i] + nums[j] + nums[j-1]
        return 0

data_nums = [3,2,3,4]
r = Solution().largestPerimeter(data_nums)
print(r)
