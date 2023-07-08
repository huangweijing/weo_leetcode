from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(grid[0])):
            max_len = 0
            for j in range(len(grid)):
                max_len = max(len(str(grid[j][i])), max_len)
            ans.append(max_len)
        return ans