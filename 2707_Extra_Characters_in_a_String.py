from typing import List
import math

class Solution:

    def get_pos_info(self, s: str, word: str) -> list[list[int]]:
        res = []
        idx = 0
        while idx != -1:
            idx = s.find(word, idx)
            if idx == -1:
                break
            res.append([idx, idx + len(word) - 1])
            idx += 1
        return res

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        pos_arr = []
        for word in dictionary:
            arr = self.get_pos_info(s, word)
            pos_arr.extend(arr)
        pos_arr.sort(key=lambda x: [x[1], x[0]])
        dp = [math.inf] * len(s)
        for pos in pos_arr:
            dp[pos[1]] = int(min(pos[0], dp[pos[1]]))
            for i, dp_cost in enumerate(dp[: pos[0]]):
                dp[pos[1]] = int(min(pos[0] - i - 1 + dp_cost, dp[pos[1]]))
        ans = len(s)
        for i, cost in enumerate(dp):
            ans = min(ans, len(s) - i - 1 + cost)
        return ans

data = [
    "xp"
    , ["a","u","d","b","s","r","z","y","f","l","q","i","j","w","o","c"]
]
r = Solution().minExtraChar(*data)
print(r)