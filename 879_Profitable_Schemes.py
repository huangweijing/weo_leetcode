from typing import List
from functools import cache

mod = 10 ** 9 + 7
class Solution:
    def __init__(self) -> None:
        self.group = []
        self.profit = []

    @cache
    def my_sol(self, n: int, min_profit: int, idx: int) -> int:
        # print(f"min_profit={min_profit}, idx={idx}")
        if min_profit <= 0:
            ret = 1
        else:
            ret = 0
        for i in range(idx, len(self.group)):
            if n < self.group[i]:
                break
            remain_profit = max(0, min_profit - self.profit[i])
            ret = (ret + self.my_sol(n - self.group[i], remain_profit, i + 1)) % mod
        return ret


    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        arr = list(sorted(zip(group, profit)))
        self.group, self.profit = [a[0] for a in arr], [a[1] for a in arr]
        return self.my_sol(n, minProfit, 0)
    

data = [
    100
    , 100
    , [10,4,3,1,6,10,7,7,4,11,20,5,13,1,27,21,1,3,1,1,1,30,7,6,5,27,39,6,18,25,4,14,2,3,6,2,11,3,3,8,3,13,10,3,20,34,5,48,1,3,8,41,2,1,1,1,1,19,59,2,20,18,15,1,5,10,16,28,4,6,1,2,1,8,15,6,5,3,18,11,11,7,34,10,1,26,1,13,7,1,9,6,37,1,32,1,9,1,1,8]
    , [9,10,0,17,22,9,1,16,12,0,8,1,12,2,5,1,0,2,12,0,18,0,11,0,3,14,0,9,0,6,0,12,1,17,19,7,56,28,1,4,4,3,24,4,6,1,6,10,1,1,0,2,1,13,1,6,6,9,43,6,1,0,5,10,2,7,31,8,3,2,3,34,7,13,4,2,1,9,13,7,9,7,15,2,10,8,3,5,3,21,22,16,1,0,0,0,1,1,1,18]
]
import time
start = time.time()
r = Solution().profitableSchemes(*data)
print(r)
print(time.time() - start)

        
        