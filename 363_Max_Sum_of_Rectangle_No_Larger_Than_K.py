import math

from sortedcontainers import SortedSet, SortedList
from typing import List
#
# s = SortedSet([7, 8, 3, 2, 1])
# print(s.bisect_left(8))

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        matrix_size_arr = [0] * m
        for i in range(n):
            for j in range(i, n):
                pass


    def max_arr_less_than_k(self, arr: list[int], k) -> int:
        sum_arr = []
        sum_val = 0
        for num in arr:
            sum_val += num
            sum_arr.append(sum_val)
        print(sum_arr)

        result = -math.inf
        sorted_list = SortedList()
        for right_idx, right in enumerate(sum_arr):
            sorted_list.add(right)
            left_idx = sorted_list.bisect_left(right - k)
            if left_idx > len(sorted_list) - 1:
                continue
            print(sorted_list[left_idx], right, sorted_list)
            if right - sorted_list[left_idx] > result:
                result = right - sorted_list[left_idx]
        return result


r = Solution().max_arr_less_than_k([-2, -1, 2, 9, 6, -3, 1, 7], 4)
print(r)

