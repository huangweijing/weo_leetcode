import math
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = [-math.inf, -1]
        sec_num = [-math.inf, -1]
        for i, n in enumerate(nums):
            if n > max_num[0]:
                sec_num = max_num
                max_num = [n, i]
            elif n > sec_num[0]:
                sec_num = [n, i]

        if max_num[0] >= sec_num[0] * 2:
            return max_num[1]
        else:
            return -1

data_nums = [1,2,5,9,4]
r = Solution().dominantIndex(data_nums)
print(r)

