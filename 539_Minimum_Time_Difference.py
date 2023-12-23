from typing import List


class Solution:
    def diff(self, t1: str, t2: str) -> int:
        t1_h, t1_m = int(t1[:2]), int(t1[3:])
        t2_h, t2_m = int(t2[:2]), int(t2[3:])
        t2_val = t2_h * 60 + t2_m
        t1_val = t1_h * 60 + t1_m
        return min(abs(t2_val - t1_val + 1440) % 1440
                   , abs(t1_val + 1440 - t2_val) % 1440)

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        ans = 1440
        for i in range(len(timePoints)):
            ans = min(ans, self.diff(timePoints[i - 1], timePoints[i]))
        return ans

