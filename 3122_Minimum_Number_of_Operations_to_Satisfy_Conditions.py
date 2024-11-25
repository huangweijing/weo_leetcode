from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        dp = [0] * 10
        for i in range(len(grid[0])):
            new_dp = [10e9] * 10
            cnt = Counter([grid[j][i] for j in range(len(grid))])
            for k, _ in enumerate(new_dp):
                cost = len(grid) - cnt[k]
                for l, old_val in enumerate(dp):
                    if l != k:
                        new_dp[k] = min(old_val + cost, new_dp[k])
            dp = new_dp
            # print(dp)
        return min(new_dp)
    
data = [[1,1,1],[0,0,0]]
r = Solution().minimumOperations(data)
print(r)

        