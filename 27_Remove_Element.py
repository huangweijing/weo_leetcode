from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        new_nums = []
        for num in nums:
            if num != val:
                new_nums.append(num)
                cnt += 1

        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        return cnt