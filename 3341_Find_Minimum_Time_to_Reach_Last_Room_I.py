from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dp = [[0] * len(moveTime[0]) for _ in moveTime]
        dp[0][0] = 0
        for i in range(len(moveTime)):
            for j in range(len(moveTime[0])):
                if i == j == 0:
                    continue
                dp1, dp2 = 10e9, 10e9
                if i > 0:
                    dp1 = dp[i - 1][j]
                if j > 0:
                    dp2 = dp[i][j - 1]
                # print(i, j, dp1, dp2)
                dp[i][j] = max(moveTime[i][j], min(dp1, dp2)) + 1
        print(dp)
        return dp[-1][-1]
    

data = [[94,79,62,27,69,84],[6,32,11,82,42,30]]
r = Solution().minTimeToReach(data)
print(r)
            

        