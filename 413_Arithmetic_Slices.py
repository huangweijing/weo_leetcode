from typing import List

class Solution:
    def count(self, size: int) -> int:
        return (size - 2) * (size - 1) >> 1

    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        i = 2
        is_arithmetic = False
        arith_len = 0
        result = 0
        while i < len(nums):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                if is_arithmetic:
                    arith_len += 1
                else:
                    arith_len = 3
                    is_arithmetic = True
            else:
                if is_arithmetic:
                    result += self.count(arith_len)
                arith_len = 0
                is_arithmetic = False
            i += 1
        if is_arithmetic:
            result += self.count(arith_len)
        return result


data_nums = [2,2,2,4,5,6]
r = Solution().numberOfArithmeticSlices(data_nums)
print(r)
