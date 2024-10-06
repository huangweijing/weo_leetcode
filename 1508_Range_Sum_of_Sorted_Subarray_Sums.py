from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix_sum = [0]
        arr = []
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)
        for i in range(n):
            for j in range(i, n):
                arr.append(prefix_sum[j + 1] - prefix_sum[i])
        arr.sort()
        ans = 0
        mod = 10 ** 9 + 7
        for i in range(left - 1, right):
            ans = (ans + arr[i]) % mod
        return ans


data = [
    [1,2,3,4]
    , 4
    , 1
    , 5
]
r = Solution().rangeSum(*data)
print(r)

