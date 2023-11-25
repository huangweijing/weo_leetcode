from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = [0, 0]
        for num in nums:
            if num > ans[1]:
                ans[0] = ans[1]
                ans[1] = num
            elif num > ans[0]:
                ans[0] = num
        return (ans[0] - 1) * (ans[1] - 1)

