from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                if i * j % k == 0 and num == num2:
                    ans += 1
        return ans

