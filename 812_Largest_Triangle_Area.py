import math
from typing import List

class Solution:
    def distance(self, p1: list[int], p2: list[int]):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def is_triangle(self, points:List[List[int]]):
        distance_arr = [0.0] * 3
        for i in range(len(points)):
            distance_arr[i] = self.distance(points[i], points[i-1])
        return distance_arr[0] + distance_arr[1] > distance_arr[2] \
        and distance_arr[0] + distance_arr[2] > distance_arr[1] \
        and distance_arr[1] + distance_arr[2] > distance_arr[0]


    def largestTriangleArea(self, points: List[List[int]]) -> float:
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    self.is_triangle([points[i], points[j], points[k]])

