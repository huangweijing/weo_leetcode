from typing import List
from collections import deque, defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        diagonal_dict = defaultdict(lambda : deque())
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                x = i + j
                diagonal_dict[x].appendleft(val)

        keys = list(diagonal_dict.keys())
        keys.sort()
        for key in keys:
            row = diagonal_dict[key]
            for val in row:
                ans.append(val)
        return ans


data_nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
r = Solution().findDiagonalOrder(data_nums)
print(r)
