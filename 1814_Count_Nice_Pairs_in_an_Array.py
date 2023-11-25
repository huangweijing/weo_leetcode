from typing import List
from collections import Counter


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = Counter()
        ans = 0
        for num in nums:
            key = num - int(str(num)[::-1])
            ans += cnt[key]
            cnt[key] += 1
        return ans % (10 ** 9 + 7)

