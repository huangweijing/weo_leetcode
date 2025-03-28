from typing import List
import math


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        num_set = set[int]()
        ans = math.ceil(len(nums) / 3)
        for i, num in enumerate(reversed(nums)):
            if num in num_set:
                return ans
            else:
                num_set.add(num)
            if (len(nums) - (i + 1)) % 3 == 0:
                ans = min(ans, (len(nums) - (i + 1)) // 3)
        return ans
    
data = [1, 2, 3, 3, 4]
r = Solution().minimumOperations(data)
print(r)
                
            