from typing import List
from collections import Counter


class WeoST:
    def __init__(self):
        self.cache = Counter()

    def get_max(self, start: int, end: int
                , left: int, right: int) -> int:
        if start > right or end < left:
            return -1
        if (left, right) in self.cache:
            return self.cache[(left, right)]

        mid = left + right >> 1
        if start <= left and end >= right:
            m1 = self.get_max(start, end, left, mid)
            m2 = self.get_max(start, end, mid + 1, right)
            self.cache[(left, mid)] = m1
            self.cache[(mid + 1, right)] = m2
            return max(m1, m2)
        else:
            m1 = self.get_max(start, end, left, mid)
            m2 = self.get_max(start, end, mid + 1, right)
            return max(m1, m2)


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = [0]
        for num in nums:
            pre_xor.append(pre_xor[-1] ^ num)


ws = WeoST()
for i in range(10):
    ws.cache[(i, i)] = i * i * pow(-1, i)
t = ws.get_max(2, 7, 0, 9)
print(ws.cache)
print(t)