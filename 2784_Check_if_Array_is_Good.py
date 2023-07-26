from typing import List
from collections import Counter

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        cnt = Counter(nums)
        # print(cnt, len(cnt))
        if len(cnt) != n:
            return False
        for i in range(1, n):
            if cnt[i] != 1:
                return False
        if cnt[n] == 2:
            return True

data = [1, 3, 3, 2]
r = Solution().isGood(data)
print(r)