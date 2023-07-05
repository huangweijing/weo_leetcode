from typing import List
import math
from collections import Counter

class Solution:
    def __init__(self):
        self.min_unfairness = math.inf
        self.cookies = []
        self.k = 0

    def my_sol(self, dis_cnt: Counter, start_idx: int):
        if start_idx == len(self.cookies):
            self.min_unfairness = min(max(dis_cnt.values()), self.min_unfairness)
            return
        cookie = self.cookies[start_idx]
        for j in range(min(self.k, start_idx + 1)):
            dis_cnt[j] += cookie
            self.my_sol(dis_cnt, start_idx + 1)
            dis_cnt[j] -= cookie

    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.cookies = cookies
        self.k = k
        self.my_sol(Counter(), 0)
        return int(self.min_unfairness)


data = [
    [6, 1, 3, 2, 2, 4, 1, 2]
    , 8
]
r = Solution().distributeCookies(* data)
print(r)