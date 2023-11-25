from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zero_cnt1, zero_cnt2 = 0, 0
        sum1, sum2 = 0, 0
        for num in nums1:
            if num == 0:
                zero_cnt1 += 1
            sum1 += num
        for num in nums2:
            if num == 0:
                zero_cnt2 += 1
            sum2 += num
        if zero_cnt1 == 0 and sum1 < sum2 + zero_cnt2:
            return -1
        if zero_cnt2 == 0 and sum2 < sum1 + zero_cnt1:
            return -1
        return max(sum1 + zero_cnt1, sum2 + zero_cnt2)
