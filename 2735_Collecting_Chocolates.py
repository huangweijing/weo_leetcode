from typing import List
import math


class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = math.inf
        cost = 0
        for i in range(n):
            ans = min(ans, sum(nums) + cost)
            # print(nums, ans)
            new_nums = [0] * n
            for j in range(n):
                if j + 1 >= len(nums):
                    new_nums[j] = min(nums[j], nums[0])
                else:
                    new_nums[j] = min(nums[j], nums[j + 1])
            cost += x
            nums = new_nums
        return ans

data = [
    [1,2,3]
    , 5
]
r = Solution().minCost(* data)
print(r)
