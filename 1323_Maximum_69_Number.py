class Solution:
    def maximum69Number(self, num: int) -> int:
        str_num = str(num)
        idx = str_num.find("6")
        if idx == -1:
            return num
        else:
            return int(str_num[:idx] + "9" + str_num[idx:])
