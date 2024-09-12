from typing import List
from sortedcontainers import SortedList


class Solution:
    def resultsArray(self, queries: List[List[int]], k: int) -> List[int]:
        ans = []
        arr = SortedList(key=lambda x: sum(map(abs, x)))
        for q in queries:
            arr.add(q)
            if len(arr) < k:
                ans.append(-1)
            else:
                ans.append(sum(map(abs, arr[k - 1])))
        return ans
