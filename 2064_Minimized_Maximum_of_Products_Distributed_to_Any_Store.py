from typing import List
import math


class Solution:
    def __init__(self) -> None:
        self.n = 0
        self.quantities = []
    
    def my_sol(self, store_size: int) -> bool:
        total_store_cnt = 0
        for q in self.quantities:
            total_store_cnt += math.ceil(q / store_size)
            if total_store_cnt > self.n:
                return False
        return True


    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        self.n, self.quantities = n, quantities
        left, right = 1, sum(quantities)
        mid = (left + right) >> 1
        while left < right:
            s1, s2 = self.my_sol(mid - 1), self.my_sol(mid)
            # print(s1, s2, left, right, mid)
            if not s1 and s2:
                return mid
            elif s1:
                right = mid - 1
            elif not s2:
                left = mid + 1
            mid = (left + right) >> 1
        return mid
    

data = [
    6
    , [11,6]
]
r = Solution().minimizedMaximum(* data)
print(r)