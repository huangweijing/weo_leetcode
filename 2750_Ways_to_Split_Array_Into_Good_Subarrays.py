from typing import List


class Solution:
    MOD = 10 ** 9 + 7

    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        start_idx, end_idx = -1, -1
        for i, num in enumerate(nums):
            if num != 0:
                start_idx = i
                break
        for i, num in enumerate(reversed(nums)):
            if num != 0:
                end_idx = len(nums) - 1 - i
                break
        if start_idx == end_idx == -1:
            return 0
        ans = 1
        i = start_idx
        ways_cnt = 1
        while i <= end_idx:
            while i <= end_idx and nums[i] == 1:
                ans = (ans * ways_cnt) % Solution.MOD
                i += 1
                ways_cnt = 1
            while i <= end_idx and nums[i] == 0:
                ways_cnt += 1
                i += 1
        return ans

data = [0,1,0]
r = Solution().numberOfGoodSubarraySplits(data)
print(r)