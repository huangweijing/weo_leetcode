class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        for i in range(32):
            if (n & (1 << i)) >> i == 1:
                result += 1
        return result

r = Solution().hammingWeight(0b00000000000000000000000000001011)
print(r)