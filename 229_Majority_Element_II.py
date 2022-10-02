from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        num_cnt = Counter(nums)
        result = []
        for key, val in num_cnt.items():
            if val > len(nums) / 3:
                result.append(key)
        return result
