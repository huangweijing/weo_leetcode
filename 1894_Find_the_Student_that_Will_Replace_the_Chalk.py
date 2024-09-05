from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        k = k % sum_chalk
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k = k - c
        return -1

        