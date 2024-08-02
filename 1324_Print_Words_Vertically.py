from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        max_len = max([len(word) for word in arr])
        ans = ["" for _ in range(max_len)]
        for i in range(max_len):
            for word in arr:
                if i >= len(word):
                    ans[i] += " "
                else:
                    ans[i] += word[i]
            ans[i] = ans[i].rstrip(" ")
        return ans
