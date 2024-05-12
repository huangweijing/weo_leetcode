from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre_sum = 0
        min_pre_sum = math.inf
        for num in nums:
            pre_sum += num
            min_pre_sum = min(min_pre_sum, pre_sum)
        return max(1 - min_pre_sum, 1)
