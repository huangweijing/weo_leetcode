class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        covered_area = 0
        if ax1 < bx2 and ax2 > bx1 and ay1 < by2 and ay2 > by1:
            covered_area_width = (ax2 - ax1) + (bx2 - bx1) - (max(ax2, bx2) - min(ax1, bx1))
            covered_area_height = (ay2 - ay1) + (by2 - by1) - (max(ay2, by2) - min(ay1, by1))
            covered_area = covered_area_height * covered_area_width
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - covered_area
