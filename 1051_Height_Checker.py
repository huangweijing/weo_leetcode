from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights.copy()
        sorted_heights.sort()
        result = 0
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                result += 1
        return result
