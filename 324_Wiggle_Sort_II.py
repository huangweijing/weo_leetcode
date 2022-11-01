from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        arr = [0] * len(nums)
        if len(nums) & 1 == 0:
            for i in range(len(nums) // 2):
                arr[i * 2] = nums[i]
                arr[i * 2 + 1] = nums[len(nums) // 2 + i]
        else:
            for i in range(len(nums) // 2):
                arr[i * 2] = nums[i]
                arr[i * 2 + 1] = nums[len(nums) // 2 + 1 + i]
            arr[-1] = nums[len(nums) // 2]

        nums[:] = arr[:]

data = [1, 2, 3, 4, 5]
Solution().wiggleSort(data)
print(data)




