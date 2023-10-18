from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for val in cnt.values():
            if val == 1:
                return -1
            else:
                mod3 = val % 3
                if mod3 == 0:
                    ans += val // 3
                elif mod3 == 1:
                    ans += 2 + (val - 4) // 3
                elif mod3 == 2:
                    ans += 1 + (val - 2) // 3
        return ans
