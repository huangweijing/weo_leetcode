from typing import List

class Solution:

    def wiggleMaxLength(self, nums: List[int]) -> int:
        last_num = -1
        new_nums = []
        for num in nums:
            if last_num == num:
                continue
            else:
                new_nums.append(num)
            last_num = num
        nums = new_nums
        # print(new_nums)

        if len(nums) == 1:
            return 1
        wiggle_length = 1
        idx = 1
        ascending = nums[idx] > nums[idx - 1]

        while idx < len(nums):
            if ascending:
                wiggle_length += 1
                while idx < len(nums):
                    if nums[idx] == nums[idx - 1]:
                        idx += 1
                        continue
                    # print(idx)
                    if nums[idx] < nums[idx - 1]:
                        ascending = False
                        break
                    idx += 1
            if not ascending:
                wiggle_length += 1
                while idx < len(nums):
                    if nums[idx] == nums[idx - 1]:
                        idx += 1
                        continue
                    if nums[idx] > nums[idx - 1]:
                        ascending = True
                        break
                    idx += 1
        return wiggle_length

sol = Solution()
data = [0,0, 1, 2, 3, 3, 2]
r = sol.wiggleMaxLength(data)
print(r)

