from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        m = max(amount)
        s = sum(amount)
        return m if m >= s - m else (s & 1) + (s >> 1)





