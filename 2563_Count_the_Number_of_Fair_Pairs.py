from typing import List
import bisect


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            idx1 = bisect.bisect_left(nums, lower - num)
            idx2 = bisect.bisect_right(nums, upper - num) - 1
            idx1 = max(idx1, i + 1)
            ans += max(0, idx2 - idx1 + 1)
        return ans
    

data = [
    [0,1,2,7,4,4,5]
    , 3
    , 6
]
r = Solution().countFairPairs(*data)
print(r)