from typing import List
from collections import Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        k = 2
        ans = 0
        dp = [Counter() for _ in range(k)]
        for i, num in enumerate(nums):
            # print(f"num={num}")
            for j in range(k):
                max_len = dp[j][(j + k - num % k) % k] + 1
                dp[j][num % k] = max(dp[j][num % k], max_len)
                ans = max(ans, max_len)
            # print(dp)
        return ans


data = [
    [1, 4, 2, 3, 1, 4]
    , 3
]
r = Solution().maximumLength(* data)
print(r)



