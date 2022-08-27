from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = []

        i = len(nums) - 1
        stack = []
        while i >= 0:
            # print(nums[i], stack)
            while len(stack) > 0 and nums[i] >= stack[-1]:
                stack.pop()
            stack.append(nums[i])
            i -= 1

        i = len(nums) - 1
        while i >= 0:
            # print(nums[i], stack)
            while len(stack) > 0 and nums[i] >= stack[-1]:
                stack.pop()
            if len(stack) > 0:
                result.append(stack[-1])
            else:
                result.append(-1)
            stack.append(nums[i])
            i -= 1
        result.reverse()
        return result

data = [1,2,3,4,3]
r = Solution().nextGreaterElements(data)
print(r)

