from typing import List
from functools import cache
from collections import defaultdict
import math

class Solution:
    def __init__(self):
        self.arr = []
        self.jump = defaultdict(lambda : list[int]())

    @cache
    def my_sol(self, n):
        print(n)
        if n == 0:
            return 0
        sub1, sub2, sub3 = math.inf, math.inf, math.inf
        if n > 0:
            sub1 = self.my_sol(n - 1) + 1
        if n < len(self.arr) - 1:
            sub2 = self.my_sol(n + 1) + 1
        sub_sol = [self.my_sol(i) for i in self.jump[self.arr[n]] if i > n]
        if len(sub_sol) > 0:
            sub3 = min(sub_sol) + 1
        return min(sub1, sub2, sub3)

    def minJumps(self, arr: List[int]) -> int:
        self.arr = arr
        for i, num in enumerate(arr):
            self.jump[num].append(i)
        print(self.jump)
        return self.my_sol(len(arr) - 1)

r = Solution().minJumps([1, 7, 5, 7])
print(r)
