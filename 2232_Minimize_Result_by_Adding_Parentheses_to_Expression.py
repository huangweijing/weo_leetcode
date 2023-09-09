class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus_idx = expression.index("+")
        min_result = int(expression[:plus_idx]) + int(expression[plus_idx + 1:])
        ans = "(" + expression + ")"
        for i in range(plus_idx):
            num1, num2, num3, num4 = -1, 0, 0, -1
            if i == 0:
                num1 = -1
                num2 = int(expression[:plus_idx])
            else:
                num1 = int(expression[: i])
                num2 = int(expression[i: plus_idx])
            for j in range(plus_idx + 1, len(expression)):
                if j == len(expression) - 1:
                    num3 = int(expression[plus_idx + 1: ])
                    num4 = -1
                else:
                    num3 = int(expression[plus_idx + 1: j + 1])
                    num4 = int(expression[j + 1: ])

                cp_num1, cp_num4 = 1, 1
                if num1 != -1:
                    cp_num1 = num1
                if num4 != -1:
                    cp_num4 = num4
                # print(num1, num2, num3, num4, cp_num1 * (num2 + num3) * cp_num4)
                if cp_num1 * (num2 + num3) * cp_num4 < min_result:
                    min_result = cp_num1 * (num2 + num3) * cp_num4
                    if num1 == -1 and num4 == -1:
                        ans = f"({num2}+{num3})"
                    elif num1 == -1:
                        ans = f"({num2}+{num3}){num4}"
                    elif num4 == -1:
                        ans = f"{num1}({num2}+{num3})"
                    else:
                        ans = f"{num1}({num2}+{num3}){num4}"
        return ans

data = "247+38"
r = Solution().minimizeResult(data)
print(r)