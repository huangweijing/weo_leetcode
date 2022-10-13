class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                pass
            else:
                flag = False
                break
        if flag:
            return True

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                pass
            else:
                return False
        return True