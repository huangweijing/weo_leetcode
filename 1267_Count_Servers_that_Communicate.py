from typing import List

class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        row_cnt = [0] * len(grid)
        col_cnt = [0] * len(grid[0])
        for i, row in enumerate(grid):
            row_cnt[i] = row.count(1)

        for i in range(len(grid[0])):
            cnt = 0
            for j, row in enumerate(grid):
                if row[i] == 1:
                    cnt += 1
            col_cnt[i] = cnt

        ans = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    if not (row_cnt[i] == 1 and col_cnt[j] == 1):
                        ans += 1
        # print(row_cnt, col_cnt)
        return ans



r = Solution().countServers(
    [[1,1,0,0]
    ,[0,0,1,0]
    ,[0,0,1,0]
    ,[0,0,0,1]])
print(r)

