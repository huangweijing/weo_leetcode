from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for key, val in cnt.items():
            if key == val:
                ans = max(ans, key)
        return ans

