from typing import List
from math import comb
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        cnt = Counter()
        pair_cnt = 0
        ans = 0
        while right < len(nums):
            # print(cnt)
            right_num = nums[right]
            cnt[right_num] += 1
            pair_cnt += (cnt[right_num] - 1)
            while pair_cnt >= k:
                # print(nums[left : right + 1], cnt)
                ans += len(nums) - right
                left_num = nums[left]
                pair_cnt -= (cnt[left_num] - 1)
                cnt[left_num] -= 1
                left += 1
            right += 1
        return ans

data = [
    [1,1,1,2,2,1,1]
    , 10
]
r = Solution().countGood(* data)
print(r)

