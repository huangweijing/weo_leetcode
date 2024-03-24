class Solution:
    def reformat(self, s: str) -> str:
        num_stk, ch_stk = [], []
        for ch in s:
            if "0" <= ch <= "9":
                ch_stk.append(ch)
            else:
                num_stk.append(ch)
        if abs(len(num_stk) - len(ch_stk)) > 1:
            return ""
        elif len(num_stk) >= len(ch_stk):
            ans = ""
            while len(ch_stk) > 0:
                ans += num_stk.pop()
                ans += ch_stk.pop()
            ans += "" if len(num_stk) == 0 else num_stk.pop()
            return ans
        else:
            ans = ""
            while len(num_stk) > 0:
                ans += ch_stk.pop()
                ans += num_stk.pop()
            ans += "" if len(ch_stk) == 0 else ch_stk.pop()
            return ans



