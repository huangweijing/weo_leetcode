from typing import List


class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        in_range = dict[int, int]()
        out_range = dict[int, int]()
        if 0 <= start <= 1000:
            in_range[start] = 0
        else:
            out_range[start] = 0
        while len(in_range) > 0:
            new_in_range = dict[int, int]()
            for num in nums:
                


