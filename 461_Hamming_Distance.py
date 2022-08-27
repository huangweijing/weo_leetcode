class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask = 1 << 30
        result = 0
        while mask > 0:
            if (mask & x) ^ (mask & y) == mask:
                result += 1
            # print(result)
            mask >>= 1
        return result

r = Solution().hammingDistance(99999, 5151)
print(r)