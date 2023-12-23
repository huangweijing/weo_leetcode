from typing import List


class Solution:
    def __init__(self):
        self.sum_cand = 0
        self.candies = []
        self.k = 0

    def my_sol(self, pile_size: int) -> bool:
        pile_cnt = 0
        for cand in self.candies:
            pile_cnt += cand // pile_size
            if pile_cnt >= self.k:
                return True
        return False

    def maximumCandies(self, candies: List[int], k: int) -> int:
        self.sum_cand = sum(candies)
        self.candies = candies
        self.k = k
        left, right = 1, self.sum_cand // k + 1
        mid = left + right >> 1
        while left <= right:
            s1 = self.my_sol(mid)
            s2 = self.my_sol(mid + 1)
            if s1 and not s2:
                return mid
            elif not s1:
                right = mid - 1
            elif s2:
                left = mid + 1
            mid = left + right >> 1
        return 0
