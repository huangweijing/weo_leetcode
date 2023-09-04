import math
from typing import List
from sortedcontainers import SortedList


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        sl = SortedList(gifts)
        for i in range(k):
            gift = sl.pop(-1)
            left = math.floor(math.sqrt(gift))
            sl.add(left)
        return sum(sl)


