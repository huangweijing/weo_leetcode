from typing import List


class Solution:

    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1
        op_cnt = 0
        diff_sum = 0
        for i in range(len(nums1)):
            n1, n2 = nums1[i], nums2[i]
            diff = n1 - n2
            if diff % k != 0:
                return -1
            new_diff_sum = diff_sum + diff
            if (diff_sum >= 0 and new_diff_sum < 0) or (diff_sum <= 0 and new_diff_sum > 0):
                op_cnt += abs(diff_sum) // k
            elif abs(new_diff_sum) < abs(diff_sum):
                op_cnt += abs(diff) // k
            # print(diff, diff_sum, new_diff_sum, op_cnt)
            diff_sum = new_diff_sum
        if diff_sum != 0:
            return -1
        return op_cnt
    

data = [
    [2,4]
    , [4,2]
    , 2
]
r = Solution().minOperations(*data)
print(r)