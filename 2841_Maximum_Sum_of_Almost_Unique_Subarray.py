from typing import List
from collections import Counter


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cnt = Counter(nums[: k])
        cnt_sum = sum(nums[: k])
        ans = 0
        if len(cnt) >= m:
            ans = max(ans, cnt_sum)
        for i in range(k, len(nums)):
            cnt_sum += nums[i]
            cnt_sum -= nums[i - k]
            cnt[nums[i]] += 1
            cnt[nums[i - k]] -= 1
            if cnt[nums[i - k]] == 0:
                del cnt[nums[i - k]]
            if len(cnt) >= m:
                ans = max(ans, cnt_sum)
        return ans


