from typing import List
from collections import Counter


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        right_k_cnt = []
        k_cnt = 0
        for num in reversed(nums):
            if num == k:
                k_cnt += 1
            right_k_cnt.append(k_cnt)
        right_k_cnt = right_k_cnt[::-1]
        max_val = Counter()
        k_cnt = 0
        num_cnt = Counter()
        ans = -10e5
        for i, num in enumerate(nums):
            left, right = 0, 0
            num_cnt[num] += 1
            if i < len(nums) - 1:
                right = right_k_cnt[i + 1]
            for key in range(51):
                left = max_val[key]
                ans = max(ans, left + num_cnt[key] + right)
                max_val[key] = max(max_val[key], num_cnt[k] - num_cnt[key])

            # print(num_cnt)
            # print(max_val)
            # print(f"num={num}, ans={ans}")
            # print("---")
        return ans


data = [
    [1,2,1,4,5,6]
    , 1
]
r = Solution().maxFrequency(*data)
print(r)