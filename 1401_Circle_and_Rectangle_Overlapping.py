class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int
                     , x1: int, y1: int, x2: int, y2: int) -> bool:
        dist = ((x1 + x2) // 2 - xCenter) ** 2 + ((y1 + y2) // 2 - yCenter) ** 2
