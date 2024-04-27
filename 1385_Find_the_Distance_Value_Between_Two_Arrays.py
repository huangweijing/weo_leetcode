from typing import List
import bisect


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        arr2.sort()
        # print(arr2)
        for num in arr1:
            idx = bisect.bisect_left(arr2, num)
            if idx > 0 and num - arr2[idx - 1] <= d:
                continue
            if idx < len(arr2) and arr2[idx] - num <= d:
                continue
            # print(num, idx, abs(arr2[idx] - num), abs(arr2[idx - 1] - num))
            ans += 1
        return ans


data = [
[1,4,2,3]
, [-4,-3,6,10,20,30]
, 3
]
r = Solution().findTheDistanceValue(* data)
print(r)