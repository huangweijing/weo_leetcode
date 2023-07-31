bbb = "abcdadf"

# def m(t:str):
#     for i in t:
#         print(t.count(i))
#         if t.count(i) == 1:
#             return i
#         else:
#             return "no"
# print(m(bbb))

class Solution:
    def __init__(self):
        self.largest_tbl: list[int] = []
        self.cache = [None] * 10000

    def lis(self, arr: list[int], arr_len) -> list[int]:
        if arr_len in self.cache:
            return self.cache[arr_len]
        if arr_len == 1:
            return [arr[0]]

        # print(arr, self.largest_tbl, arr_len - 1)
        if arr[arr_len - 1] == self.largest_tbl[arr_len - 1]:
            n_1_result = self.lis(arr, arr_len - 1)
            result = n_1_result.copy()
            result.append(arr[arr_len - 1])
        else:
            result = self.lis(arr, arr_len - 1).copy()

        self.cache[arr_len] = result
        return result

    def get_list(self, arr: list[int]):
        maximum = -1
        for i in arr:
            if i > maximum:
                maximum = i
            self.largest_tbl.append(maximum)
        # print(self.largest_tbl)
        # print(self.lis(arr, len(arr)))
        return self.lis(arr, len(arr))

# sol = Solution()
# r = sol.get_list([1, 4, 2, 7, 8, 9, 2, 1, 3, 8, 6, 5])
# print(r)


from functools import cache
import math

class Solution:
    def __init__(self):
        self.s = ""

    @cache
    def my_sol(self, s: str) -> int:
        # if s == "aca":
        #     print("aaaaaaaaaaaaaaa")
        if len(s) == 0:
            return 0
        res = math.inf
        for i, ch in enumerate(s):
            # if s == "abca":
                # print(s, f"i={i}" ":", s[:i] + s[i + 1:], self.my_sol(s[:i] + s[i + 1:]))
            if 0 < i < len(s) - 1:
                if s[i - 1] == s[i + 1]:
                    res = min(res, self.my_sol(s[:i - 1] + s[i + 1:]) + 1)
                else:
                    res = min(res, self.my_sol(s[:i] + s[i + 1:]) + 1)
            else:
                # sub_sol = self.my_sol(s[:i] + s[i + 1:])
                # if sub_sol + 1 < res:
                #     print(sub_sol)
                res = min(res, self.my_sol(s[:i] + s[i + 1:]) + 1)
                if s == "cdcdabcadcdcbdbcadadadac" and res == 13:
                    print(s[:i],s[i], s[i + 1:])
                # print(s[:i], s[i + 1:], res)
        # print(s, res)
        return res


    def convert_s(self, s: str) -> str:
        new_s = ""
        old_ch = ""
        for ch in s:
            if ch != old_ch:
                new_s += ch
            old_ch = ch
        return new_s

    def strangePrinter(self, s: str) -> int:
        new_s = self.convert_s(s)
        print(new_s)
        return self.my_sol(new_s)


r = Solution().strangePrinter("cdcdabcadcdcbdbcadadadac")
print(r)