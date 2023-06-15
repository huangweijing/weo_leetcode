class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        bin_a, bin_b, bin_c = list(bin(a)[2:]), list(bin(b)[2:]), list(bin(c)[2:])
        ans = 0
        while len(bin_a) > 0 or len(bin_b) > 0 or len(bin_c) > 0:
            a_bit, b_bit, c_bit = 0, 0, 0
            if len(bin_a) > 0:
                a_bit = int(bin_a.pop())
            if len(bin_b) > 0:
                b_bit = int(bin_b.pop())
            if len(bin_c) > 0:
                c_bit = int(bin_c.pop())
            if a_bit | b_bit == c_bit:
                continue
            else:
                if c_bit == 0:
                    ans += a_bit + b_bit
                else:
                    ans += 1
        return ans


r = Solution().minFlips(8, 3, 5)
print(r)