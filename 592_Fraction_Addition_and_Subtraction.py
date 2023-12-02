import math

class Solution:
    def fractionAddition(self, expression: str) -> str:
        exp = list(expression)
        idx = 0
        den, num = 1, 0
        while idx < len(exp):
            #sign
            sign = "+"
            if exp[idx] == "-":
                idx += 1
                sign = "-"
            elif exp[idx] == "+":
                idx += 1
            new_num, new_den = 0, 0
            while "0" <= exp[idx] <= "9":
                new_num = new_num * 10 + int(exp[idx])
                idx += 1
            idx += 1
            while idx < len(exp) and "0" <= exp[idx] <= "9":
                new_den = new_den * 10 + int(exp[idx])
                idx += 1
            # print(f"{sign}{new_num}/{new_den},{num}/{den}")
            if sign == "+":
                num = num * new_den + den * new_num
            else:
                num = num * new_den - den * new_num
            den = new_den * den
            gcd = math.gcd(num, den)
            num = num // gcd
            den = den // gcd
        return f"{num}/{den}"

r = Solution().fractionAddition("1/3-1/2")
print(r)