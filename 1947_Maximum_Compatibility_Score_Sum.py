from typing import List
from functools import reduce, cache


class Solution:
    def __init__(self):
        self.stu_list = list[int]()
        self.men_list = list[int]()
        self.sur_len = 0

    @classmethod
    def arr_to_bin(cls, arr: list[int]) -> int:
        return reduce(lambda a, b: a * 2 + b, arr)

    @cache
    def my_sol(self, stu_idx: int, men_mask: int) -> int:
        if stu_idx == len(self.stu_list):
            return 0
        ret = 0
        for i in range(len(self.men_list)):
            bit = (men_mask & (1 << i)) >> i
            if bit == 0:
                comp = self.men_list[i] ^ self.stu_list[stu_idx] ^ ((1 << self.sur_len) - 1)
                ret = max(ret, comp.bit_count() +
                          self.my_sol(stu_idx + 1, men_mask | (1 << i)))
        return ret


    def maxCompatibilitySum(self, students: List[List[int]]
                            , mentors: List[List[int]]) -> int:
        self.sur_len = len(students[0])
        self.stu_list = list(map(Solution.arr_to_bin, students))
        self.men_list = list(map(Solution.arr_to_bin, mentors))
        return self.my_sol(0, 0)

data = [
    [[1,1,0],[1,0,1],[0,0,1]]
    , [[1,0,0],[0,0,1],[1,1,0]]
]
r = Solution().maxCompatibilitySum(* data)
print(r)
