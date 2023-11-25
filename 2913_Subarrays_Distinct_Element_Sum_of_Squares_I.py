from typing import List
from collections import Counter


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            num_set = set[int]()
            for j, num2 in enumerate(nums[i: ], start=i):
                num_set.add(num2)
                ans += len(num_set) ** 2

        return ans


data = [[2,2,5,5]]
r = Solution().sumCounts(* data)
print(r)