from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        s1_cnt_odd = Counter()
        s1_cnt_eve = Counter()
        s2_cnt_odd = Counter()
        s2_cnt_eve = Counter()
        for i, ch in enumerate(s1):
            if i & 1 == 1:
                s1_cnt_odd[ch] += 1
            else:
                s1_cnt_eve[ch] += 1

        for i, ch in enumerate(s2):
            if i & 1 == 1:
                s2_cnt_odd[ch] += 1
            else:
                s2_cnt_eve[ch] += 1

        return s1_cnt_odd == s2_cnt_odd and s1_cnt_eve == s2_cnt_eve