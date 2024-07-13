from typing import List
from collections import Counter
import bisect


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        arr = []
        cnt = Counter()
        arr_cnt = Counter()
        for num in nums:
            cnt[num] += 1
            arr.append(len(cnt))
            arr_cnt[len(cnt)] += 1
        print(arr_cnt)
        ans = 0
        for i, val in enumerate(arr):
            ans += arr_cnt[val + k - 1]
            print(arr_cnt[val + k - 1])
        return ans


data = [
    [1,2,1,2,3]
    , 2
]
r = Solution().subarraysWithKDistinct(* data)
print(r)
