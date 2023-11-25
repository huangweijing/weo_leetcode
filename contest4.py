from typing import List
from functools import cache
import bisect


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i, num in enumerate(nums):
            idx = bisect.bisect_right(nums, num * 2) - 1
            print("bisect", num, nums[idx])
            if idx == i:
                continue
            # print(i, idx)
            base = 0
            for j in reversed(range(21)):
                bit = (num & (1 << j))
                k1 = bisect.bisect_left(nums, base)
                k2 = bisect.bisect_left(nums, base + (1 << j))
                if bit == 0:
                    if k2 <= idx:
                        ans = max(ans, num ^ nums[k2])
                        base = base + (1 << j)
                    else:
                        ans = max(ans, num ^ nums[k1])
                else:
                    if k1 <= idx:
                        ans = max(ans, num ^ nums[k1])
                        base = base + (nums[k1] & (1 << j))
            print(num, bin(num), base)
        return ans

data = [500,520,2500,3000]
# print(500 ^ 2500)
print(list(map(bin, data)))
r = Solution().maximumStrongPairXor(data)
print(r)