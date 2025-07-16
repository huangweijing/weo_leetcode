class Solution:
    def minus(self, a: int, b: int, limit: int) -> int:
        dec_a, dec_b = 0, 0
        for i, ch in enumerate(reversed(str(a))):
            dec_a += int(ch) * (limit + 1) ** i
        for i, ch in enumerate(reversed(str(b))):
            dec_b += int(ch) * (limit + 1) ** i
        print(dec_a, dec_b)
        return dec_a - dec_b
    
    def next_big(self, num: int, limit: int) -> int:
        str_num = str(num)
        new_str_num = ""
        plus_val = 0
        for ch in reversed(str_num):
            if int(ch) + plus_val > limit:
                new_str_num = "0" * (len(new_str_num) + 1)
                plus_val = 1
            else:
                new_str_num = str(int(ch) + plus_val) + new_str_num
                plus_val = 0
        if plus_val > 0:
            new_str_num = str(plus_val) + new_str_num
        return int(new_str_num)



    def numberOfPowerfulInt(self, num: int, finish: int, limit: int, s: str) -> int:
        for ch in s:
            if int(ch) > limit:
                return 0
        str_finish = str(finish)
        new_str_finish = ""
        for ch in reversed(str_finish):
            if int(ch) > limit:
                new_str_finish = str(limit) * (len(new_str_finish) + 1)
            else:
                new_str_finish = ch + new_str_finish
                plus_val = 0
        new_str_num = ""
        str_num = str(num)
        plus_val = 0
        for ch in reversed(str_num):
            if int(ch) + plus_val > limit:
                new_str_num = "0" * (len(new_str_num) + 1)
                plus_val = 1
            else:
                new_str_num = str(int(ch) + plus_val) + new_str_num
                plus_val = 0
        if plus_val > 0:
            new_str_num = str(plus_val) + new_str_num

        new_num, new_finish = 0, 0
        if len(new_str_num) > len(s):
            new_num = int(new_str_num[:-len(s)])
        elif int(new_str_num) > int(s):
            new_num = 1
        if len(new_str_finish) > len(s):
            new_finish = int(new_str_finish[:-len(s)])
        elif int(new_str_finish) > int(s):
            finish = 1
        print(new_num, new_finish)
        print("minus: ", self.minus(new_num, new_finish, limit))
        
        


# print(Solution().minus(111, 11, 1))

data = [
    4333393
    , 2522
    , 4
    , "123"
]
r = Solution().numberOfPowerfulInt(*data)
print(r)