from typing import List

class Solution:
    def maxJump(self, stones: List[int]) -> int:
        ans = 0
        last_stone = 0
        for i in range(1, len(stones), 2):
            ans = max(ans, stones[i] - last_stone)
            last_stone = stones[i]
        last_stone = 0
        for i in range(0, len(stones), 2):
            ans = max(ans, stones[i] - last_stone)
            last_stone = stones[i]
        return ans


