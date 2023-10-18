from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_val = sum(arr[: k])
        ans = 1 if sum_val / k >= threshold else 0
        for i in range(k, len(arr)):
            sum_val = sum_val + arr[i] - arr[i - k]
            ans += 1 if sum_val / k >= threshold else 0
        return ans

data = [
    [1,1,1,1,1]
    , 1
    , 0
]
r = Solution().numOfSubarrays(* data)
print(r)