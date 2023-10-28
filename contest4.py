from typing import List
from functools import cache


class Solution:
    def __init__(self):
        self.s = ""
        self.k = 0

    @cache
    def my_sol(self, cut_pos:int, cnt:int) -> int:
        pass

    def calc_sub(self, start: int, end: int) -> int:
        for d in range(1, end - start):
            

    def minimumChanges(self, s: str, k: int) -> int:
        self.s, self.k = s, k
        dp = [[0] * cut_pos for _ in range(cnt + 1)]


