from typing import List
from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        s_cnt = Counter(s)
        sl = list(reversed(sorted(list(s_cnt.keys()))))
        stk = []
        ans = ""
        for ch in s:
            while len(stk) > 0 and stk[-1] <= sl[-1]:
                ans += stk.pop()

            if ch == sl[-1]:
                ans += ch
            else:
                stk.append(ch)

            if s_cnt[ch] == 1:
                del s_cnt[ch]
                sl.remove(ch)
            else:
                s_cnt[ch] -= 1

            # print(ch, stk, ans)
        ans += "".join(reversed(stk))
        return ans


r = Solution().robotWithString("bydizfve")
# r = Solution().robotWithString("bac")
print(r)



