import math
from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        out_num = nums[-1]
        ans = 0
        for num in reversed(nums[:-1]):
            if num <= out_num:
                out_num = num
            else:
                k = math.ceil(num / out_num)
                out_num = num // k
                # print(k, out_num)
                ans += k - 1
        return ans


cases = [
    # [3, 9, 3]
    # , [1,2,3,4,5]
    # , [3, 100, 4, 100, 5]
    # , [5,4,3,2,1]
    [7,6,15,6,11,14,10],
]
output = list(map(Solution().minimumReplacement, cases))
print(output)