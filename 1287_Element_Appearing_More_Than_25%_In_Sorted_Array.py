import bisect
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in (0, n // 4, 2 * n // 4, 3 * n // 4):
            left = bisect.bisect_left(arr, arr[i])
            right = bisect.bisect_right(arr, arr[i])
            if right - left > n / 4:
                return arr[i]
        return -1
