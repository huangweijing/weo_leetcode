from typing import List

class Solution:
    def __init__(self):
        self.sum_result = 0

    def my_xor_sum(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return [nums[0]]
        result = list[int]()
        sub_result = self.my_xor_sum(nums[1:])
        for sub in sub_result:
            result.append(sub ^ nums[0])
        result.extend(sub_result)
        result.append(nums[0])
        return result

    def subsetXORSum(self, nums: List[int]) -> int:
        return sum(self.my_xor_sum(nums))


data_nums = [3,4,5,6,7,8]
r = Solution().subsetXORSum(data_nums)
print(r)