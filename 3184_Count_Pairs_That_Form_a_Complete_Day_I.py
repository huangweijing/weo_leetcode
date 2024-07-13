from typing import List
from collections import Counter


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        day_cnt = Counter()
        ans = 0
        for hour in hours:
            ans += day_cnt[(24 - hour % 24) % 24]
            day_cnt[hour % 24] += 1
        return ans
