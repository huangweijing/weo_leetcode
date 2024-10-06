from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        presum = 0
        ans = 0
        for num in nums:
            presum += num
            if presum > 0:
                ans += 1
            else:
                break
        return ans