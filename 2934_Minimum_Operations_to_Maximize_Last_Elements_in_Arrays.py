from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1_last, n2_last = nums1[-1], nums2[-1]
        n1_good_cnt, n2_good_cnt = 0, 0
        for i in range(len(nums1[: -1])):
            n1, n2 = nums1[i], nums2[i]
            if max(n1, n2) <= min(n1_last, n2_last):
                pass
            elif n2 <= min(n1_last, n2_last) < n1 <= max(n1_last, n2_last):
                n2_good_cnt += 1
            elif n1 <= min(n1_last, n2_last) < n2 <= max(n1_last, n2_last):
                n1_good_cnt += 1
            else:
                return -1
        ans = len(nums1)
        if n1_last < n2_last:
            ans = min(ans, n2_good_cnt, n1_good_cnt + 1)
        else:
            ans = min(ans, n1_good_cnt, n2_good_cnt + 1)
        return ans

data = [
    [1,5,8]
    , [4,2,7]
]
r = Solution().minOperations(* data)
print(r)
