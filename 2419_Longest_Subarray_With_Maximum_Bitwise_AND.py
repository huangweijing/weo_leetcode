from typing import List
import math

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num, ans, i = -math.inf, 0, 0
        while i < len(nums):
            cnt = 1
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                cnt += 1
                i += 1
            if max_num < nums[i]:
                max_num = nums[i]
                ans = cnt
            elif max_num == nums[i]:
                ans = max(ans, cnt)
            i += 1
        return ans

data = [1,2,3,4]
r = Solution().longestSubarray(data)
print(r)