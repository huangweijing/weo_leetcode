class Calculator:
    def __init__(self, exp: str) -> None:
        self.exp = exp
        self.idx = 0

    def read_num(self) -> int:
        ret = 0
        while self.idx <len(self.exp):
            if '0' <= self.exp[self.idx] <= '9':
                ret = ret * 10 + int(self.exp[self.idx])
            else:
                break
            self.idx += 1
        return ret
    
    def read_exp(self) -> int:
        if self.idx >= len(self.exp):
            return 0
        signal, val = 1, 0
        if self.exp[self.idx] in ("+", "-"):
            if self.exp[self.idx] == "-":
                signal = -1
            self.idx += 1
        if self.exp[self.idx] == "(":
            self.idx += 1
            val = self.read_exp()
            self.idx += 1
        elif "0" <= self.exp[self.idx] <= "9":
            val = self.read_num()
        elif self.exp[self.idx] == ")":
            return signal * val
        return signal * val + self.read_exp()
            

class Solution:

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        return Calculator(exp=s).read_exp()

print(Calculator(exp="(1+(4+5+2)-3)+(6+8)").read_exp())