class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int
                                  , c: int, d: int, e: int, f: int) -> int:
        if (a == e and b == f) or (c == e and d == f):
            return 0
        if b == f:
            if d == f and abs(c - a) + abs(c - e) == abs(e - a):
                return 2
            else:
                return 1
        if a == e:
            if c == e and abs(d - b) + abs(d - f) == abs(f - b):
                return 2
            else:
                return 1
        if abs(e - c) == abs(f - d):
            c1, d1 = e - c, f - d
            a1, b1 = e - a, f - b
            # print("hey", c1 / a1, c1, d1, a1, b1)
            if 0 < a1 / c1 < 1 and c1 * b1 == a1 * d1:
                return 2
            else:
                return 1
        return 2


data = [4
    , 3
    , 3
    , 4
    , 5
    , 2]
r = Solution().minMovesToCaptureTheQueen(* data)
print(r)