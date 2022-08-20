class Solution:
    def my_first_bad(self, n: int, m: int) -> int:

        # b b b b
        if isBadVersion(n):
            return n
        # nb nb nb
        if not isBadVersion(m):
            return -1
        # nb b
        if n + 1 == m:
            return m

        mid = (n + m) >> 1
        if isBadVersion(mid):
            left_bad = self.my_first_bad(n, mid - 1)
            if left_bad == -1:
                return mid
            else:
                return left_bad
        else:
            return self.my_first_bad(mid, m)

    def firstBadVersion(self, n: int) -> int:
        return self.my_first_bad(1, n)
