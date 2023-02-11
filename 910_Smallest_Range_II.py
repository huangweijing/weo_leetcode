from typing import List
import math

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        nums_plus_k, nums_minus_k = [], []
        for num in nums:
            nums_plus_k.append(num + k)
            nums_minus_k.append(num - k)
        ans = math.inf
        for i in range(0, len(nums)):
            if i == len(nums) - 1:
                ans = min(ans, nums[-1] - nums[0])
            else:
                ans = min(ans, abs(max(nums[-1] - k, nums_plus_k[i]) -
                      min(nums[0] + k, nums_minus_k[i + 1])))
        return ans

data = [
    [7,8,8]
    , 5
]
r = Solution().smallestRangeII(* data)
print(r)