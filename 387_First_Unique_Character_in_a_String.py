from typing import List


class Solution:
    DIG_CNT = 32

    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        n_sum = [0] * Solution.DIG_CNT
        nums_sum = [0] * Solution.DIG_CNT
        ans = 0
        for i in range(Solution.DIG_CNT):
            mask = 1 << i
            for num in nums:
                nums_sum[i] += (num & mask) >> i
            for num in range(n):
                n_sum[i] += (num & mask) >> i
            if nums_sum[i] > n_sum[i]:
                ans = 1 << i | ans
        return ans

data = [1, 3, 4, 3, 3]
r = Solution().findDuplicate(data)
print(r)