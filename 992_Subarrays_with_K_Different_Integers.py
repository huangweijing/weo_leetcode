from typing import List
from collections import Counter


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        ans = 0
        cnt = Counter()
        while right < len(nums):
            while len(cnt) < k and right < len(nums):
                cnt[nums[right]] += 1
                right += 1
            left_cnt, right_cnt = 0, 0
            while len(cnt) == k and right < len(nums):
                if cnt[nums[right]] + 1 > k:
                    break
                cnt[nums[right]] += 1
                right += 1
                right_cnt += 1
            while len(cnt) == k and left < right:
                if cnt[nums[left]] == 1:
                    break
                cnt[nums[left]] -= 1
                left += 1
                left_cnt += 1
            print(left, right, left_cnt, right_cnt)
            ans += (left_cnt + 1) * (right_cnt + 1)
        return ans


data = [
    [1,2,1,2,3]
    , 2
]
r = Solution().subarraysWithKDistinct(* data)
print(r)
