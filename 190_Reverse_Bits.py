class Solution:
    def reverseBits(self, n: int) -> int:
        bits = [0] * 32
        for i in range(len(bits)):
            bits[-i - 1] = (n & (1 << i)) >> i
        result = 0
        for i in range(len(bits)):
            result += bits[i] * (1 << i)
        if result & (1 << 31) != 0:
            result -= (1 << 31)
        return result

r = Solution().reverseBits(3)
print(r)

print(0b10111111111111111111111111111111)
