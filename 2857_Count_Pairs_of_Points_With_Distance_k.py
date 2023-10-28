from typing import List
from collections import Counter


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        cnt = Counter()
        ans = 0
        for c in coordinates:
            print(cnt)
            print(c, c[0] ^ c[1], c[0] ^ c[1] ^ k)
            ans += cnt[c[0] ^ c[1] ^ k]
            cnt[c[0] ^ c[1]] += 1
        return ans


data = [
    [[27,94],[61,68],[47,0],[100,4],[127,89],[61,103],[26,4],[51,54],[91,26],[98,23],[80,74],[19,93]]
    , 95]
r = Solution().countPairs(* data)
print(r)