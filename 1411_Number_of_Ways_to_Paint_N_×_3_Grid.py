from functools import cache


class Solution:
    MOD = 10 ** 9 + 7

    def numOfWays(self, n: int) -> int:
        xyx, xyz = 6, 6
        for i in range(2, n + 1):
            new_xyx = (xyx * 3 + xyz * 2) % Solution.MOD
            new_xyz = (xyx * 2 + xyz * 2) % Solution.MOD
            xyx, xyz = new_xyx, new_xyz
        return (xyx + xyz) % Solution.MOD

r = Solution().numOfWays(5000)
print(r)
