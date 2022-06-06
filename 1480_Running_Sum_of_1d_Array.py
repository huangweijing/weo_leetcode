from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result_list = list[int]()
        running_sum = 0
        for num in nums:
            running_sum = running_sum + num
            result_list.append(running_sum)
        return result_list