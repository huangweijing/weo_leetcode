from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = Counter(s)
        return cnt[letter] * 100 // len(s)
