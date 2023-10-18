class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        stk = []
        for ch in s:
            if ch != " ":
                stk.append(ch)
            else:
                if len(ans) > 0:
                    ans += " "
                while len(stk) > 0:
                    ans += stk.pop()
        if len(ans) > 0:
            ans += " "
        while len(stk) > 0:
            ans += stk.pop()
        return ans
        # arr = s.split(sep=" ")
        # result = list[str]()
        # for word in arr:
        #     result.append(word[::-1])
        # return " ".join(result)
