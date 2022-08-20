class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg_flg = num < 0
        if neg_flg:
            num = -num
        result = ""
        while num != 0:
            result = str(num % 7) + result
            num = int(num / 7)
        if neg_flg:
            result = "-" + result
        return result

r =Solution().convertToBase7(10**7)
print(r)
