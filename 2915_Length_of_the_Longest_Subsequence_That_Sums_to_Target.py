from typing import List
from collections import Counter


class Solution:

    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        dp = [Counter() for _ in nums]
        dp[0][nums[0]] = 1
        for i, num in enumerate(nums[1: ], start=1):
            dp[i] = dp[i - 1].copy()
            dp[i][num] = max(1, dp[i][num])
            for key, val in dp[i - 1].items():
                if key + num <= 1000:
                    dp[i][key + num] = max(dp[i][key + num], dp[i - 1][key] + 1)
        # print(dp)
        if target in dp[len(nums) - 1]:
            return dp[len(nums) - 1][target]
        else:
            return -1


data = [
[4,1,3,2,1,5]
, 7
]
r = Solution().lengthOfLongestSubsequence(* data)
print(r)

