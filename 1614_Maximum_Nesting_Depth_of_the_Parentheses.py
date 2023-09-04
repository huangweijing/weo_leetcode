class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        stk = []
        for ch in s:
            if ch == "(":
                stk.append(ch)
            elif ch == ")":
                stk.pop()
            ans = max(ans, len(stk))
        return ans