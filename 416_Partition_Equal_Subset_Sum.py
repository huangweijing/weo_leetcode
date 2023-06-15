from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum & 1 == 1:
            return False
        nums_sum >>= 1
        dp = [[0] * (nums_sum + 1) for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            for j in range(1, nums_sum + 1):
                if num > j:
                    dp[i + 1][j] = max(dp[i + 1][j - 1], dp[i][j])
                else:
                    dp[i + 1][j] = max(dp[i][j - num] + num, dp[i][j])

                if dp[i + 1][j] == nums_sum:
                    return True
        # print(dp)
        return False

r = Solution().canPartition([1,5,10,6])
print(r)