from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num_arr = [0] * 2001
        for num in nums:
            num_arr[num + 1000] += 1

        min_height = [0] * 2003
        for i in range(2001):
            if i == 0:
                last_num = 0
            else:
                last_num = num_arr[i - 1]

            if num_arr[i] < min_height[i]:
                return False

            if num_arr[i] > last_num:
                min_height[i + 1] += num_arr[i] - last_num
                min_height[i + 2] += num_arr[i] - last_num
        return True
