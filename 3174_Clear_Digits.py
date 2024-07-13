class Solution:
    def clearDigits(self, s: str) -> str:
        stk = list(s)
        ans = ""
        dig_cnt = 0
        while len(stk) > 0:
            ch = stk.pop()
            if "0" <= ch <= "9":
                dig_cnt += 1
            else:
                if dig_cnt > 0:
                    dig_cnt -= 1
                else:
                    ans = ch + ans
        return ans



