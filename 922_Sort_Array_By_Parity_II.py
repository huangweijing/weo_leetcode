from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_idx, even_idx = 1, 0
        result = [0] * len(nums)
        for num in nums:
            if num & 1 == 1:
                result[odd_idx] = num
                odd_idx += 2
            else:
                result[even_idx] = num
                even_idx += 2
        return result
