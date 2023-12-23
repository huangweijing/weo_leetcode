from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        val_set = set(range(1, len(grid) ** 2 + 1))
        ans = [-1, -1]
        for row in grid:
            for val in row:
                if val in val_set:
                    val_set.remove(val)
                else:
                    ans[0] = val
        ans[1] = val_set.pop()
        return ans


