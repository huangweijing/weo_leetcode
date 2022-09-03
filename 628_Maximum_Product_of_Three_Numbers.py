import math
from typing import List
from sortedcontainers import SortedList

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max3 = SortedList(key=lambda x: -x)
        min3 = SortedList()
        for num in nums:
            max3.add(num)
            min3.add(num)
            if len(max3) > 3:
                max3.pop()
            if len(min3) > 3:
                min3.pop()
        return max(max3[0] * max3[1] * max3[2]
                   , max3[0] * min3[0] * min3[1])

data = [-4, -2, -1, 5]
r = Solution().maximumProduct(data)
print(r)
