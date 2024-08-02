from typing import List


class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        arr = []
        for i, w in enumerate(weights[:-1]):
            arr.append(w + weights[i + 1])
        arr.sort()
        return sum(arr[-(k - 1): ]) - sum(arr[: k - 1])
        