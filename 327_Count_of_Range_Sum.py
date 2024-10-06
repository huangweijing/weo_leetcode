from sortedcontainers import SortedList
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sl = SortedList()
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)
            sl.add(pre_sum[-1])
        sl.add(0)

        ans = 0
        for num in pre_sum[: -1]:
            sl.remove(num)
            idx1 = sl.bisect_left(num + lower) - 1
            idx2 = sl.bisect_right(num + upper)
            # print(sl, num + lower, num+ upper, idx2 - idx1 - 1, idx1, idx2)
            ans += idx2 - idx1 - 1
        return ans


data = [
    [-2,5,-1]
    , -2
    , 2
]
r = Solution().countRangeSum(*data)
print(r)

