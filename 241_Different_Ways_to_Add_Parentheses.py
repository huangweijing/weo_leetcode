from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.dp = dict[str, list[int]]()

    def exp_to_arr(self, expression: str) -> (list[int], list[str]):
        num = -1
        num_arr = []
        exp_arr = []
        for ch in expression:
            if '0' <= ch <= '9':
                if num == -1:
                    num = (ord(ch) - ord("0"))
                    num_arr.append(num)
                else:
                    num = num * 10 + (ord(ch) - ord("0"))
                    num_arr[-1] = num
            else:
                num = -1
                exp_arr.append(ch)
        return num_arr, exp_arr

    # @cache
    def my_diff_way(self, num_arr, exp_arr) -> list[int]:
        key = ".".join(map(str, num_arr)) + "".join(exp_arr)
        if key in self.dp:
            return self.dp[key]
        # print(num_arr, exp_arr)
        result = []
        if len(num_arr) == 1:
            result = [num_arr[0]]
        else:
            for i, exp in enumerate(exp_arr):
                sub1 = self.my_diff_way(num_arr[:i + 1], exp_arr[:i])
                sub2 = self.my_diff_way(num_arr[i + 1:], exp_arr[i + 1:])
                if exp == "*":
                    for n1 in sub1:
                        for n2 in sub2:
                            result.append(n1 * n2)
                if exp == "+":
                    for n1 in sub1:
                        for n2 in sub2:
                            result.append(n1 + n2)
                if exp == "-":
                    for n1 in sub1:
                        for n2 in sub2:
                            result.append(n1 - n2)
        # print(num_arr, exp_arr, result)
        self.dp[key] = result
        return result

    def diffWaysToCompute(self, expression: str) -> List[int]:
        num_arr, exp_arr = self.exp_to_arr(expression)
        return self.my_diff_way(num_arr, exp_arr)

data_exp = "2*234+1"
r = Solution().diffWaysToCompute(data_exp)
print(r)





