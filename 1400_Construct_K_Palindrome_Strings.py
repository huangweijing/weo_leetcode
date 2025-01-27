from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cnt = Counter(s)
        single_cnt = len([v for v in cnt.values() if v & 1 == 1])
        return single_cnt <= k and len(s) >= k