from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def digits_sum(self, num):
        digits = 0
        while num > 0:
            digits += num % 10
            num //= 10
        return digits

    def maximumSum(self, nums: List[int]) -> int:
        digits = defaultdict(lambda : SortedList())
        for num in nums:
            dig = self.digits_sum(num)
            digits[dig].add(num)
        ans = -1
        for key, val in digits.items():
            if len(val) >= 2:
                ans = max(ans, val[-1] + val[-2])
        return ans

data = [18,43,36,13,7]
r = Solution().maximumSum(data)
print(r)
