import bisect
import math
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ksqrt = math.ceil(math.sqrt(k)) - 1
        pivot = matrix[ksqrt][ksqrt]
        list_to_sort = list[int]()
        for row in matrix:
            i = bisect.bisect_right(row, pivot)
            list_to_sort.extend(row[:i])
            # print(row[:i], pivot)
        list_to_sort.sort()

        return list_to_sort[k - 1]

# r = Solution().kthSmallest([[1]], 1)
r = Solution().kthSmallest([[1, 2],[1, 3]], 4)
# r = Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 3)
# r = Solution().kthSmallest([[1,3,5],[6,7,12],[11,14,14]], 3)
print(r)
