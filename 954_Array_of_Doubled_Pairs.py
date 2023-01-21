from typing import List
from sortedcontainers import SortedList

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr = SortedList(arr)
        while len(arr) > 0:
            num = arr.pop()
            if num >= 0:
                if num & 1 == 1:
                    return False
                elif num >> 1 in arr:
                    arr.remove(num >> 1)
                else:
                    return False
            else:
                if num << 1 in arr:
                    arr.remove(num << 1)
                else:
                    return False

        return True
