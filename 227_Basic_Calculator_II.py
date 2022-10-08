from collections import deque

class Solution:
    def __init__(self):
        self.s = ""
        self.ptr = 0

    def read_int(self) -> int:
        s = self.s
        idx = self.ptr
        result = 0
        while idx < len(s):
            if "0" <= s[idx] <= "9":
                n = ord(s[idx]) - ord("0")
                result = result * 10 + n
            elif " " == s[idx]:
                pass
            else:
                break
            idx += 1
        self.ptr = idx
        return result

    def read_exp(self) -> str:
        s = self.s
        idx = self.ptr
        result = ""
        while idx < len(s):
            if s[idx] in ("+", "-", "*", "/"):
                result = s[idx]
                break
            elif " " == s[idx]:
                pass
            else:
                break
            idx += 1
        self.ptr = idx + 1
        return result


    def calculate(self, s: str) -> int:
        self.s = s
        stk_int, stk_exp = deque(), deque()
        result = 0
        stk_int.append(self.read_int())
        while self.ptr < len(s):
            exp = self.read_exp()
            n = self.read_int()
            if exp in ("+", "-"):
                stk_int.append(n)
                stk_exp.append(exp)
            elif exp == "*":
                stk_int.append(stk_int.pop() * n)
            elif exp == "/":
                stk_int.append(int(stk_int.pop() / n))
        # print(stk_int, stk_exp)
        while len(stk_exp) > 0:
            exp = stk_exp.popleft()
            if exp == "+":
                stk_int.appendleft(stk_int.popleft() + stk_int.popleft())
            elif exp == "-":
                n1 = stk_int.popleft()
                n2 = stk_int.popleft()
                stk_int.appendleft(n1 - n2)
        return stk_int[0]
#
# r = Solution().calculate("1+1-1")
# print(r)
