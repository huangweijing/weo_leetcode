from typing import List


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points.sort()
        ans = 0
        max_rect_covered = -1
        for p in points:
            if p[0] > max_rect_covered:
                max_rect_covered = p[0] + w
                ans += 1
        return ans
