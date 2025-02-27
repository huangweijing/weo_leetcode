from collections import Counter


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = list[list[int]]()
        for ch in s:
            if len(stk) > 0:
                if ch == stk[-1][0]:
                    stk[-1][1] += 1
                    if stk[-1][1] == k:
                        stk.pop()
                else:
                    stk.append([ch, 1])
            else:
                stk.append([ch, 1])
        ans = ""
        for rec in stk:
            ans += rec[0] * rec[1]
        return ans
    

data = [
    "abbbccbd"
    , 2
]
r = Solution().removeDuplicates(*data)
print(r)