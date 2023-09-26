import math

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power_set = set[int]()
        while n > 0:
            power = int(math.log(n, 3) + 0.000000001)
            # print(n, power, power_set)
            if power in power_set:
                return False
            power_set.add(power)
            n -= 3 ** power
        return True

r = Solution().checkPowersOfThree(6574365)
print(r)

# print(math.log(243, 3))

