class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        stk = []
        while n != 1:
            next_n = (n // -2)
            if next_n * -2 > n:
                next_n += 1
            stk.append(n - next_n * (-2))
            n = next_n
        stk.append(1)
        return "".join(map(str, reversed(stk)))

r = Solution().baseNeg2(3)
print(r)