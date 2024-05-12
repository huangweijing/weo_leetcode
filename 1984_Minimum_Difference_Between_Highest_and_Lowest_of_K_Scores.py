from typing import List
import math


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = math.inf
        nums.sort()
        for i in range(len(nums) - k + 1):
            ans = min(nums[i + k - 1] - nums[i], ans)
        return ans

data = [
    [1, 2]
    , 2
]
r = Solution().minimumDifference(*data)
print(r)
