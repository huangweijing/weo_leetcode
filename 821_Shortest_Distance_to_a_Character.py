from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [math.inf] * len(s)
        distance = -1
        for i in range(len(s)):
            if s[i] == c:
                distance = 0
            else:
                if distance != -1:
                    distance += 1
            if distance != -1:
                ans[i] = min(ans[i], distance)

        distance = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                distance = 0
            else:
                if distance != -1:
                    distance += 1
            if distance != -1:
                ans[i] = min(ans[i], distance)

        return ans

