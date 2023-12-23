import itertools
import random
from typing import List
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.prob = []
        self.w = list(itertools.accumulate(w))
        self.sum_w = self.w[-1]

    def pickIndex(self) -> int:
        rit = random.randint(1, self.sum_w)
        i = bisect.bisect_left(self.w, rit)
        return i

data = [1, 3, 2]
s = Solution(data)
print(s.pickIndex())



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()