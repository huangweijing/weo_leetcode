from typing import List
from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = deque(range(1, m + 1))
        result = []
        for query in queries:
            idx = arr.index(query)
            val = arr[idx]
            del arr[idx]
            arr.appendleft(val)
            result.append(idx)
        return result
