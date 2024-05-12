import functools
import operator
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return (functools.reduce(operator.xor, nums) ^ k).bit_count()
