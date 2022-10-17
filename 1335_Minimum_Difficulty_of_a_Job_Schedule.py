import math
from functools import cache
from typing import List

class Solution:
    def __init__(self):
        self.jd = []

    @cache
    def my_sol(self, jd_len:int, d: int) -> int:
        if d == 1:
            return max(self.jd[: jd_len])

        result = math.inf
        for i in range(d - 1, jd_len):
            result = min(self.my_sol(i, d - 1) + max(self.jd[i: jd_len]), result)
        return result

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        self.jd = jobDifficulty
        return self.my_sol(len(jobDifficulty), d)

data = [[9, 9, 9]
,4]
r = Solution().minDifficulty(* data)
print(r)