from collections import Counter

class Solution:
    def __init__(self) -> None:
        self.equation = ""
        self.idx = 0

    def read_int(self) -> int:
        has_int = False
        ret = 0
        while self.idx < len(self.equation) and '0' <= self.equation[self.idx] <= '9':
            ret *= 10
            ret += int(self.equation[self.idx])
            self.idx += 1
            has_int = True
        if has_int:
            return ret
        else:
            return None
    
    def read_x(self) -> int:
        coef = self.read_int()
        if coef is None:
            coef = 1
        if self.equation[self.idx] == "x":
            self.idx += 1
        return False
    
    def read_word(self) -> tuple[str, int]:
        sign = self.read_sign()
        coef = self.read_int()
        if coef is None:
            coef = 1
        if self.idx < len(self.equation) and self.equation[self.idx] == "x":
            self.idx += 1
            return "x", coef * sign
        else:
            return "num", coef * sign


    def read_sign(self) -> int:
        if self.equation[self.idx] == "+":
            self.idx += 1
            return 1
        elif self.equation[self.idx] == "-":
            self.idx += 1
            return -1
        else:
            return 1

    def read_sect(self) -> dict[str, int]:
        ret = Counter()
        while self.idx < len(self.equation) and self.equation[self.idx] != "=":
            sect = self.read_word()
            ret[sect[0]] += sect[1]
        return ret
        

    def solveEquation(self, equation: str) -> str:
        self.equation = equation
        sec1 = self.read_sect()
        self.idx += 1
        sec2 = self.read_sect()
        x_cnt = sec1["x"] - sec2["x"]
        num_cnt = sec2["num"] - sec1["num"]
        if x_cnt == 0:
            if num_cnt == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return f"x={int(num_cnt//x_cnt)}"

r = Solution().solveEquation("x+5-3+x=6+x-2")
print(r)