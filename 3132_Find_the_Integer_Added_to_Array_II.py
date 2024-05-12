from typing import List
import math


class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        # print(nums1)
        # print(nums2)
        ans = math.inf
        for start in range(3):
            diff = nums2[0] - nums1[start]
            idx, chance = start, 2
            is_okay = True
            for i, num in enumerate(nums2):
                # print(i, idx, num, nums1[idx], diff, chance)
                # if idx == len(nums1):
                #     is_okay = False
                #     break
                while idx < len(nums1) and num - nums1[idx] != diff:
                    chance -= 1
                    idx += 1
                    if chance < 0:
                        is_okay = False
                        break
                if idx >= len(nums1) or num - nums1[idx] != diff:
                    is_okay = False
                    break
                idx += 1
                if not is_okay:
                    break
            if is_okay:
                ans = min(ans, diff)
        return ans


data = [
    [7, 9, 1, 4]
    , [0, 8]
]
r = Solution().minimumAddedInteger(* data)
print(r)



