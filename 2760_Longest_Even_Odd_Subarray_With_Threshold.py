from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        dp_even = [0] * len(nums)
        dp_odd = [0] * len(nums)
        ans = 0
        for i, num in enumerate(nums):
            if num > threshold:
                continue
            if num % 2 == 0:
                dp_even[i] = dp_odd[i - 1] + 1
                ans = max(ans, dp_even[i])
            else:
                if dp_even[i - 1] > 0:
                    dp_odd[i] = dp_even[i - 1] + 1
                    ans = max(ans, dp_odd[i])
        return ans

data = [
    [1,2]
    , 2
]
r = Solution().longestAlternatingSubarray(* data)
print(r)
