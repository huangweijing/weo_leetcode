from typing import List

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for word in strs:
            if word.isdigit():
                ans = max(int(word), ans)
            else:
                ans = max(len(word), ans)
        return ans

print("1a01".isdigit())