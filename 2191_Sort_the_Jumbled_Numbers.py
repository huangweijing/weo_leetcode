from typing import List
from functools import reduce


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            val = reduce(lambda a, b: a * 10 + b
                         , map(lambda x: mapping[int(x)], str(num))) 
            arr.append([num, val, i])
        arr.sort(key=lambda x: (x[1], x[2]))
        return [num[0] for num in arr]

        