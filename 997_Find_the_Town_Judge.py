from typing import List
from collections import Counter

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        cnt = Counter()
        cnt_from = Counter()
        for t in trust:
            cnt[t[1]] += 1
            cnt_from[t[0]] += 1
        if len(cnt) == 0:
            return -1
        cmn = cnt.most_common(1)[0]
        if cmn[1] == n - 1 and cnt_from[cmn[0]] == 0:
            return cmn[0]
        return -1

data = [
    1
    , [[]]
]
r = Solution().findJudge(* data)
print(r)