from typing import List

class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        while len(nums) > 1:
            n1 = nums.pop()
            n2 = nums.pop()
            if n1 >= n2:
                nums.append(n1 + n2)
            else:
                nums.append(n2)
        return nums[0]

data = [2,13,20,9,10]
r = Solution().maxArrayValue(data)
print(r)
