from collections import Counter

class Solution:
    def minFlips(self, target: str) -> int:
        target = str(int(target))
        if target == "0":
            return 0
        idx = 0
        mode = ""
        ans = 0
        while idx < len(target):
            if target[idx] != mode:
                ans += 1
                mode = target[idx]
            idx += 1
        return ans

from itertools import groupby
print(list(groupby("aaaacc")))