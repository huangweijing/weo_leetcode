from typing import List

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum_all = 0
        cnt = 0
        for num in nums:
            if num % 6 == 0:
                cnt += 1
                sum_all += num
        if cnt == 0:
            return 0
        return sum_all // cnt

