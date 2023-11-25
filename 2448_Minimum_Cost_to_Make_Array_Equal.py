from typing import List
import itertools


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums_cost = list(sorted(zip(nums, cost), key=lambda x: x[0]))
        prefix_sum_arr, suffix_sum_arr = [], []
        prefix_sum, suffix_sum = 0, 0
        head_cost = 0
        for nc in nums_cost:
            prefix_sum += nc[1]
            prefix_sum_arr.append(prefix_sum)
            head_cost += abs(nc[0] - nums_cost[0][0]) * nc[1]
        for nc in reversed(nums_cost):
            suffix_sum += nc[1]
            suffix_sum_arr.append(suffix_sum)
        suffix_sum_arr = suffix_sum_arr[::-1]
        print(nums_cost)
        # print(head_cost)
        print(prefix_sum_arr, suffix_sum_arr)
        cost = head_cost
        ans = cost
        idx = 0
        for i in range(nums_cost[0][0], nums_cost[-1][0]):
            if idx + 1 < len(nums_cost):
                cost += prefix_sum_arr[idx] - suffix_sum_arr[idx + 1]
            else:
                cost += prefix_sum_arr[idx]
            ans = min(ans, cost)
            if i >= nums_cost[idx][0]:
                idx += 1
        return ans

        # for i, nc in enumerate(nums_cost[: -1]):
        #     (nums_cost[i + 1][0] - nc[0]) * prefix_sum_arr[i] - suffix_sum_arr[i + 1]




data = [
    [2,2,2,3,2]
    , [4,2,8,1,3]
]
r = Solution().minCost(* data)
print(r)
