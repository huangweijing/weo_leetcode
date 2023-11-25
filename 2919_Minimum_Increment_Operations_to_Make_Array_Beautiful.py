from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        dp = [max(k - nums[2], 0)
            , max(k - nums[1], 0)
            , max(k - nums[0], 0)]
        ans = min(dp)
        for i, num in enumerate(nums[3: ], start=3):
            # print(dp)
            dp = [max(k - num, 0) + min(dp), dp[0], dp[1]]
            ans = min(dp)
        # print(dp)
        return ans

data = [
    [4,0,10,2,10,6]
    , 8
]
r = Solution().minIncrementOperations(* data)
print(r)

