from typing import List

class Solution:

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key=lambda x: x[0])
        
        for i in range(len(rectangles), -1, -1):
            
