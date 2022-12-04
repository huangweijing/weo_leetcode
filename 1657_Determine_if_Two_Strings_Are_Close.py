from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cnt1, cnt2 = Counter(word1), Counter(word2)
        cnt1_val, cnt2_val = list(cnt1.values()), list(cnt2.values())
        cnt1_val.sort()
        cnt2_val.sort()
        return cnt1_val == cnt2_val and cnt1.keys() == cnt2.keys()