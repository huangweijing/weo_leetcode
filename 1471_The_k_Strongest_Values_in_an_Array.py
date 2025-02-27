from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        arr.sort()
        mid = arr[(n - 1) >> 1]
        arr.sort(key=lambda x: [abs(x - mid), x], reverse=True)
        return arr[: k]