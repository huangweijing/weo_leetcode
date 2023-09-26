class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        ax, ay = abs(fx - sx), abs(fy - sy)
        if ax == ay == 0 and t == 1:
            return False
        return t >= max(ax, ay)
