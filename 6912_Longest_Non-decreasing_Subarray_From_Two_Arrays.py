from typing import List
from functools import cache


class Solution:
    def my_sol(self, nums1: List[int], nums2: List[int]) -> int:
        min_num_0 = min(nums1[0], nums2[0])
        dp = [[1, min_num_0], [1, min_num_0]]  #seq_len, top_num
        ans = 1
        for i in range(1, len(nums1)):
            # print(dp)
            n1 = min(nums1[i], nums2[i])
            n2 = max(nums1[i], nums2[i])

            new_dp = [[1, n1], [1, n1]]
            if n1 >= dp[0][1]:
                new_dp[0] = [dp[0][0] + 1, n1]
            elif n2 >= dp[0][1]:
                new_dp[0] = [dp[0][0] + 1, n2]

            if n1 >= dp[1][1]:
                new_dp[1] = [dp[1][0] + 1, n1]
            elif n2 >= dp[1][1]:
                new_dp[1] = [dp[1][0] + 1, n2]

            if new_dp[0][1] == new_dp[1][1] > n1:
                new_dp = [[1, n1], [max(new_dp[0][0], new_dp[1][0]), new_dp[0][1]]]

            ans = max(new_dp[0][0], new_dp[1][0], ans)
            dp = new_dp

        return ans

    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        return self.my_sol(nums1, nums2)

data = [
    [1]
    , [1]
]
    # [2, 4, 23, 47, 37]
    # , [8, 3, 15, 39, 21]
# [11, 7, 7, 9]
# , [19, 19, 1, 7]
r = Solution().maxNonDecreasingLength(* data)
print(r)



