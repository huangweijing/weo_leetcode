from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        idx = 0
        while True:
            is_okay = True
            for i in range(len(grid)):
                if i != idx:
                    if grid[idx][i] == 0:
                        is_okay = False
                        idx = i
                        break
            if is_okay:
                return idx
