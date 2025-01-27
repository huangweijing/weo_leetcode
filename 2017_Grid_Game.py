from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        acc_sum_arr, acc_sum_rev = [], []
        for _, val in enumerate(grid[1]):
            if len(acc_sum_arr) == 0:
                acc_sum_arr.append(val)
            else:
                acc_sum_arr.append(val + acc_sum_arr[-1])
        for _, val in enumerate(reversed(grid[0])):
            if len(acc_sum_rev) == 0:
                acc_sum_rev.append(val)
            else:
                acc_sum_rev.append(val + acc_sum_rev[-1])
        acc_sum_rev = acc_sum_rev[::-1]
        ans = 10e9
        for i in range(len(acc_sum_rev)):
            left, right = 0, 0
            if i > 0:
                left = acc_sum_arr[i - 1]
            if i < len(acc_sum_arr) - 1:
                right = acc_sum_rev[i + 1]
            ans = min(ans, max(left, right))
        # print(acc_sum_rev)
        # print(acc_sum_arr)
        return ans


data = [[2,5,4],[1,5,1]]
r = Solution().gridGame(data)
print(r)