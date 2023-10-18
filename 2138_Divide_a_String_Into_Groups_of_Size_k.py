from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = list[str]()
        division = ""
        for ch in s:
            division += ch
            if len(division) == k:
                ans.append(division)
                division = ""
        if len(division) > 0:
            division += fill * (k - len(division))
            ans.append(division)
        return ans