from typing import List
from collections import Counter

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum, prefix_sum_arr = 0, []
        for num in nums:
            prefix_sum += num
            prefix_sum_arr.append(prefix_sum)

        num_cnt = Counter(nums[:k])
        ans = prefix_sum_arr[k - 1] if len(num_cnt) == k else 0
        # print(prefix_sum_arr)
        for i in range(k, len(nums)):
            num_cnt[nums[i - k]] -= 1
            if num_cnt[nums[i - k]] == 0:
                del num_cnt[nums[i - k]]
            num_cnt[nums[i]] += 1
            # print(i, num_cnt, prefix_sum_arr[i], prefix_sum_arr[i - k])
            if len(num_cnt) == k:
                ans = max(ans, prefix_sum_arr[i] - prefix_sum_arr[i - k])

        return ans

data = [
    [9, 9, 9, 1, 2, 3]
    , 3
]
r = Solution().maximumSubarraySum(* data)
print(r)