from typing import List

class Solution:

    def is_existed(self, nums: List[int], x: int) -> int:
        if len(nums) > 0 and (x < nums[0] or x > nums[len(nums) - 1]):
            return -1

        left_wall = 0
        right_wall = len(nums)
        idx = (left_wall + right_wall) >> 1
        while left_wall < right_wall:
            if nums[idx] < x:
                left_wall = idx
            elif nums[idx] > x:
                right_wall = idx
            idx = (left_wall + right_wall) >> 1
            if nums[idx] == x:
                return idx
            if idx > 0 and nums[idx - 1] < x < nums[idx]:
                return -1
            if idx < len(nums) - 1 and nums[idx] < x < nums[idx + 1]:
                return -1
            # print(nums, x, right_wall, left_wall, idx)


    def minOperations(self, nums: List[int], x: int) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1
        sum_left_arr = [0] * len(nums)
        sum_right_arr = [0] * len(nums)

        sum_left = 0
        sum_right = 0

        while left_ptr < len(nums):
            sum_left += nums[left_ptr]
            sum_left_arr[left_ptr] = sum_left

            sum_right += nums[right_ptr]
            sum_right_arr[left_ptr] = sum_right

            left_ptr += 1
            right_ptr -= 1

        # print(sum_left_arr)
        # print(sum_right_arr)

        sum_2_side = None
        min_sum_2_side = len(nums)
        for left_ptr in range(len(sum_left_arr)):
            expect = x - sum_left_arr[left_ptr]
            idx = self.is_existed(sum_right_arr, expect)
            if idx == -1 or idx + left_ptr + 2 > len(nums):
                continue
            else:
                sum_2_side = idx + 1 + left_ptr + 1
                if sum_2_side < min_sum_2_side:
                    min_sum_2_side = sum_2_side

        idx = self.is_existed(sum_right_arr, x)
        if idx != -1:
            sum_2_side = idx + 1
            if sum_2_side < min_sum_2_side:
                min_sum_2_side = sum_2_side

        idx = self.is_existed(sum_left_arr, x)
        if idx != -1:
            sum_2_side = idx + 1
            if sum_2_side < min_sum_2_side:
                min_sum_2_side = sum_2_side

        if sum_2_side is None:
            return -1
        else:
            return  min_sum_2_side

sol = Solution()
r = sol.minOperations([5,1,4,2,3,8], 18)
print(r)
# print(sol.is_existed([1, 2, 3, 4, 5], 1))