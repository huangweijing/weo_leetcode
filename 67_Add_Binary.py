class Solution:
    def addBinary(self, a: str, b: str) -> str:
        idx = 0
        plus_flag = False
        result = []
        while idx < len(a) and idx < len(b):
            b1 = a[-idx - 1]
            b2 = b[-idx - 1]
            b3 = int(b1) + int(b2) + (1 if plus_flag else 0)
            # print(a, b, str(b1), str(b2), str(b3), plus_flag, result)
            if b3 >= 2:
                plus_flag = True
                b3 -= 2
            else:
                plus_flag = False
            result.append(str(b3))
            idx += 1
            # print(a, b, str(b1), str(b2), str(b3), plus_flag, result)
            # print()

        if len(a) >= len(b):
            longer_one = a
        elif len(a) < len(b):
            longer_one = b

        while idx < len(longer_one):
            b1 = longer_one[-idx - 1]
            b3 = int(b1) + (1 if plus_flag else 0)
            if b3 >= 2:
                plus_flag = True
                b3 -= 2
            else:
                plus_flag = False
            result.append(str(b3))
            idx += 1

        if plus_flag:
            result.append("1")

        result.reverse()
        return "".join(result)

sol = Solution()
r = sol.addBinary("1010", "1011")
print(r)


