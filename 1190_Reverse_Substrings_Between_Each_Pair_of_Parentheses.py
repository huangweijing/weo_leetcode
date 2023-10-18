class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch == ")":
                tmp_stk = []
                while len(stk) > 0:
                    ch2 = stk.pop()
                    if ch2 == "(":
                        stk.extend(tmp_stk)
                        break
                    else:
                        tmp_stk.append(ch2)
            else:
                stk.append(ch)
        return "".join(stk)


data = "(ab(cba)c)"
r = Solution().reverseParentheses(data)
print(r)
