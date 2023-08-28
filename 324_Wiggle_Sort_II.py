from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        arr = [0] * len(nums)
        i = 0
        while i * 2 + 1 < len(arr):
            arr[i * 2 + 1] = nums.pop()
            i += 1
        i = 0
        while i * 2 < len(arr):
            arr[i * 2] = nums.pop()
            i += 1
        # arr[0] = nums.pop()

        nums[:] = arr[:]

data = [4, 5, 5, 6]
Solution().wiggleSort(data)
print(data)




