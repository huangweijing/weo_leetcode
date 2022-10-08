from typing import List
from functools import cache
import math

class Solution:
    def __init__(self):
        self.arr = []

    @cache
    def my_mct(self, left: int, right: int) -> (int, int):
        arr = self.arr[left: right]
        if len(arr) == 1:
            return arr[0], 0
        r_max = 0
        r_sum = math.inf
        for i in range(1, len(arr)):
            max1, sum1 = self.my_mct(left, left+i)
            max2, sum2 = self.my_mct(left+i, right)
            if r_sum > sum1 + sum2 + max1 * max2:
                r_sum = sum1 + sum2 + max1 * max2
                r_max = max(max1, max2)
        return r_max,r_sum

    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.arr = arr
        r_max, r_sum = self.my_mct(0, len(arr))
        return r_sum

data_arr = [6,2,4]
r = Solution().mctFromLeafValues(data_arr)
print(r)