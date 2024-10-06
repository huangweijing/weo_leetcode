from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        g1, g2 = 0, 0
        for num in nums:
            if num < 10:
                g1 += num
            else:
                g2 += num
        return g1 != g2

