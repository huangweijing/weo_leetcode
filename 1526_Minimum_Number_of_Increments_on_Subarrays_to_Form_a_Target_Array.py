from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # stk = []
        level = 0
        ans = 0
        for num in target:
            if num > level:
                ans += num - level
            level = num
        return ans