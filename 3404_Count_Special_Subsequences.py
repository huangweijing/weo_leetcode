from typing import List
from collections import Counter


class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        cnt_arr = []
        for i in range(len(nums)):
            cnt = Counter()
            for j in range(i + 2, len(nums)):
                cnt[nums[j] / nums[i]] += 1
            cnt_arr.append(cnt)
        sum_cnt = Counter()
        sum_cnt_arr = [None] * len(nums)
        for idx, cnt in enumerate(reversed(cnt_arr)):
            i = len(nums) - 1 - idx
            sum_cnt = sum_cnt + cnt
            sum_cnt_arr[i] = sum_cnt
        # print(sum_cnt_arr)
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 2, len(nums)):
                ratio = nums[i] / nums[j]
                if j + 2 < len(nums):
                    ans += sum_cnt_arr[j + 2][ratio]
        return ans

data = [3,4,3,4,3,4,3,4]
r = Solution().numberOfSubsequences(data)
print(r)