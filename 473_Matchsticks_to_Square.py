from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.avg_len = 0
        self.matchsticks = []

    def validate(self, matchsticks: List[int]):
        sum_all = sum(matchsticks)
        if sum_all % 4 != 0:
            return False
        self.avg_len = sum_all // 4
        for match in matchsticks:
            if match > self.avg_len:
                return False
        return True

    @cache
    def my_sol(self, remain_side: int, remain_length: int, sticks: int) -> bool:
        # print(f"my_sol({remain_side}, {remain_length}, {sticks})")
        # if remain_side == remain_length == sticks == 0:
        #     return True
        for i in range(sticks.bit_length()):
            if (sticks & (1 << i)) >> i == 1:
                # print(f"calc {i} stick_len={self.matchsticks[i]} ... ({remain_side}, {remain_length}, {sticks})")
                if self.matchsticks[i] == remain_length:
                    if remain_side == 1 and sticks ^ (1 << i) == 0:
                        return True
                    if self.my_sol(remain_side - 1, self.avg_len, sticks ^ (1 << i)):
                        return True
                elif self.matchsticks[i] <= remain_length:
                    if self.my_sol(remain_side, remain_length - self.matchsticks[i]
                            , sticks ^ (1 << i)):
                        return True
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        if not self.validate(matchsticks):
            return False
        self.matchsticks = matchsticks
        self.avg_len = sum(self.matchsticks) >> 2
        result = self.my_sol(4, self.avg_len, (1 << len(matchsticks)) - 1)
        return result


r = Solution().makesquare([1, 1, 2, 2, 1, 1])
print(r)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s1.union(s2)
# print(s1)