from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0].copy()
        # print(dp)
        for row_idx, row in enumerate(points[1:], start=1):
            new_dp = [0] * len(points[0])
            max_val = 0
            for i, val in enumerate(row):
                max_val = max(max_val, dp[i])
                new_dp[i] = max(new_dp[i], max_val + val)
                max_val -= 1
            max_val = 0
            for i, val in enumerate(reversed(row)):
                max_val = max(max_val, dp[-1 - i])
                # print(val, max_val)
                new_dp[-1 - i] = max(new_dp[-1 - i], max_val + val)
                max_val -= 1
            # print(dp, new_dp)
            dp = new_dp
        ans = max(dp)
        return ans


data = [[1,5],[2,3],[4,2]]
r = Solution().maxPoints(data)
print(r)
