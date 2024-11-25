from collections import Counter
from math import comb


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        cnt = Counter(s)
        return comb(cnt[c], 2) + cnt[c]
