class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        ans, i = 0, 0
        while i < len(s):
            zero_cnt, one_cnt = 0, 0
            while i < len(s) and s[i] == "0":
                zero_cnt += 1
                i += 1
            while i < len(s) and s[i] == "1":
                one_cnt += 1
                i += 1
            ans = max(min(zero_cnt, one_cnt) * 2, ans)
        return ans