from typing import List
from collections import deque


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        left_inc = deque()
        right_inc = deque()
        for i, num in enumerate(nums):
            if i > 0 and num > nums[i - 1]:
                left_inc.append(left_inc[-1] + 1)
            else:
                left_inc.append(1)
        for i, num in enumerate(reversed(nums)):
            if i > 0 and num < nums[-i]:
                right_inc.appendleft(right_inc[0] + 1)
            else:
                right_inc.appendleft(1)
        # print(left_inc, right_inc)
        ans = 0
        for i, num in enumerate(nums):
            if i > 0:
                ans = max(ans, min(left_inc[i - 1], right_inc[i]))
        return ans
    
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        max_k = self.maxIncreasingSubarrays(nums)
        return max_k >= k
    

data = [2,5,7,8,9,2,3,4,3,1]
r = Solution().maxIncreasingSubarrays(data)
print(r)

        