from typing import List
from collections import deque


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -math.inf
        ans = deque([-1])
        for num in reversed(arr[1:]):
            max_num = max(num, max_num)
            ans.appendleft(max_num)
        return ans