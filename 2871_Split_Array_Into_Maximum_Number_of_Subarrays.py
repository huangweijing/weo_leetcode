from typing import List
from functools import reduce


class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        arr_and = reduce(lambda a, b: a & b, nums)
        ans = 0
        and_val = (1 << 31) - 1
        for num in nums:
            # print(ans, num & and_val, num, and_val, arr_and)
            if and_val & num == arr_and:
                ans += 1
                and_val = (1 << 31) - 1
            else:
                and_val &= num

        if and_val == arr_and:
            ans += 1

        if arr_and != 0:
            ans = 1

        return ans


data = [22,21,29,22]
# print(22 & 21 & 29 & 22)
# print(22 & 21)
# print(29 & 22)
r = Solution().maxSubarrays(data)
print(r)

