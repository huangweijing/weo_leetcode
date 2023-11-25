from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        dp = [1, 1]
        for i, val in enumerate(arr[1: ], start=1):
            new_dp = [1, 1]
            if val > arr[i - 1]:
                new_dp[0] = dp[1] + 1
            elif val < arr[i - 1]:
                new_dp[1] = dp[0] + 1
            dp = new_dp
            ans = max(ans, dp[0], dp[1])
        return ans
