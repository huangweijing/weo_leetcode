from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i, h in enumerate(happiness):
            if i >= k:
                return ans
            ans += max(h - i, 0)
        return ans
