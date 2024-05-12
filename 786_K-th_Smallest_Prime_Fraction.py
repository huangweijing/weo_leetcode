from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        l = []
        for i, num in enumerate(arr):
            for j in range(i + 1, len(arr)):
                l.append([num, arr[j]])
        l.sort(key=lambda x: x[0] / x[1])
        return l[k - 1]
