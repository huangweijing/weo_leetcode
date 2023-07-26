from functools import cache
import math

class Solution:

    FIVE_STR = [
        "1"
        ,"101"
        ,"11001"
        ,"1111101"
        ,"1001110001"
        ,"110000110101"
        ,"11110100001001"
    ]

    def __init__(self):
        self.s = ""
        self.five_str_dict = dict[int, str]()
        for five_str in Solution.FIVE_STR:
            self.five_str_dict[len(five_str)] = five_str

    @cache
    def cmp(self, start_idx: int, length: int) -> bool:
        if length not in self.five_str_dict:
            return False
        return self.s[start_idx: start_idx + length] == self.five_str_dict[length]

    @cache
    def my_sol(self, start_idx: int) -> int:
        if self.cmp(start_idx, len(self.s) - start_idx):
            return 1
        ans = math.inf
        for length, val in self.five_str_dict.items():
            if self.cmp(start_idx, length):
                ans = min(self.my_sol(start_idx + length) + 1, ans)
        return ans

    def minimumBeautifulSubstrings(self, s: str) -> int:
        self.s = s
        ans = self.my_sol(0)
        if ans == math.inf:
            return -1
        return ans

data = "0"
r = Solution().minimumBeautifulSubstrings(data)
print(r)




