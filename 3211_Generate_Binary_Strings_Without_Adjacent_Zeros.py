from typing import List
from functools import cache


class Solution:
    @cache
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1"]
        sub_ans = self.validStrings(n - 1)
        ans = []
        for s in sub_ans:
            if s[0] != "0":
                ans.append("0" + s)
            ans.append("1" + s)
        return ans

