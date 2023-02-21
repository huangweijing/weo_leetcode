from typing import List

class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int]
                           , firstLen: int, secondLen: int) -> int:
        prefix_sum = 0
        prefix_sum_arr = [0]
        for num in nums:
            prefix_sum += num
            prefix_sum_arr.append(prefix_sum)

        max_val = 0
        for i in range(len(nums) - firstLen + 1):
            val = prefix_sum_arr[i + firstLen] - prefix_sum_arr[i]
            for j in range(len(nums) - secondLen + 1):
                if i <= j + secondLen - 1 and j <= i + firstLen - 1:
                    continue
                    # print(i, j, j + secondLen)
                val2 = prefix_sum_arr[j + secondLen] - prefix_sum_arr[j]
                # print(i, j, val + val2)
                max_val = max(max_val, val + val2)
        return max_val

data = [
    [2,1,5,6,0,9,5,0,3,8]
    , 4, 3
]
r = Solution().maxSumTwoNoOverlap(* data)
print(r)

