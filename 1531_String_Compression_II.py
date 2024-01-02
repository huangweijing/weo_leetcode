from collections import defaultdict
import math

class Solution:
    def group(self, s: str) -> list[[str, int]]:
        idx = 0
        ret = list[str, int]()
        while idx < len(s):
            ch = s[idx]
            cnt = 0
            while idx < len(s) and s[idx] == ch:
                cnt += 1
                idx += 1
            ret.append([ch, cnt])
        return ret

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        ans = math.inf
        dp = [[0] * 101 for _ in range(27)]
        dp[27][0] = 0
        g_arr = self.group(s)
        for i, arr in enumerate(g_arr):
            new_dp = [[0] * 101 for _ in range(27)]
            # 1. delete all


        return ans

data = [
    "aababbaaa"
    , 3
]
r = Solution().getLengthOfOptimalCompression(* data)
print(r)








