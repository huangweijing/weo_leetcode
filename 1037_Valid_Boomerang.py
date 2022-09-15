from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        slope1 = (points[0][0] - points[1][0], points[0][1] - points[1][1])
        slope2 = (points[1][0] - points[2][0], points[1][1] - points[2][1])
        return (slope1[0] * slope2[1]) != (slope1[1] * slope2[0])
