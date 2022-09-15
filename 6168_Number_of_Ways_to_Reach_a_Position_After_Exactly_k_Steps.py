from functools import cache

class Solution:
    MODULO = 10 ** 9 + 7

    @cache
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        result = 0
        if k < 0:
            result = 0
        elif endPos - startPos - k > 0:
            result = 0
        elif (endPos - startPos - k) & 1 == 1:
            result = 0
        elif endPos - startPos - k == 0:
            result = 1
        else:
            result += self.numberOfWays(startPos - 1, endPos, k - 1)
            result += self.numberOfWays(startPos + 1, endPos, k - 1)
        # print(f"startPos={startPos}, endPos={endPos}, k={k}, result={result}")
        return result % Solution.MODULO

r = Solution().numberOfWays(2, 8, 1000)
print(r)