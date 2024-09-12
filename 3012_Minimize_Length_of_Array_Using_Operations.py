import math
from typing import List
from collections import Counter


class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        min_num = min(nums)
        for key in cnt.keys():
            if key % min_num > 0:
                return 1
        return math.ceil(cnt[min_num] / 2)