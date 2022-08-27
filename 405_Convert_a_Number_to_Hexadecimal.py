class Solution:
    HEX_DEF = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    CHAR_CNT = 8
    def toHex(self, num: int) -> str:
        ch_cnt = 0
        result = list[str]()
        while ch_cnt < Solution.CHAR_CNT:
            hex_num = num & 0xf
            result.append(Solution.HEX_DEF[hex_num])
            num >>= 4
            ch_cnt += 1
        while len(result) > 1 and result[-1] == "0":
            result.pop()
        result.reverse()
        return "".join(result)

r = Solution().toHex(0)
print(r)

# print(-15 & 0xf)