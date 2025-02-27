from typing import List
import math
from functools import cache

mod = 10 ** 9 + 7

class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            comb_val_1, comb_val_2 = 1, 1
            for j in range(k):
                if i + j >= len(nums):
                    break
                # ans += num * math.comb(len(nums) - i - 1, j)
                ans += num * comb_val_1
                ans %= mod
                comb_val_1 = comb_val_1 * (len(nums) - i - 1 - j) // (j + 1)
                # print(num, len(nums) - i - 1, j)
            for j in range(k):
                if i - j < 0:
                    break
                # ans += num * math.comb(i, j)
                ans += num * comb_val_2
                ans %= mod
                comb_val_2 = comb_val_2 * (i - j) // (j + 1)
                # print(num, i, j)
        return ans

data = [
    [1,2,3,4]
    , 3
]
r = Solution().minMaxSums(*data)
print(r)