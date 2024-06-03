from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        max_end = 1
        ans = 0
        for m in meetings:
            if m[0] - 1 >= max_end:
                ans += m[0] - 1 - max_end
            max_end = max(m[1], max_end)
        ans += days - max_end
        return ans

