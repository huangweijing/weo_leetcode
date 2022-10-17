class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_cnt = num2.bit_count()
        bit_num1 = bin(num1)[2:]
        tmp_num = ""
        for ch in bit_num1:
            if ch == "1" and bit_cnt > 0:
                bit_cnt -= 1
                tmp_num += "1"
            else:
                tmp_num += "0"
        # print(bin(num2))
        # print(bin(num1), tmp_num, bit_cnt)
        result = ""
        for ch in reversed(tmp_num):
            if ch == "0" and bit_cnt > 0:
                result = "1" + result
                bit_cnt -= 1
            else:
                result = ch + result
        while bit_cnt > 0:
            bit_cnt -= 1
            result = "1" + result
        # print(result)
        return int(result, 2)

r = Solution().minimizeXor(25, 72)
print(r, r ^ 1)
