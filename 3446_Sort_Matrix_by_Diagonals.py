from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        for i in range(len(grid)):
            stk = []
            row_idx, col_idx = i, 0
            while row_idx < len(grid):
                stk.append(grid[row_idx][col_idx])
                row_idx += 1
                col_idx += 1
            stk.sort()
            row_idx, col_idx = i, 0
            while row_idx < len(grid):
                grid[row_idx][col_idx] = stk.pop()
                row_idx += 1
                col_idx += 1
        
        for i in range(1, len(grid)):
            stk = []
            row_idx, col_idx = 0, i
            while col_idx < len(grid):
                stk.append(grid[row_idx][col_idx])
                row_idx += 1
                col_idx += 1
            stk.sort(reverse=True)
            row_idx, col_idx = 0, i
            while col_idx < len(grid):
                grid[row_idx][col_idx] = stk.pop()
                row_idx += 1
                col_idx += 1
        return grid
    

data = [[1,2,5,0],
        [3,4,0,4],
        [4,1,0,0],
        [4,2,4,1]]
r = Solution().sortMatrix(data)
print(r)


