from typing import List
from collections import Counter


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
        cnt = Counter(nums1) + Counter(nums2) + Counter(nums3)
        return [key for key, val in cnt.items() if val >= 2]


data = [
    [1,1,3,2]
    , [1, 2,3]
    , [3]
]
r = Solution().twoOutOfThree(*data)
print(r)
