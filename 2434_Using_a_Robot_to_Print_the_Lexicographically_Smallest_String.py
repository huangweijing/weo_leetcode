from typing import List

class Solution:
    def robotWithString(self, s: str) -> str:
        stk = []
        for ch in s:
            ch_str = ch
            while len(stk) > 0 and ch_str < stk[-1]:
                ch_str += stk.pop()
            stk.append(ch_str)
            print(stk)
        return "".join(stk)

r = Solution().robotWithString("bydizfve")
print(r)



