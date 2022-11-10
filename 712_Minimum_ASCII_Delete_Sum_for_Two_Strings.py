from functools import cache

class Solution:
    def __init__(self):
        self.s1 = ""
        self.s2 = ""

    def calc_ascii(self, s: str):
        return sum(map(ord, s))

    @cache
    def my_del_sum(self, s1_len: int, s2_len: int) -> int:
        if s1_len == 0 and s2_len == 0:
            return 0
        if s1_len == 0:
            return self.calc_ascii(self.s2[:s2_len])
        if s2_len == 0:
            return self.calc_ascii(self.s1[:s1_len])
        if self.s1[s1_len - 1] == self.s2[s2_len - 1]:
            return self.my_del_sum(s1_len - 1, s2_len - 1)
        else:
            r1 = self.my_del_sum(s1_len, s2_len - 1) + self.calc_ascii(self.s2[s2_len - 1])
            r2 = self.my_del_sum(s1_len - 1, s2_len) + self.calc_ascii(self.s1[s1_len - 1])
            return min(r1, r2)

    @cache
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        self.s1, self.s2 = s1, s2
        return self.my_del_sum(len(s1), len(s2))

data = [
    "delete"
    , "leet"
]
r = Solution().minimumDeleteSum(* data)
print(r)
