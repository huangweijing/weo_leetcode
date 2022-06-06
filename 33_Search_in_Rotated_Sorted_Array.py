from typing import List

class Solution:
    def find_pivot(self, nums: List[int]):
        first = nums[0]
        pivot = len(nums) >> 1
        right_wall = len(nums)
        while nums[pivot - 1] < nums[pivot] and pivot != len(nums) - 1:
            if first < nums[pivot]:
                pivot = (right_wall + pivot) >> 1
            else:
                right_wall = pivot
                pivot = pivot >> 1
            # print(pivot)
        # if pivot == len(nums) - 1:
        #     pivot = 0
        if nums[pivot - 1] > nums[pivot]:
            return pivot
        return 0

    @classmethod
    def translate_idx(cls, nums: List[int], pivot: int, idx: int):
        new_idx = pivot + idx
        if new_idx >= len(nums):
            new_idx -= len(nums)
        return new_idx

    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        idx = 0
        left_wall = 0
        right_wall = len(nums)
        # while idx != len(nums) - 1 and idx
        while True:
            # print(nums, pivot, idx, Solution.translate_idx(nums, pivot, idx))
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
            # print()


sol = Solution()
data = [1, 3, 4, 7, 0]
p = sol.find_pivot(data)
print(p)
r = sol.search(data, 6)
print(r)