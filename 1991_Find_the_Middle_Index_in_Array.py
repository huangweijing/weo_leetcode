from itertools import accumulate

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        prefix_sum = 0
        for i, num in enumerate(nums):
            if sum_nums - num - prefix_sum == prefix_sum:
                return i
            prefix_sum += num
        return -1



