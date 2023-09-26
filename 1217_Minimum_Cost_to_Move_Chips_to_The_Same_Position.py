from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even, odd = 0, 0
        for i, pos in enumerate(position):
            if pos & 1 == 0:
                even += 1
            else:
                odd += 1
        return min(even, odd)
