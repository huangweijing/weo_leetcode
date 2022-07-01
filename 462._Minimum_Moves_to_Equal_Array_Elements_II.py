from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid_num = nums[len(nums) >> 1]
        # num_avg = int(sum(nums) / len(nums) + 0.5)
        result = 0
        for num in nums:
            result += abs(num - mid_num)
        return result

data = [1,0,0,8,6]
r = Solution().minMoves2(data)
print(r)

