from typing import List
from functools import cache


class Solution:

    def __init__(self) -> None:
        self.num = ""
        self.ans = []
        self.target = 0


    def my_sol(self, idx: int, fixed_res: int, unfixed_res: int, last_sig: int, exp: str):
        if idx == len(self.num) - 1:
            # print(fixed_res, last_sig * unfixed_res * int(self.num[idx]), exp)
            if fixed_res + last_sig * unfixed_res * int(self.num[idx]) == self.target:
                self.ans.append(exp + "*" + self.num[idx])
            if fixed_res + last_sig * unfixed_res + int(self.num[idx]) == self.target:
                self.ans.append(exp + "+" + self.num[idx])
            if fixed_res + last_sig * unfixed_res - int(self.num[idx]) == self.target:
                self.ans.append(exp + "-" + self.num[idx])
            return
        num_str = self.num[idx: ]
        if not (len(num_str) > 1 and num_str[0] == "0"):
            if fixed_res + last_sig * unfixed_res * int(num_str) == self.target:
                self.ans.append(exp + "*" + num_str)
            if fixed_res + last_sig * unfixed_res + int(num_str) == self.target:
                self.ans.append(exp + "+" + num_str)
            if fixed_res + last_sig * unfixed_res - int(num_str) == self.target:
                self.ans.append(exp + "-" + num_str)
        for i in range(1, len(self.num) - idx):
            num_str = self.num[idx: idx + i]
            if len(num_str) > 1 and num_str[0] == "0":
                continue
            self.my_sol(idx + i, fixed_res, unfixed_res * int(num_str), last_sig, exp + "*" + num_str)
            self.my_sol(idx + i, fixed_res + last_sig * unfixed_res, int(num_str), 1, exp + "+" + num_str)
            self.my_sol(idx + i, fixed_res + last_sig * unfixed_res, int(num_str), -1, exp + "-" + num_str)


    def addOperators(self, num: str, target: int) -> List[str]:
        self.num = num
        self.target = target
        if int(num) == target:
            if not (len(num) > 1 and num[0] == "0"):
                self.ans.append(num)
        for i in range(1, len(num)):
            num_str = num[: i]
            if len(num_str) > 1 and num_str[0] == "0":
                continue
            self.my_sol(i, 0, int(num_str), 1, num_str)
        return self.ans
    

r = Solution().addOperators("000", 0)
print(r)