from typing import List
from collections import Counter


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        node_cnt = Counter()
        for road in roads:
            node_cnt[road[0]] += 1
            node_cnt[road[1]] += 1
        val_sorted = sorted([val for key, val in node_cnt.items()])
        sum_val = 0
        for i in range(n, -1, -1):
            val = val_sorted.pop()
            sum_val += val * i
            if len(val_sorted) == 0:
                break
        return sum_val


data = [
    5
    , [[0, 3], [2, 4], [1, 3]]
]
r = Solution().maximumImportance(* data)
print(r)


