# from collections import List

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return
        new_nums = nums[-k:]
        new_nums.extend(nums[:-k])
        nums[:] = new_nums[:]
        # while i < len(nums):
        #     tmp = nums[i]
        #     new_i = i + k
        #     new_i %= len(nums)
        #     nums[i] = nums[new_i]
        #     nums[new_i] = tmp
        #     i += 1
