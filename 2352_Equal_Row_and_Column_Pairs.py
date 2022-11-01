from typing import List

class Solution:
    MOD = 900000001633
    BASE = 10 ** 5 + 1
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_arr, col_arr = [0] * len(grid), [0] * len(grid)
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                row_arr[i] = (row_arr[i] * Solution.BASE + col) % Solution.MOD
                col_arr[j] = (col_arr[j] * Solution.BASE + col) % Solution.MOD
        # print(row_arr, col_arr)
        ans = 0
        for row_sum in row_arr:
            for col_sum in col_arr:
                if row_sum == col_sum:
                    ans += 1
        return ans

data = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
r = Solution().equalPairs(data)
print(r)
