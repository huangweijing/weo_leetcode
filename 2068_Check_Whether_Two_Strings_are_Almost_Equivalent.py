from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        for i in range(ord('a'), ord('z') + 1):
            diff = abs(cnt1[chr(i)] - cnt2[chr(i)])
            if diff > 3:
                return False
        return True
