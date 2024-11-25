from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = 10e9
        for num in nums:
            ans = min(ans, sum([int(dig) for dig in str(num)]))
        return ans
        