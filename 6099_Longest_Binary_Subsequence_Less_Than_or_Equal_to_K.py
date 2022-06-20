class Solution:
    def __init__(self):
        self.cache = [None] * 1001

    def ls(self, s: str, n: int, k: int) -> str:
        if n == len(s):
            return ""
        ls_n_1 = self.ls(s, n + 1, k)
        a_try = s[n] + ls_n_1
        if s[n] == "0":
            return a_try
        # for idx in len(ls_n_1):

        a_try_num = int(a_try, 2)
        if k >= a_try_num:
            return a_try
        else:
            return ls_n_1

    def longestSubsequence(self, s: str, k: int) -> int:
        return len(self.ls(s, 0, k))

sol = Solution()
data = "100010001101"
r = sol.ls(data, 0, 14)
print(r)