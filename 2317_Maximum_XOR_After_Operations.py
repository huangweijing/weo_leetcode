from functools import reduce
from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a | b, nums)
