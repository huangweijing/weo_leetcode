from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        presum = [0]
        dp = [[0] *  len(nums) for _ in range(k + 1)]
        for i, num in enumerate(nums):
            presum.append(presum[-1] + num)
            dp[1][i] = presum[-1] / (i + 1)
        for i in range(2, k + 1):
            for j, num in enumerate(nums):
                for x in range(j):
                    dp[i][j] = max(dp[i][j], dp[i - 1][x] + (presum[j + 1] - presum[x + 1]) / (j - x))
        # print(dp)
        return dp[k][len(nums) - 1]
    

data = [
    [1,2,3,4,5,6,7]
    , 4
]
r = Solution().largestSumOfAverages(*data)
print(r)
