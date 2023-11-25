class Solution:
    def countHomogenous(self, s: str) -> int:
        idx= 0
        ans = 0
        while idx < len(s):
            last_ch = s[idx]
            cons_len = 0
            while idx < len(s) and s[idx] == last_ch:
                cons_len += 1
                idx += 1
            ans += cons_len * (cons_len + 1) // 2
            ans %= 10 ** 9 + 7

        return ans

r = Solution().countHomogenous("xxx88888y")
print(r)
