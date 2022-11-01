from typing import List
import bisect

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        pre_sum_arr, sum_all = [], 0
        costs.sort()
        for cost in costs:
            sum_all += cost
            pre_sum_arr.append(sum_all)
        idx = bisect.bisect_left(pre_sum_arr, coins)
        if idx < len(costs) and pre_sum_arr[idx] == coins:
            return idx + 1
        else:
            return idx
