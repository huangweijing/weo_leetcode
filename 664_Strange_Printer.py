import datetime
from functools import cache
import math

class Solution:
    def __init__(self):
        self.s = ""

    @cache
    def my_sol(self, left_idx: int, right_idx: int) -> int:
        """
        return the minimum step count from left_idx to right_idx of self.s
        :param left_idx:
        :param right_idx:
        :return:
        """
        # print(self.s[left_idx: right_idx + 1])
        if left_idx > right_idx:
            return 0
        if left_idx == right_idx:
            return 1
        res = math.inf
        start_idx = left_idx
        # on condition that the s is simplified (no adjacent same chars)
        if self.s[left_idx] == self.s[right_idx]:
            start_idx = left_idx + 1

        for i in range(start_idx, right_idx):
            sub_sol = self.my_sol(start_idx, i) + self.my_sol(i + 1, right_idx)
            res = min(res, sub_sol)
        # print(self.s[left_idx: right_idx + 1], res)
        return res


    def simplify(self, s: str) -> str:
        new_s = ""
        old_ch = ""
        for ch in s:
            if ch != old_ch:
                new_s += ch
            old_ch = ch
        return new_s

    def strangePrinter(self, s: str) -> int:
        self.s = self.simplify(s)
        return self.my_sol(0, len(self.s) - 1)


start = datetime.datetime.now()
# r = Solution().strangePrinter("dddccbdbababaddcbcaabdbdddcccddbbaabddb")
# r = Solution().strangePrinter("dcdcdddabcaddcdcbdbcadadadddac")
# r2 = Solution2().strangePrinter("dcdcdddabcaddcdcbdbcadadadddac")
# r2 = Solution2().strangePrinter("dcdcdddabcaddcdcbdbcadadaddd")

r = Solution().strangePrinter("dcdcdddabcaddcdcbdbcadadadddac")
print(r)
# print(r2)
print(datetime.datetime.now() - start)