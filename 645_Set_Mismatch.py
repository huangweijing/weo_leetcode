from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_set = set()
        num_set2 = set(range(1, len(nums) + 1))
        result = []
        for num in nums:
            if num in num_set:
                result.append(num)
            else:
                num_set.add(num)
                num_set2.remove(num)
        result.append(num_set2.pop())
        return result
