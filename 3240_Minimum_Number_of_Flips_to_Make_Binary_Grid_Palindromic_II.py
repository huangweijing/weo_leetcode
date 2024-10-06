from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            if i >= m - 1 - i:
                break
            for j in range(n):
                if j >= n - 1 - j:
                    break
                else:
                    amt = grid[i][j] + grid[i][-1-j] + grid[-1-i][j] + grid[-1-i][-1-j]
                    ans += min(4 - amt, amt)
        center = 0
        middle_row, middle_col = 0, 0
        flip_cnt_row, flip_cnt_col = 0, 0 
        if m & 1 == 1 and n & 1 == 1:
            # flip center if it equals to 1
            center = grid[m // 2][n // 2]
            ans += grid[m // 2][n // 2]
        if m & 1 == 1:
            middle_row = sum(grid[m // 2]) - center
            for i in range(n // 2):
                if grid[m // 2][i] != grid[m // 2][-i - 1]:
                    flip_cnt_row += 1
        if n & 1 == 1:
            middle_col = sum(row[n // 2] for row in grid) - center
            for i in range(m // 2):
                if grid[i][n // 2] != grid[-1-i][n // 2]:
                    flip_cnt_col += 1

        okay_one = middle_row + middle_col - flip_cnt_col - flip_cnt_row
        # print(okay_one, flip_cnt_col, flip_cnt_row, middle_row, middle_col, center)
        if okay_one % 4 == 0:
            ans += flip_cnt_col + flip_cnt_row
        elif okay_one % 4 == 2:
            if flip_cnt_col + flip_cnt_row >= 2:
                ans += flip_cnt_col + flip_cnt_row
            else:
                ans += 2 - (flip_cnt_col + flip_cnt_row)
        else:
            raise f"data error okay_one={okay_one}"
        return ans
        

data = [[1],[1],[1],[0]]
r = Solution().minFlips(data)
print(r)