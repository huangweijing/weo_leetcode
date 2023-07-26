from typing import List
from collections import defaultdict


class Solution:
    MODULO = 10 ** 9 + 7

    def countPaths(self, grid: List[List[int]]) -> int:
        dp = [[1] * len(grid[0]) for _ in range(len(grid))]
        axis_list = defaultdict(lambda : list[list[int]]())
        for i, row in enumerate(grid):
            for j, val in enumerate(grid[i]):
                axis_list[val].append([i, j])
        key_list = list(axis_list.keys())
        key_list.sort()
        offset_list = [
            [1, 0], [0, -1], [0, 1], [-1, 0]
        ]
        for key in key_list:
            for axis in axis_list[key]:
                # print(axis)
                for offset in offset_list:
                    row_idx = axis[0] + offset[0]
                    col_idx = axis[1] + offset[1]
                    # print(f"row_idx={row_idx}, col_idx={col_idx}")
                    if 0 <= row_idx < len(grid) and 0 <= col_idx < len(grid[0]):
                        if grid[row_idx][col_idx] < key:
                            dp[axis[0]][axis[1]] += dp[row_idx][col_idx] % Solution.MODULO
        # print(dp)
        ans = 0
        for row in dp:
            for val in row:
                ans += val
                ans %= Solution.MODULO
        return ans


data = [[1]]
r = Solution().countPaths(data)
print(r)

