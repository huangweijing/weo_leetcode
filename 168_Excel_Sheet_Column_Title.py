class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while True:
            alp = columnNumber % 26
            columnNumber = int(columnNumber/ 26)
            if alp == 0:
                alp = 26
                columnNumber -= 1
            result.append(chr(alp + ord("A") - 1))
            if columnNumber == 0:
                break
        result.reverse()
        return "".join(result)

sol = Solution()
r = sol.convertToTitle(26 * 26 + 26 + 1)
print(r)