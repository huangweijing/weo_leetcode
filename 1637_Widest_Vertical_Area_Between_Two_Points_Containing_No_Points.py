from typing import List

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        result = -math.inf
        for i in range(1, len(points)):
            distance = points[i][0] - points[i - 1][0]
            result = max(distance, result)
        return result