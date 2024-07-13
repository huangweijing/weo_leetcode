class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        for ch in s:
            if ch == "(":
                stk.append("(")
            elif ch == ")":
                if stk[-1] == "(":
                    stk.pop()
                    stk.append(1)
                else:
                    val = 0
                    while len(stk) > 0 and stk[-1] != "(":
                        val += stk.pop()
                    stk.pop()
                    stk.append(val * 2)
            # print(stk)
        return sum(stk)


data = "(()(()))"
r = Solution().scoreOfParentheses(data)
print(r)