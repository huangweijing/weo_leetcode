from typing import List
from functools import reduce

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_num = (1 << maximumBit) - 1
        result = []
        xor_all = reduce(lambda a, b: a^b, nums)
        while len(nums) > 0:
            result.append(max_num ^ xor_all)
            xor_all ^= nums.pop()
        return result

data_nums = [0, 1, 1, 3]
data_maximumBit = 2
r = Solution().getMaximumXor(data_nums, data_maximumBit)
print(r)