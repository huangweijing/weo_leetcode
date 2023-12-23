from typing import List
import math


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        prefix_sum = 0
        level = 0
        remain = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            new_level = math.floor((k + prefix_sum) / (i + 1))
            if new_level < num:
                break
            else:
                level = new_level
        for i, num in enumerate(nums):
            # print(nums[i], level)
            if nums[i] <= level:
                diff = level - nums[i]
                nums[i] += min(k, diff)
                k -= min(k, diff)
            else:
                break
        i = 0
        while k > 0:
            nums[i] += 1
            k -= 1
            i += 1
        # print(nums)
        ans = 1
        mod = 10 ** 9 + 7
        for i, num in enumerate(nums):
            ans = num * ans % mod
        return ans

data = [
    [24,5,64,53,26,38]
    , 54
]
r = Solution().maximumProduct(*data)
print(r)