class Solution:
    HEX_DEF = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    def toHex(self, num: int) -> str:
        dig = 0
        max_ch = 7
        while num > 0 or num < -1: #or dig != 0 or max_ch > 0:
            dig = num & 0xf
            print(dig)
            num >>= 4
            max_ch -= 1

# r = Solution().toHex(155)

print(-15 & 0xf)