from typing import List


class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        last_one = -1
        for i, num in enumerate(nums):
            if i == 0 or i >= len(nums) - 1:
                last_one = num
                continue
            if num == nums[i + 1]:
                continue
            # print(last_one, num, nums[i + 1])
            if num > last_one and num > nums[i + 1]:
                ans += 1
            elif num < last_one and num < nums[i + 1]:
                ans += 1
            last_one = num
        return ans


data = [2,4,1,1,6,5]
r = Solution().countHillValley(data)
print(r)