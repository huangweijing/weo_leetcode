from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        candy_cnt = 0
        ans = 0
        while len(cost) > 0:
            ans += cost.pop()
            candy_cnt += 1
            if candy_cnt == 2:
                candy_cnt = 0
                if len(cost) > 0:
                    cost.pop()
        return ans





