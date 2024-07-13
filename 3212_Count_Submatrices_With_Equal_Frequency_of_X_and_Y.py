from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        ans = 0
        dp = []
        for i, row in enumerate(grid):
            x_cnt, y_cnt = 0, 0
            dp_row = []
            for j, val in enumerate(row):
                if val == "X":
                    x_cnt += 1
                elif val == "Y":
                    y_cnt += 1
                if i == 0:
                    x, y = x_cnt, y_cnt
                else:
                    x = x_cnt + dp[i - 1][j][0]
                    y = y_cnt + dp[i - 1][j][1]
                dp_row.append([x, y])
                if x == y and x > 0:
                    ans += 1
            dp.append(dp_row)
        return ans

