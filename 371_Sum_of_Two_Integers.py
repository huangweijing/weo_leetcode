class Solution:
    MAX_BIT_CNT = 12

    def getSum(self, a: int, b: int) -> int:
        carry_bit = 0
        result = 0
        bit_cnt = 0
        while True:
            bit_a = a & 1
            bit_b = b & 1
            cur_bit = bit_a ^ bit_b
            cur_bit = carry_bit ^ cur_bit
            carry_bit = (bit_a & bit_b) | (bit_a & carry_bit) | (bit_b & carry_bit)
            result = (cur_bit << bit_cnt) | result
            a >>= 1
            b >>= 1
            bit_cnt += 1
            if bit_cnt > Solution.MAX_BIT_CNT:
                break

        if result & (1 << Solution.MAX_BIT_CNT) == (1 << Solution.MAX_BIT_CNT):
            return (-1 << Solution.MAX_BIT_CNT << 1) | result

        return result

r = Solution().getSum(-1000, -1000)
print(r)
# print(bin((0xffff & -4) >> 1))
# print( ~0 )
