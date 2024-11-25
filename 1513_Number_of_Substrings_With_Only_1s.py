class Solution:
    def numSub(self, s: str) -> int:
        idx = 0
        ans = 0
        mod = 10 ** 9 + 7
        while idx < len(s):
            while idx < len(s) and s[idx] == '0':
                idx += 1
            one_cnt = 0
            while idx < len(s) and s[idx] == '1':
                one_cnt += 1
                idx += 1
            ans = (ans + (pow(one_cnt, 2, mod) + one_cnt) // 2) % mod
        return ans
        