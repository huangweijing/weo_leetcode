from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)
        cnt = Counter()
        ans = []
        for i in range(len(s) - len(p) + 1):
            if i == 0:
                cnt = Counter(s[:len(p)])
            else:
                cnt[s[i - 1]] -= 1
                cnt[s[i + len(p) - 1]] += 1
            if cnt_p == cnt:
                ans.append(i)
        return ans

