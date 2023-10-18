from typing import List
import math

class Solution:

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min_val, max_val = math.inf, -math.inf
        min_idx, max_idx = -1, -1
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < min_val:
                min_val = nums[i - indexDifference]
                min_idx = i - indexDifference
            if nums[i - indexDifference] > max_val:
                max_val = nums[i - indexDifference]
                max_idx = i - indexDifference
            if abs(nums[i] - min_val) >= valueDifference:
                return [min_idx, i]
            if abs(nums[i] - max_val) >= valueDifference:
                return [max_idx, i]
        return [-1, -1]


data = [
    # [5,1,4,1]
    [4, 3, 8, 6, 2, 8]
    , 2
    , 3
]
r = Solution().findIndices(*data)
print(r)

# arr = [
#     1, 4, 7, 9
# ]
# r = bisect.bisect_left(arr, 7, hi=3)
# print(r)
