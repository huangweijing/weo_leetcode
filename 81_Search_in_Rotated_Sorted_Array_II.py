from typing import List

class Solution:
    def find_pivot(self, nums: List[int]):
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] > nums[idx + 1]:
                return idx
            idx += 1
        # first = nums[0]
        # pivot = len(nums) >> 1
        # right_wall = len(nums)
        # while nums[pivot - 1] < nums[pivot] and pivot != len(nums) - 1:
        #     if first < nums[pivot]:
        #         pivot = (right_wall + pivot) >> 1
        #     else:
        #         right_wall = pivot
        #         pivot = pivot >> 1
        #     # print(pivot)
        # # if pivot == len(nums) - 1:
        # #     pivot = 0
        # if nums[pivot - 1] > nums[pivot]:
        #     return pivot
        # return 0

    @classmethod
    def translate_idx(cls, nums: List[int], pivot: int, idx: int):
        if pivot is None:
            return idx
        new_idx = pivot + idx + 1
        if new_idx >= len(nums):
            new_idx -= len(nums)
        return new_idx


    def search(self, nums: List[int], target: int) -> bool:
        idx = self.my_search(nums, target)
        return idx != -1

    def my_search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        idx = 0
        left_wall = 0
        right_wall = len(nums)
        # while idx != len(nums) - 1 and idx
        while True:
            # print(nums, pivot, idx, Solution.translate_idx(nums, pivot, idx), right_wall)
            if target < nums[Solution.translate_idx(nums, pivot, idx)]:
                right_wall = idx
                idx = (right_wall + left_wall) >> 1
            else:
                left_wall = idx
                idx = (right_wall + left_wall) >> 1
            if target == nums[Solution.translate_idx(nums, pivot, idx)]:
                return Solution.translate_idx(nums, pivot, idx)
            # print(nums, pivot, idx, Solution.translate_idx(nums, pivot, idx))
            if idx > 0 and nums[Solution.translate_idx(nums, pivot, idx - 1)]\
                    < target < nums[Solution.translate_idx(nums, pivot, idx)]:
                return -1
            if idx == 0 and target < nums[Solution.translate_idx(nums, pivot, idx)]:
                return -1
            if idx == len(nums) - 1 and target > nums[Solution.translate_idx(nums, pivot, idx)]:
                return -1

sol = Solution()
# r = sol.find_pivot([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1])
r = sol.my_search([1], 2)
print(r)