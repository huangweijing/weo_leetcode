from typing import List
from sortedcontainers import SortedList
import math

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # print(nums)
        sl = SortedList()
        ans = math.inf
        for i, num in enumerate(nums):
            sl.add(num)
            if i + x < len(nums):
                idx = sl.bisect_right(nums[i + x])
                if idx < len(sl):
                    ans = min(ans, abs(nums[i + x] - sl[idx]))
                if idx > 0:
                    ans = min(ans, abs(nums[i + x] - sl[idx - 1]))
            # print(f"sl={sl}, i={i}, i+x={i + x}, ans={ans}")

        nums = list(reversed(nums))
        sl = SortedList()
        for i, num in enumerate(nums):
            sl.add(num)
            if i + x < len(nums):
                idx = sl.bisect_right(nums[i + x])
                if idx < len(sl):
                    ans = min(ans, abs(nums[i + x] - sl[idx]))
                if idx > 0:
                    ans = min(ans, abs(nums[i + x] - sl[idx - 1]))
            # print(f"sl={sl}, i={i}, i+x={i + x}, ans={ans}")

        return ans


data = [
    [5,3,2,10,15]
    , 1
]
r = Solution().minAbsoluteDifference(* data)
print(r)
