from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_all, sum_dig = 0, 0
        for num in nums:
            dig_sum = 0
            str_num = str(num)
            for ch in str_num:
                dig_sum += ord(ch) - ord("0")
            sum_dig += dig_sum
            sum_all += num
        return abs(sum_dig - sum_all)