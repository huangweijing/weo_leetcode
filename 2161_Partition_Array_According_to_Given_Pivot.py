from typing import List
from collections import deque

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        arr1 = deque()
        arr2 = deque()
        pivot_cnt = 0
        for num in nums:
            if num < pivot:
                arr1.append(num)
            elif num == pivot:
                pivot_cnt += 1
            else:
                arr2.append(num)
        arr1.extend([pivot] * pivot_cnt)
        arr1.extend(arr2)
        return arr1
