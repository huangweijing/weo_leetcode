from typing import List


class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        cur = bottom - 1
        ans = 0
        for s in special:
            ans = max(s - cur - 1, ans)
            cur = s
        ans = max(top - cur, ans)
        return ans
