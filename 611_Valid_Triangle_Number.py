from typing import List
import bisect


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        for i, side in enumerate(nums):
            for j, side2 in enumerate(nums[i + 1: ], start=i + 1):
                idx = bisect.bisect_right(nums, side + side2 - 1) - 1
                if idx > j:
                    ans += idx - j
        return ans


data = [2,2,3,4]
r = Solution().triangleNumber(data)
print(r)