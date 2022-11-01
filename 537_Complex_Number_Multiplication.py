class Solution:
    def parse_complex(self, num: str) -> (int, int):
        arr = num.split("+")
        real = int(arr[0])
        imaginary = int(arr[1][:-1])
        return real, imaginary

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = self.parse_complex(num1)
        r2, i2 = self.parse_complex(num2)
        r = r1 * r2 + i1 * i2 * -1
        i = r1 * i2 + r2 * i1
        return str(r) + "+" + str(i) + "i"

data = [
    "1+-1i"
    , "1+-1i"
]
res = Solution().complexNumberMultiply(* data)
print(res)