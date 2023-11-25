from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        level = 0
        for num in arr:
            if num > level:
                level += 1
        return level

