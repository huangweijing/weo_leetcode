import math


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        i = int(math.sqrt(area))
        while i > 0:
            if area % i != 0:
                i -= 1
                continue
            return [int(area / i), i]
