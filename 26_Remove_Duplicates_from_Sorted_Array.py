from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = len(nums)
        i = 0
        while i < cnt:
        # for i in range(len(nums)):
            if i + 1 < cnt:
                if nums[i] == nums[i + 1]:
                    for j in range(i+1, cnt):
                        nums[j-1] = nums[j]
                    cnt -= 1
                    i -= 1
            i += 1
        return cnt

    def removeDuplicates2(self, nums: List[int]) -> int:
        cnt = 0
        new_nums = []
        i = 0
        while i < len(nums):
            num = nums[i]
            new_nums.append(num)
            cnt += 1
            n = 1
            while i + n < len(nums) and num == nums[i + n]:
                n = n + 1
                continue
            i += n

        for i in range(len(new_nums)):
            nums[i] = new_nums[i]

        return cnt

sol = Solution()
input_data = [0,0,1,1,1,2,2,3,3,4]
r = sol.removeDuplicates2(input_data)
print(r)
print(input_data)