from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        closest_max, closest_min, farthest_targ = -1, -1, -1
        ans = 0
        for i, num in enumerate(nums):
            if minK <= num <= maxK:
                if farthest_targ == -1:
                    farthest_targ = i
            else:
                farthest_targ = -1
            if num == minK:
                closest_min = max(closest_min, i)
            if num == maxK:
                closest_max = max(closest_max, i)
            if farthest_targ != -1 and closest_min >= farthest_targ \
                    and closest_max >= farthest_targ:
                ans += min(closest_min, closest_max) - farthest_targ + 1
            # print(i, num, ans)
        return ans


data = [
    [1, 1, 1, 1]
    , 1
    , 1
]
r = Solution().countSubarrays(* data)
print(r)