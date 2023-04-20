from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, 0
        ans = 0
        while right < len(nums):
            while right < len(nums) and nums[right] <= nums[left]:
                right += 1
            if right < len(nums):
                ans += 1
                right += 1
            else:
                break
            left += 1
        return ans

data = [1,3,5,2,1,3,1]
r = Solution().maximizeGreatness(data)
print(r)