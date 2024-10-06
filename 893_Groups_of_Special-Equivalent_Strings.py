from typing import List
from collections import Counter


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        cnt_set = set[str]()
        for word in words:
            cnt0, cnt1 = Counter(), Counter()
            for i, ch in enumerate(word):
                if i & 1 == 0:
                    cnt0[ch] += 1
                else:
                    cnt1[ch] += 1
            key0, key1 = "", ""
            for k in sorted(cnt0.keys()):
                key0 += k + str(cnt0[k])
            for k in sorted(cnt1.keys()):
                key1 += k + str(cnt1[k])
            cnt_set.add(key0 + "," + key1)
        return len(cnt_set)

