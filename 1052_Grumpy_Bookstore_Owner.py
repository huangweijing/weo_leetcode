from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int]
                     , grumpy: List[int], minutes: int) -> int:
        not_grumpy_sum = 0
        prefix_sum_arr = []
        prefix_sum = 0
        for i, c in enumerate(customers):
            not_grumpy_sum += c * (1 - grumpy[i])
            prefix_sum += grumpy[i] * c
            prefix_sum_arr.append(prefix_sum)
        ans = not_grumpy_sum
        for i in range(len(customers)):
            if i == 0:
                ans = prefix_sum_arr[min(i + minutes, len(customers)) - 1] + not_grumpy_sum
            else:
                ans = max(ans, prefix_sum_arr[min(i + minutes, len(customers)) - 1] - prefix_sum_arr[i - 1] + not_grumpy_sum)
        return ans


data = [
    [1,0,1,2,1,1,7,5]
    , [0,1,0,1,0,1,0,1]
    , 3
]
r = Solution().maxSatisfied(* data)
print(r)
        