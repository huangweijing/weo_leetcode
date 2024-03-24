from typing import List
from itertools import accumulate
import bisect


class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        acc_cap = list(accumulate(capacity))
        sum_apple = sum(apple)
        idx = bisect.bisect_left(acc_cap, sum_apple)
        return idx + 1