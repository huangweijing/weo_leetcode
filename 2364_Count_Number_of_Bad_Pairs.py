from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        num_sub_idx = [0] * len(nums)
        num_sub_idx_dict = dict[int, int]()
        for i, n in enumerate(nums):
            num_sub_idx[i] = n - i
            if n - i not in num_sub_idx_dict:
                num_sub_idx_dict[n - i] = 0
            num_sub_idx_dict[n - i] += 1

        result = 0
        for val in num_sub_idx_dict.values():
            result += val * (len(nums) - val)
        return result >> 1




