from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        sum_all = 0
        ans = 0
        for i in range(1, n + 1):
            if i not in banned:
                if sum_all + i <= maxSum:
                    sum_all += i
                    ans += 1
        return ans