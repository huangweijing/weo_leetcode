from typing import List
from collections import Counter


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        ans = 0
        cnt = Counter()
        for c in coordinates:
            for i in range(k + 1):
                x, y = i, k - i
                x2, y2 = c[0] ^ x, c[1] ^ y
                ans += cnt[(x2, y2)]
            cnt[(c[0], c[1])] += 1
        return ans


data = [
    [[27,94],[61,68],[47,0],[100,4],[127,89],[61,103],[26,4],[51,54],[91,26],[98,23],[80,74],[19,93]]
    , 95]
r = Solution().countPairs(* data)
print(r)

print(Counter([(1,2), (3, 4)]))