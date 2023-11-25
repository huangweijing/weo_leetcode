import math
from typing import List


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        last_rung = 0
        ans = 0
        for rung in rungs:
            ans += math.ceil((rung - last_rung) / dist) - 1
            last_rung = rung
        return ans

data = [
    [4]
    , 2
]
r = Solution().addRungs(* data)
print(r)

