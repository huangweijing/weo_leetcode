class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(1, 100):
            print(i, num1 - num2 * i, bin(num1 - num2 * i))
            if num1 - num2 * i <= 0:
                return -1
            if i > num1 - num2 * i:
                continue
            if (num1 - num2 * i).bit_count() <= i:
                return i
        return -1

r = Solution().makeTheIntegerZero(85, 42)
print(r)

# print(int(10).bit_count())