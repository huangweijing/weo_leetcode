from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [" "] * len(indices)
        for i, idx in enumerate(indices):
            ans[idx] = s[i]
        return "".join(ans)