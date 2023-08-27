from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        dp = {stone: set[int]() for stone in stones}
        dp[0].add(0)
        stone_set = set(stones)
        for stone in stones:
            unit_list = dp[stone]
            next_unit_set = set[int]()
            for unit in unit_list:
                if abs(stones[-1] - (unit + stone)) <= 1:
                    return True
                if unit - 1 > 0 and stone + unit - 1 in stone_set:
                    next_unit_set.add(unit - 1)
                if stone + unit in stone_set:
                    next_unit_set.add(unit)
                if stone + unit + 1 in stone_set:
                    next_unit_set.add(unit + 1)
            for unit in next_unit_set:
                dp[stone + unit].add(unit)
        return False

data = [0,1,2,3,4,8,9,11]
r = Solution().canCross(data)
print(r)


