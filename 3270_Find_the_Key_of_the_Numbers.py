class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        s1 = str(num1).rjust(4, "0")
        s2 = str(num2).rjust(4, "0")
        s3 = str(num3).rjust(4, "0")
        return int("".join([min(s1[i], s2[i], s3[i]) for i in range(4)]))


r = Solution().generateKey(1, 10, 1000)
print(r)
