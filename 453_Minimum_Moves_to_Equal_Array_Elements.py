from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_num = min(nums)
        ans = sum(map(lambda x: x - min_num, nums))
        return ans

r = Solution().minMoves([3, 2, 3])
print(r)