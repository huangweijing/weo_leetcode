from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        arr_len = len(nums)
        while arr_len > 1:
            new_nums = []
            for i in range(arr_len - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
            arr_len = len(nums)
        return nums[0]

data = [1,2,3,4,5]
r = Solution().triangularSum(data)
print(r)
