import math
from typing import List
# from functools import cache

def get_sum_arr(arr: list[int]):
    sum_val = 0
    result = list[int]()
    for num in arr:
        sum_val += num
        result.append(sum_val)
    return result

# class Solution:
#     def __init__(self):
#         self.gas_sum_arr = []
#         self.cost_sum_arr = []
#
#     def calc_range(self, sum_arr: list[int], i: int, j: int) -> int:
#         if i == 0:
#             return sum_arr[j - 1]
#         if j == 0:
#             return sum_arr[-1] - sum_arr[i - 1]
#         if 0 < i < j:
#             return self.calc_range(sum_arr, i, 0) - self.calc_range(sum_arr, j, 0)
#         elif 0 < j <= i:
#             return self.calc_range(sum_arr, i, 0) + self.calc_range(sum_arr, 0, j)
#
#     def get_gas_cost_diff(self, gas: list[int], cost: list[int]):
#         gas_cost_diff = []
#         for i in range(len(gas)):
#             gas_cost_diff.append([gas[i] - cost[i], i])
#         gas_cost_diff.sort(key=lambda x:x[0], reverse=True)
#         return gas_cost_diff
#
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         self.gas_sum_arr = get_sum_arr(gas)
#         self.cost_sum_arr = get_sum_arr(cost)
#         if self.gas_sum_arr[-1] < self.cost_sum_arr[-1]:
#             return -1
#
#         gas_cost_diff = self.get_gas_cost_diff(gas, cost)
#
#         for diff, i in gas_cost_diff:
#             print(diff, i)
#             idx_okay = True
#             for step in range(len(gas)):
#                 obtained_gas = self.calc_range(self.gas_sum_arr, i, (i + step) % len(gas))
#                 gas_cost = self.calc_range(self.cost_sum_arr, i, (i + step) % len(gas))
#                 if gas_cost > obtained_gas:
#                     idx_okay = False
#                     break
#             if idx_okay:
#                 return i
#         return -1

class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_val = 0
        min_sum = math.inf
        min_idx = 0
        for i in range(len(gas)):
            sum_val += gas[i] - cost[i]
            if sum_val < min_sum:
                min_sum = sum_val
                min_idx = i
        if sum_val < 0:
            return -1
        if min_idx == len(gas) - 1:
            return 0
        else:
            return min_idx + 1


sol = Solution()

data = [
    [1, 2, 3, 4, 5]
    ,[3, 4, 5, 1, 2]
]
# print(len(data[0]))
r = sol.canCompleteCircuit(* data)
print(r)
# r = sol.calc_range(sol.gas_sum_arr, 4, 3), sol.calc_range(sol.cost_sum_arr, 4, 3)
# print(r)