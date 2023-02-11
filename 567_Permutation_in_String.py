from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_cnt = Counter(s1)
        s2_cnt = Counter(s2[: len(s1)])
        if s1_cnt == s2_cnt:
            return True
        for i in range(len(s1), len(s2)):
            s2_cnt[s2[i]] += 1
            s2_cnt[s2[i - len(s1)]] -= 1
            if s1_cnt == s2_cnt:
                return True
        return False

data = [
    "a"
    , "ab"
]
r = Solution().checkInclusion(* data)
print(r)
