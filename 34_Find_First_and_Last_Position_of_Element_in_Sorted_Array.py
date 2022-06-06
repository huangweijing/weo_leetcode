import threading
from typing import List

class Solution:

    def find_start(self, nums: List[int], target: int):
        left_wall = 0
        right_wall = len(nums)
        start_idx = -1
        idx = left_wall
        while True:
            if nums[idx] < target:
                left_wall = idx
                idx = (idx + right_wall) >> 1
            elif nums[idx] == target:
                if idx == 0 or nums[idx - 1] != nums[idx]:
                    start_idx = idx
                    break
                else:
                    right_wall = idx
                    idx = (idx + left_wall) >> 1
            else:
                right_wall = idx
                idx = (idx + left_wall) >> 1
            # cant find the result
            if idx > 0 and nums[idx - 1] < target < nums[idx]:
                break
            if idx == 0 and target < nums[idx]:
                break
            if idx == len(nums) - 1 and target > nums[idx]:
                break
        return start_idx

    def find_end(self, nums: List[int], target: int):
        left_wall = 0
        right_wall = len(nums)
        end_idx = -1
        idx = left_wall
        while True:
            if nums[idx] < target:
                left_wall = idx
                idx = (idx + right_wall) >> 1
            elif nums[idx] == target:
                if idx == len(nums) - 1 or nums[idx + 1] != nums[idx]:
                    end_idx = idx
                    break
                else:
                    left_wall = idx
                    idx = (idx + right_wall) >> 1
            else:
                right_wall = idx
                idx = (idx + left_wall) >> 1
            # cant find the result
            if idx > 0 and nums[idx - 1] < target < nums[idx]:
                break
            if idx == 0 and target < nums[idx]:
                break
            if idx == len(nums) - 1 and target > nums[idx]:
                break
        return end_idx


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        else:
            return [
                self.find_start(nums, target)
                , self.find_end(nums, target)
            ]


sol = Solution()
r = sol.searchRange([], 0)
print(r)