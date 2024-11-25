from typing import List
from collections import Counter


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        inc_dec_dict = Counter()
        for query in queries:
            inc_dec_dict[query[0]] += 1
            inc_dec_dict[query[1] + 1] -= 1
        # print(inc_dec_dict)
        height = 0
        for i, num in enumerate(nums):
            if i in inc_dec_dict:
                height += inc_dec_dict[i]
            # print(height, num)
            if height < num:
                return False
        return True


data = [
    [1,0,1]
    , [[0,2]]
]
r = Solution().isZeroArray(*data)
print(r)