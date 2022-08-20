import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # cur = num
        divisor_set = set[int]()
        if num != 1:
            divisor_set.add(1)
        for divisor in range(2, int(math.sqrt(num)) + 1):
            # print(divisor)
            if num % divisor == 0:
                divisor_set.add(divisor)
                divisor_set.add(int(num / divisor))
        return sum(divisor_set) == num

r = Solution().checkPerfectNumber(10**8)
print(r)


