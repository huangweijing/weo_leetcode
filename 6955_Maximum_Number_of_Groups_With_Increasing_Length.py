from typing import List
from functools import cache
from sortedcontainers import SortedList

class Solution:
    def __init__(self):
        self.arr = []
        self.sum_all = 0
        self.used_cnt = []

    @cache
    def check_okay(self, k: int) -> bool:
        if k == 0:
            return True
        arr = SortedList(self.arr)
        available_cnt, need_cnt = 0, 0
        # available_cnt, need_cnt = 0, 0
        sum_all = self.sum_all

        while k > 0:
            if available_cnt == 0:
                if len(arr) == 0:
                    return False
                pop_value = arr.pop()
                sum_all -= pop_value
                available_cnt = min(k, pop_value)
            if need_cnt == 0:
                need_cnt = k
                k -= 1
                if (k + 1) * k / 2 > sum_all:
                    return False
            # print(f"arr={arr}, k={k}, need_cnt={need_cnt}, available_cnt={available_cnt}")

            if available_cnt >= need_cnt:
                available_cnt -= need_cnt
                need_cnt = 0
                if available_cnt != 0:
                    arr.add(available_cnt)
                    sum_all += available_cnt
                    available_cnt = 0
            else:
                need_cnt -= available_cnt
                available_cnt = 0

        # print(k, need_cnt)
        if k == 0 and need_cnt == 0:
            return True
        return False

    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        self.arr = usageLimits
        self.arr.sort(reverse=True)
        self.sum_all = sum(self.arr)
        # print(self.arr)
        # return
        #binary search
        # return
        left, right = 1, len(self.arr)
        mid = right
        while left <= right:
            res_mid = self.check_okay(mid)
            res_mid_m1 = self.check_okay(mid + 1)
            # print(f"mid={mid}, res_mid={res_mid}, res_mid_m1={res_mid_m1}, {left}, {right}")
            if res_mid and (not res_mid_m1):
                return mid
            elif res_mid and res_mid_m1:
                left = mid + 1
            else:
                right = mid - 1
            # print(left, right)
            mid = left + right >> 1
        return mid


sol = Solution()
r = sol.maxIncreasingGroups([7,10,4,5,7,4,5,3,5,6])
print(r)
# print(sol.check_okay(11))

# sl = SortedList([4, 8, 3, 12])
# while len(sl) > 0:
#     val = sl.pop()
#     print(sl, val)
#     if val % 3 == 0:
#         sl.add(val // 3)