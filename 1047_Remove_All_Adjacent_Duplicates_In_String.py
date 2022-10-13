class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for ch in s:
            if len(stk) > 0 and ch == stk[-1]:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)
