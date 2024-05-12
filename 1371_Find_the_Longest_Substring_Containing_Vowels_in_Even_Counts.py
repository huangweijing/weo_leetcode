from collections import Counter


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vow_map = {
            "a": 0,
            "i": 1,
            "u": 2,
            "e": 3,
            "o": 4
        }
        ans = 0
        cnt = Counter()
        cnt[0] = -1
        mask = 0
        for i, ch in enumerate(s):
            if ch in vow_map:
                mask ^= 1 << vow_map[ch]
            # print(i, bin(mask))
            if mask in cnt:
                ans = max(ans, i - cnt[mask])
            else:
                cnt[mask] = i
        return ans


data = "eleetminicoworoep"
r = Solution().findTheLongestSubstring(data)
print(r)