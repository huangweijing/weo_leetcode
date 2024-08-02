from typing import List
import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        stone_sum = sum(stones)
        dp = set[int]()
        for stone in stones:
            to_add = set[int]()
            for val in dp:
                if stone + val <= stone_sum >> 1:
                    to_add.add(stone + val)
            if stone <= stone_sum >> 1:
                to_add.add(stone)
            for val in to_add:
                dp.add(val)
        ans = math.inf
        for val in dp:
            ans = min(ans, stone_sum - (val << 1))
        return ans


data = [1]
r = Solution().lastStoneWeightII(data)
print(r)