from collections import Counter


class Solution:
    def __init__(self):
        self.s = ""
        self.k = 0

    def substr_exists(self, strlen: int) -> bool:
        cnt = Counter(self.s[: strlen])
        # print(cnt, strlen)
        ret = True
        for v in cnt.values():
            if v < self.k:
                ret = False
        if ret:
            print(strlen, "is okay1")
            return ret
        idx = 0
        for ch in self.s[strlen:]:
            cnt[self.s[idx]] -= 1
            if cnt[self.s[idx]] == 0:
                del cnt[self.s[idx]]
            cnt[ch] += 1
            idx += 1
            ret = True
            for v in cnt.values():
                if v < self.k:
                    ret = False
            if ret:
                print(strlen, "is okay")
                return ret
        return False

    def longestSubstring(self, s: str, k: int) -> int:
        self.s, self.k = s, k
        left, right = k, len(s)
        mid = (left + right) >> 1
        while left < right:
            print(mid)
            s1 = self.substr_exists(mid)
            s2 = self.substr_exists(mid + 1)
            if s1 and not s2:
                return mid
            elif s1 and s2:
                left = mid + 1
            elif not s1 and not s2:
                right = mid - 1
            mid = (left + right) >> 1
        return mid


data = [
    "aaabbb"
    , 3
]
r = Solution().longestSubstring(*data)
print(r)