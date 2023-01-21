from typing import List
from sortedcontainers import SortedList

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        point_list = [[point[0] ** 2 + point[1] ** 2, point] for point in points]
        point_list.sort(key=lambda x: x[0])
        return [point[1] for point in point_list[: k]]