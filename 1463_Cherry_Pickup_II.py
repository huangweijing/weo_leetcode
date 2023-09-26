from typing import List


class Solution:

    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = [[-1] * len(grid[0])
              for _ in grid[0]]
        dp[0][len(grid[0]) - 1] = grid[0][0] + grid[0][-1]
        for row_idx, row in enumerate(grid[1:]):
            new_dp = [[-1] * len(grid[0])
              for _ in grid[0]]
            # print(dp)
            for pos1 in range(len(new_dp)):
                for pos2 in range(len(new_dp[0])):
                    prev = []
                    if dp[pos1][pos2] != -1:
                        prev.append(dp[pos1][pos2])
                    if pos1 - 1 >= 0:
                        if dp[pos1 - 1][pos2] != -1:
                            prev.append(dp[pos1 - 1][pos2])
                        if pos2 - 1 >= 0 and dp[pos1 - 1][pos2 - 1] != -1:
                            prev.append(dp[pos1 - 1][pos2 - 1])
                        if pos2 + 1 < len(dp) and dp[pos1 - 1][pos2 + 1] != -1:
                            prev.append(dp[pos1 - 1][pos2 + 1])
                    if pos1 + 1 < len(dp):
                        if dp[pos1 + 1][pos2] != -1:
                            prev.append(dp[pos1 + 1][pos2])
                        if pos2 - 1 >= 0 and dp[pos1 + 1][pos2 - 1] != -1:
                            prev.append(dp[pos1 + 1][pos2 - 1])
                        if pos2 + 1 < len(dp) and dp[pos1 + 1][pos2 + 1] != -1:
                            prev.append(dp[pos1 + 1][pos2 + 1])
                    if pos2 - 1 >= 0 and dp[pos1][pos2 - 1] != -1:
                        prev.append(dp[pos1][pos2 - 1])
                    if pos2 + 1 < len(dp) and dp[pos1][pos2 + 1] != -1:
                        prev.append(dp[pos1][pos2 + 1])
                    # if row_idx == 0 and pos1 == 1 and pos2 == len(dp) - 2:
                    #     print(prev)
                    if len(prev) > 0:
                        point = max(prev)
                        if pos1 == pos2:
                            point += row[pos1]
                        else:
                            point += row[pos1] + row[pos2]
                        new_dp[pos1][pos2] = point
            dp = new_dp
        ans = max([max(x) for x in dp])
        return ans

grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
r = Solution().cherryPickup(grid)
print(r)