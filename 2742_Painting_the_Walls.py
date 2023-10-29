from typing import List
import math


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        # dp[i][j] 代表了从前i个墙里选择出哪些让付费油漆工涂j个墙时的最小cost
        dp = [[math.inf] * (n + 1) for _ in range(n)]
        dp[0][0] = 0  # 漆0面墙不需要花一分钱
        for j in range(min(n + 1, time[0] + 1 + 1)):
            dp[0][j] = min(cost[0], dp[0][j])
            # 第一个油漆工肯定是要收费的，他和免费油漆工合作油漆完time[0]+1个墙，
            # 所以若第0座墙选择油漆工时，油漆完time[0]+1的墙都是一样的价格
        for i in range(1, n):
            # 第i个墙的选择上场了, 先是选择不用收费油漆工的情况，相当于啥都没干
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
            # 第i个墙选择了收费油漆工，那么
            for j in range(n + 1):
                if j - time[i] - 1 < 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][0] + cost[i])
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - time[i] - 1] + cost[i])
        return dp[n - 1][n]


data = [
    [1,2,3,2]
    , [1,2,3,2]
]
r = Solution().paintWalls(*data)
print(r)

