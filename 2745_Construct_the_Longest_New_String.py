from functools import cache

class Solution:

    @cache
    def my_sol(self, x: int, y: int, z: int, last_ch: str) -> int:

        if last_ch == "x":
            s1 = s2 = s3 = 0
            if y > 0:
                s2 = self.my_sol(x - 1, y, z, "y")
            if z > 0:
                s3 = self.my_sol(x - 1, y, z, "z")
            return max(s1, s2, s3) + 1
        elif last_ch == "y":
            if x > 0:
                s1 = self.my_sol(x, y - 1, z, "x")
                return s1 + 1
        else:
            s1 = s2 = 0
            if y > 0:
                s1 = self.my_sol(x, y, z - 1, "y")
            if z - 1 > 0:
                s2 = self.my_sol(x, y, z - 1, "z")
            return max(s1, s2) + 1
        return 1

    def longestString(self, x: int, y: int, z: int) -> int:
        s1 = s2 = s3 = 0
        if x > 0:
            s1 = self.my_sol(x, y, z, "x")
        if y > 0:
            s2 = self.my_sol(x, y, z, "y")
        if z > 0:
            s3 = self.my_sol(x, y, z, "z")
        return max(s1, s2, s3) * 2

data = [
    3, 2, 2
]
r = Solution().longestString(* data)
print(r)