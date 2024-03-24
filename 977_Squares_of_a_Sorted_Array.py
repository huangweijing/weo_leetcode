from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        q = deque(nums)
        ans = deque()
        while len(q) > 0:
            if abs(q[-1]) > abs(q[0]):
                ans.appendleft(q.pop() ** 2)
            else:
                ans.appendleft(q.popleft() ** 2)
        return ans
