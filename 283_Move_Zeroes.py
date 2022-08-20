class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        look_forward_idx = -1
        while i < len(nums):
            if nums[i] == 0:
                if look_forward_idx == -1:
                    look_forward_idx = i + 1
                while look_forward_idx < len(nums) and nums[look_forward_idx] == 0:
                    look_forward_idx += 1
                if look_forward_idx == len(nums):
                    return
                tmp = nums[look_forward_idx]
                nums[look_forward_idx] = nums[i]
                nums[i] = tmp
            i += 1
data = [0]
Solution().moveZeroes(data)
print(data)