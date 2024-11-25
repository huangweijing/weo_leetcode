from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0] * 3
        for num in nums:
            new_dp = dp.copy()
            for i, val in enumerate(dp):
                new_dp[(val + num) % 3] = max(new_dp[(val + num) % 3], val + num)
            dp = new_dp
        return dp[0]
    

data = [3,6,5,1,8]
r = Solution().maxSumDivThree(data)
print(r)