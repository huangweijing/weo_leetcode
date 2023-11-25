from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    ans = max(nums[i] ^ nums[j], ans)
        return ans


data = [1,2,2,1,2]
r = Solution().maximumStrongPairXor(data)
print(r)