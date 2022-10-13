class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stk_outer, stk = [], []
        result = ""
        for ch in s:
            if ch == "(":
                if len(stk_outer) == 0:
                    stk_outer.append(ch)
                else:
                    result += ch
                    stk.append(ch)
            elif ch == ")":
                if len(stk) != 0:
                    result += ch
                    stk.pop()
                else:
                    stk_outer.pop()
        return result
