import math
from typing import List
from collections import deque


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] % k != 0:
                continue
            gcd_val = nums[i]
            if gcd_val == k:
                ans += 1
            for j in range(i + 1, len(nums)):
                if nums[j] % k != 0:
                    break
                if gcd_val != k:
                    gcd_val = math.gcd(gcd_val, nums[j])
                if gcd_val == k:
                    ans += 1
                # print(nums[i], nums[j], ans)
        return ans


data = [
    [9, 3, 1, 15, 21, 6, 3]
    , 3
]
r = Solution().subarrayGCD(*data)
print(r)



