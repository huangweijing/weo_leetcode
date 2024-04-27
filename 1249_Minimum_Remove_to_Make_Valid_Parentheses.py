class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        ans = []
        for ch in s:
            if ch not in ["(", ")"]:
                ans.append(ch)
            else:
                if ch == ")":
                    if len(stk) == 0:
                        continue
                    else:
                        stk.pop()
                        ans.append(ch)
                elif ch == "(":
                    stk.append(len(ans))
                    ans.append(ch)
        for idx in stk:
            ans[idx] = ""
        return "".join(ans)




