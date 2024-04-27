from typing import List
import math


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return grid[0][0]
        row_arr = [[i, val] for i, val in enumerate(grid[0])]
        row_arr.sort(key=lambda x: x[1])
        # print(row_arr)
        first, second = row_arr[0], row_arr[1]
        for i in range(1, len(grid)):
            row_arr = [0] * len(grid)
            for j, val in enumerate(grid[i]):
                if first[0] == j:
                    row_arr[j] = second[1] + val
                else:
                    row_arr[j] = first[1] + val
            row_arr = sorted(enumerate(row_arr), key=lambda x: x[1])
            new_first, new_second = row_arr[0], row_arr[1]
            first, second = new_first, new_second
        return first[1]


data = [[1,99,99]
        ,[0,2,1]
        ,[99,99,4]]
r = Solution().minFallingPathSum(data)
print(r)