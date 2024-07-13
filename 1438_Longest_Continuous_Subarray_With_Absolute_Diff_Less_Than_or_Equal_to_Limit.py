from typing import List
from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ls = SortedList()
        left_idx, right_idx = 0, 0
        ans = 0
        while right_idx < len(nums):
            if len(ls) == 0:
                ls.add(nums[right_idx])
            else:
                while len(ls) > 0 and not nums[right_idx] - limit <= ls[0] <= ls[-1] <= nums[right_idx] + limit:
                    ls.remove(nums[left_idx])
                    left_idx += 1
                ls.add(nums[right_idx])
            ans = max(ans, len(ls))
            right_idx += 1
        return ans
