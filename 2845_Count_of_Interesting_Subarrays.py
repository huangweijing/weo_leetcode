from typing import List
from collections import Counter


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        cnt_arr = [1 if num % modulo == k else 0 for num in nums]
        prefix_cnt = 0
        modulo_cnt = Counter()
        modulo_cnt[0] = 1
        ans = 0
        for cnt in cnt_arr:
            prefix_cnt += cnt
            ans += modulo_cnt[(prefix_cnt + modulo - k) % modulo]
            modulo_cnt[prefix_cnt % modulo] += 1
        return ans


data = [
    [3,1,9,6]
    , 3
    , 0
]
r = Solution().countInterestingSubarrays(* data)
print(r)
