class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        ans = 0
        if x > y:
            stk = []
            for ch in s:
                # print("".join(stk), ch, ans)
                if ch == "b" and len(stk) > 0 and stk[-1] == "a":
                    stk.pop()
                    ans += x
                else:
                    stk.append(ch)
            stk2 = []
            for ch in stk:
                # print("".join(stk2), ch, ans)
                if ch == "a" and len(stk2) > 0 and stk2[-1] == "b":
                    stk2.pop()
                    ans += y
                else:
                    stk2.append(ch)
            # print(stk2)
        else:
            stk = []
            for ch in s:
                if ch == "a" and len(stk) > 0 and stk[-1] == "b":
                    stk.pop()
                    ans += y
                else:
                    stk.append(ch)
                # print(stk)
            stk2 = []
            for ch in stk:
                if ch == "b" and len(stk2) > 0 and stk2[-1] == "a":
                    stk2.pop()
                    ans += x
                else:
                    stk2.append(ch)
                # print(stk, stk2)
        return ans


data = [
    "bbbaaa"
    , 4
    , 3
]
r = Solution().maximumGain(*data)
print(r)

