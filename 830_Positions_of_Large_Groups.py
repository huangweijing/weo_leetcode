from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        idx = 0
        ans = []
        while idx < len(s):
            ch = s[idx]
            forward = idx
            while forward < len(s) and s[forward] == ch:
                forward += 1
            # print(idx, forward)
            if forward - idx >= 3:
                ans.append([idx, forward - 1])
            idx = forward
        return ans

r = Solution().largeGroupPositions("abbxxxxzzy")
print(r)