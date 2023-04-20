from typing import List
from collections import defaultdict

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        num_dict = dict[int, int]()
        for i, row in enumerate(mat):
            row_sum = sum(row)
            if row_sum not in num_dict:
                num_dict[row_sum] = [i, row_sum]
        keys = list(num_dict.keys())
        keys.sort(reverse=True)
        return num_dict[keys[0]]

mat = [[0,0,0],[0,1,1]]
r = Solution().rowAndMaximumOnes(mat)
print(r)