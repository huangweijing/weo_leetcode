from typing import List
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return [num for num in nums
               if cnt[num] == 1
               and num + 1 not in cnt
               and num - 1 not in cnt]

