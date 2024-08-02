from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        ans = len(s)
        for key, val in cnt.items():
            ans -= ((val - 1) >> 1) << 1
        return ans