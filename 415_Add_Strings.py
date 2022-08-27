class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num2_arr = list(num2)
        num2_arr.reverse()
        num1_arr = list(num1)
        num1_arr.reverse()
        result = list[int]()
        i = 0
        carry = 0
        while i < len(num1) or i < len(num2):
            n1 = "0"
            n2 = "0"
            if i < len(num1):
                n1 = num1_arr[i]
            if i < len(num2):
                n2 = num2_arr[i]
            r = (ord(n1) + ord(n2) - ord("0") * 2) + carry
            carry = 0
            if r >= 10:
                carry = int(r / 10)
                r = r % 10
            result.append(r)
            i += 1
        if carry > 0:
            result.append(carry)
        result.reverse()
        return "".join(map(str, result))