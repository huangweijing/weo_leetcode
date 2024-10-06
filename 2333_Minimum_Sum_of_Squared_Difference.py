from typing import List


class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff_list = list(sorted([abs(nums1[i] - nums2[i]) for i in range(len(nums1))], reverse=True))
        diff_list.append(0)
        # print(diff_list)
        for i in range(len(diff_list) - 1):
            if (diff_list[i] - diff_list[i + 1]) * (i + 1) > k:
                v1 = diff_list[i] - k // (i + 1)
                v2 = diff_list[i] - k // (i + 1) - 1
                c2 = k % (i + 1)
                c1 = i + 1 - c2
                ret = v1 ** 2 * c1 + v2 ** 2 * c2 + sum([diff_list[j] ** 2 for j in range(i + 1, len(diff_list))])
                return ret
            else:
                k -= (diff_list[i] - diff_list[i + 1]) * (i + 1)
        return 0
    

data = [
    [7,11,4,19,11,5,6,1,8]
    , [4,7,6,16,12,9,10,2,10]
    , 3
    , 6
]
r = Solution().minSumSquareDiff(* data)
print(r)
        