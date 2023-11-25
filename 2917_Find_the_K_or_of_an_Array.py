from typing import List
from collections import Counter


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        for i in range(32):
            for num in nums:
                if (num & (1 << i)) >> i == 1:
                    cnt[1 << i] += 1
        ans = 0
        for key, val in cnt.items():
            if val >= k:
                ans += key
        return ans