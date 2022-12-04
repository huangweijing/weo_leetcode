import math
from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        return int(math.sqrt(2 * len(grades) + 1 / 4) - 1 / 2)

r = Solution().maximumGroups([8,8])
print(r)
