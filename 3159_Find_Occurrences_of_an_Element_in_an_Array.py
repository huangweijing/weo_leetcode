from typing import List
from collections import Counter


class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        ans = []
        idx_list = [i for i, num in enumerate(nums) if num == x]
        for q in queries:
            if len(idx_list) == 0 or q > len(idx_list):
                ans.append(-1)
            else:
                ans.append(idx_list[q - 1])
        return ans
