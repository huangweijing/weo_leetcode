from collections import deque
from typing import List
import math


class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        k_dividable = []
        k_dividable_len = [0] * len(nums)
        for num in nums:
            k_dividable.append(k % num == 0)
        for i, dv in enumerate(reversed(k_dividable)):
            if dv:
                if i > 0:
                    k_dividable_len[-1 - i] = k_dividable_len[-1 - (i - 1)] + 1
                else:
                    k_dividable_len[-1 - i] = 1
        ans = 0
        # print(k_dividable_len)
        for i, num in enumerate(nums):
            base = num
            idx = i
            while idx < len(nums) and k % base == 0:
                if k == base:
                    # print(i, idx, k_dividable_len[idx])
                    ans += k_dividable_len[idx]
                    break
                idx += 1
                if idx < len(nums):
                    base = math.lcm(base, nums[idx])
        return ans
    

data = [
    [5,1,1,1,2]
    , 1
]
r = Solution().subarrayLCM(* data)
print(r)
                

