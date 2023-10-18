from typing import List

class Expression:
    def __init__(self, expression: str):
        self.expression = expression
        self.children = []
        self.word = ""

    def parse(self, idx: int) -> int:
        raise NotImplemented(Expression.parse)

    def val(self) -> set[str]:
        raise NotImplemented(Expression.val)

class Word(Expression):
    def __init__(self, expression: str):
        super().__init__(expression)

    def parse(self, idx: int) -> int:
        while idx < len(self.expression) and "a" <= self.expression[idx] <= "z":
            self.word += self.expression[idx]
            idx += 1
        return idx

    def val(self) -> set[str]:
        return {self.word}


class CommaExp(Expression):
    def __init__(self, expression: str):
        super().__init__(expression)

    def parse(self, idx: int) -> int:
        if self.expression[idx] == "{":
            idx += 1
        exp = ProdExp(self.expression)
        idx = exp.parse(idx)
        while idx < len(self.expression):
            if self.expression[idx] == "}":
                self.children.append(exp)
                idx += 1
                break
            elif self.expression[idx] == ",":
                self.children.append(exp)
                idx += 1
            else:
                exp = ProdExp(self.expression)
                idx = exp.parse(idx)
        return idx

    def val(self) -> set[str]:
        ret = set[str]()
        for exp in self.children:
            for v in exp.val():
                ret.add(v)
        return ret

class ProdExp(Expression):
    def __init__(self, expression: str):
        super().__init__(expression)

    def val(self) -> set[str]:
        stk = self.children.copy()
        ret = None
        while len(stk) > 0:
            exp = stk.pop()
            exp_val_list = exp.val()
            if ret is None:
                ret = exp_val_list.copy()
            else:
                new_ret = set[str]()
                for exp_val in exp_val_list:
                    for ret_val in ret:
                        new_ret.add(exp_val + ret_val)
                ret = new_ret
        return ret


    def parse(self, idx: int) -> int:
        while idx < len(self.expression):
            if "a" <= self.expression[idx] <= "z":
                exp = Word(self.expression)
                idx = exp.parse(idx)
                self.children.append(exp)
            elif "{" == self.expression[idx]:
                exp = CommaExp(self.expression)
                idx = exp.parse(idx)
                self.children.append(exp)
            else:
                break
        return idx

class Solution:
    def __init__(self):
        self.expression = ""

    def braceExpansionII(self, expression: str) -> List[str]:
        self.expression = expression
        exp = ProdExp(expression)
        exp.parse(0)
        # print(exp.children, exp.word)
        ans = list(exp.val())
        ans.sort()
        return ans


r = Solution().braceExpansionII("g{a,b}{c,d}{e,f}bc")
print(r)
