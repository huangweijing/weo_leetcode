class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            minus = -1
            num = x * -1
        else:
            minus = 1
            num = x

        dig_list = []
        while num > 0:
            dig = num % 10
            dig_list.append(dig)
            num = int(num / 10)

        result = 0
        for dig in dig_list:
            result = result * 10 + dig
        result = result * minus

        if result > pow(2, 31) - 1 or result < -pow(2, 31):
            return 0

        return result

# sol = Solution()
# print(sol.reverse(-321))

