from typing import List
import bisect


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(reversed(nums)):
            lo, hi = lower - num, upper - num
            lo_idx = bisect.bisect_left(nums, lo) - 1
            hi_idx = bisect.bisect_right(nums, hi) - 1
            print(num, lo_idx, hi_idx)
            if hi_idx == -1 or lo_idx >= len(nums):
                continue
            if i >= hi_idx:
                continue
            print(num, lo_idx, hi_idx)
            ans += max(hi_idx - max(lo_idx, i + 1), 0)
            # ans += hi_idx - lo_idx
        return ans

data = [
    [0,1,4,4,5,7]
    , 3
    , 6
    # [1, 2, 5, 7, 9]
    # , 11
    # , 11
]
r = Solution().countFairPairs(*data)
print(r)
