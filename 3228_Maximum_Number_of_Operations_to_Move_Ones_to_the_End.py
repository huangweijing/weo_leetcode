class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        one_cnt = 0
        last_ch = "x"
        for ch in s:
            if ch == "1":
                one_cnt += 1
            elif last_ch != ch and ch == "0":
                ans += one_cnt
            last_ch = ch
        return ans

