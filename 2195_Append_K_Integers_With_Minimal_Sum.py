from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        for i, num in enumerate(nums):
            cnt = len(nums) - i + k
            if cnt >= num:
                return (1 + cnt) * cnt // 2 - sum(nums[i: ])
        return (1 + k) * k // 2
    

data = [
    [1,4,25,10,25]
    , 2
]
r = Solution().minimalKSum(*data)
print(r)
