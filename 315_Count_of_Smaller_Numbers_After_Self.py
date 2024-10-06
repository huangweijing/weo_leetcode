from typing import List
from sortedcontainers import SortedList
from collections import deque


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        ans = deque()
        for num in reversed(nums):
            idx = sl.bisect_left(num)
            ans.appendleft(idx)
            sl.add(num)
        return list(ans)

