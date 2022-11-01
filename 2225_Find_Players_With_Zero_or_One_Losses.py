from typing import List
from collections import Counter

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        cnt = Counter()
        for match in matches:
            cnt[match[0]] += 0
            cnt[match[1]] += 1

        for key, val in cnt.items():
            if val == 0:
                ans[0].append(key)
            if val == 1:
                ans[1].append(key)
        ans[0].sort()
        ans[1].sort()
        return ans

