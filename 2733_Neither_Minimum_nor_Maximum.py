from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        num_set = set[int]()
        for num in nums:
            num_set.add(num)
            if len(num_set) >= 3:
                num_list = list(num_set)
                num_list.sort()
                return list(num_set)[1]
        return -1
