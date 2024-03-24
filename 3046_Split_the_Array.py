from typing import List
from collections import Counter


class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        cnt = Counter()
        for num in nums:
            cnt[num] += 1
            if cnt[num] > 2:
                return False
        return True
