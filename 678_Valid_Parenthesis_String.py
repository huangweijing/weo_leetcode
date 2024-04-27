class Solution:
    def checkValidString(self, s: str) -> bool:
        stk = []
        for ch in s:
            if ch == ")":
                if len(stk) > 0 and stk[-1] == "(":
                    stk.pop()
                elif len(stk) > 1 and stk[-2] == "(" and stk[-1] not in (")", "("):
                    val = stk.pop()
                    stk.pop()
                    if len(stk) > 1 and stk[-1] not in (")", "("):
                        stk[-1] += val
                    else:
                        stk.append(val)
                elif len(stk) > 0 and stk[-1] not in ("(", ")"):
                    stk[-1] -= 1
                    if stk[-1] == 0:
                        stk.pop()
                else:
                    return False
            elif ch == "(":
                stk.append(ch)
            elif ch == "*":
                if len(stk) > 0 and stk[-1] not in ("(", ")"):
                    stk[-1] += 1
                else:
                    stk.append(1)
            # print(ch, stk)
        final_stk = []
        for ch in stk:
            if ch != "(":
                if len(final_stk) < ch:
                    final_stk.clear()
                else:
                    for i in range(ch):
                        final_stk.pop()
            else:
                final_stk.append(ch)
        if len(final_stk) > 0:
            return False
        return True

data = "(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)"
r = Solution().checkValidString(data)
print(r)
