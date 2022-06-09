from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10000
        arr_sum = 0
        for num in nums:
            arr_sum += num
            if max_sum < arr_sum:
                max_sum = arr_sum
            if arr_sum < 0:
                arr_sum = 0
        return max_sum

sol = Solution()
data = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(data))

class DivideConquerSolution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        left = maxSubArray(nums[0: len(nums) >> 1])
        right = maxSubArray(nums[len(nums) >> 1: len(nums)])
