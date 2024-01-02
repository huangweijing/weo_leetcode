from typing import List
from collections import Counter


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_num = 0
        cnt = Counter()
        cnt[0] = 1
        ans = 0
        for num in nums:
            if num & 1 == 1:
                odd_num += 1
            ans += cnt[odd_num - k]
            cnt[odd_num] += 1
        return ans