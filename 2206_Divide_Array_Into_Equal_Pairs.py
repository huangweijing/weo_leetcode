from typing import List
from collections import Counter


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)
        for val in cnt.values():
            if val & 1 == 1:
                return False
        return True

