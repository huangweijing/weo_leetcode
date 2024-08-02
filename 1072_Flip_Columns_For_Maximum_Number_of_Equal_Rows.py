from typing import List
from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for row in matrix:
            key1 = "".join(map(str, row))
            key2 = "".join(map(lambda x: str(1 - x), row))
            cnt[key1] += 1
            cnt[key2] += 1
        return max(cnt.values())

        