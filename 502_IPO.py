from typing import List
import heapq
from sortedcontainers import SortedList


class CapitalProject:
    def __init__(self, profit: int, capital: int):
        self.profit = profit
        self.capital = capital

    def __lt__(self, other):
        if self.capital < other.capital:
            return True
        return False

    def __str__(self):
        return f"<{self.capital}, {self.profit}>"

class ProfitProject:
    def __init__(self, profit: int, capital: int):
        self.profit = profit
        self.capital = capital

    def __lt__(self, other):
        if self.profit > other.profit:
            return True
        return False

    def __str__(self):
        return f"<{self.capital}, {self.profit}>"


class Solution:
    def findMaximizedCapital(self, k: int, w: int
                             , profits: List[int], capital: List[int]) -> int:
        heap_profit, heap_capital = [], []
        for i in range(len(profits)):
            proj = CapitalProject(profit=profits[i], capital=capital[i])
            heapq.heappush(heap_capital, proj)
        ans = w
        cnt = 0
        while cnt < k:
            # print(list(map(str, heap_capital)))
            while len(heap_capital) > 0 and heap_capital[0].capital <= ans:
                proj = heapq.heappop(heap_capital)
                heapq.heappush(heap_profit,
                               ProfitProject(profit=proj.profit, capital=proj.capital))
            # print(list(map(str, heap_profit)))
            if len(heap_profit) == 0:
                break
            did_proj = heapq.heappop(heap_profit)
            # print(did_proj)
            ans += did_proj.profit
            cnt += 1
        return ans


data = [
    1
    , 2
    , [1, 2, 3]
    , [1, 1, 2]
]
r = Solution().findMaximizedCapital(*data)
print(r)


