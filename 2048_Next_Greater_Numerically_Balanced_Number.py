import bisect
from collections import Counter

class Solution:
    def is_beautiful(self, k: int) -> bool:
        cnt = Counter(str(k))
        for key, v in cnt.items():
            if int(key) != v:
                return False
        return True

    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            if self.is_beautiful(n):
                return n

# print(Solution().is_beautiful(22))

r = Solution().nextBeautifulNumber(3000)
print(r)
