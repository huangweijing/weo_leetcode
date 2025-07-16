class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] == nums[1]:
            return -1
        