from typing import List
from functools import cache


class Solution:
    mod = 10 ** 9 + 7
    def __init__(self) -> None:
        self.pizza = []
        self.k = 0
        self.m, self.n = -1, -1

    @cache
    def cut_cnt(self, row_idx: int, col_idx: int, k: int) -> int:
        ret = 0
        for i in range(row_idx + 1, self.m):
            ret += self.cut_cnt(i, col_idx, k - 1)
            ret %= Solution.mod
        for i in range(row_idx + 1, self.n):
            self.cut_cnt(row_idx, i, k - 1)
            ret %= Solution.mod

    def ways(self, pizza: List[str], k: int) -> int:
        self.pizza = pizza
        self.k = k
        self.m, self.n = len(pizza), len(pizza[0])