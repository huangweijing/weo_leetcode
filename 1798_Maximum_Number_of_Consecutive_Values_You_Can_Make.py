from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        max_expressable = 0
        for coin in coins:
            if coin > max_expressable + 1:
                break
            max_expressable += coin
        return max_expressable + 1