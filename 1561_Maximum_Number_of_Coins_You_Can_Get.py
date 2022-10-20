from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        start = len(piles) // 3
        ans = 0
        for i in range(start, len(piles), 2):
            ans += piles[i]
        return ans

