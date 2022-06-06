class Solution:
    ZERO = ord("0")

    def mul_1_1(self, num1: str, num2: str, carry: int = 0):
        result = (ord(num1) - Solution.ZERO) * (ord(num2) - Solution.ZERO) + carry
        return [result % 10, int(result / 10)]

    def mul_n_1(self, num1: str, num2: str, carry: int = 0):
        idx = len(num1) - 1
        result = []
        while idx >= 0:
            r = self.mul_1_1(num1[idx], num2, carry)
            carry = r[1]
            result.append(r[0])
            idx -= 1
        result.append(carry)
        result.reverse()
        return result

    def mul_n_n(self, num1: str, num2: str):
        idx = len(num2) - 1
        result = []
        carry = 0
        while idx >= 0:
            r = self.mul_n_1(num1, num2[idx], carry)

    def add_n_n(self, num1: list[int], num2: list[int]):
        pass


    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))

# sol = Solution()
# print(sol.mul_1_1("8", "3"))
# print(sol.mul_n_1("99", "3"))
