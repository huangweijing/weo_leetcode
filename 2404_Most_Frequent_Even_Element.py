from typing import List
from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = Counter()
        for num in nums:
            if num & 1 == 0:
                cnt[num] += 1
        if len(cnt) == 0:
            return -1
        freq = cnt.most_common(1).pop()[1]
        ans = math.inf
        for num, f in cnt.items():
            if f == freq:
                ans = min(ans, num)
        return ans
