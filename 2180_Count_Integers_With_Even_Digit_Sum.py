class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for i in range(1, num + 1):
            sum_dig = 0
            for dig in str(i):
                sum_dig += int(dig)
            ans += 1 if sum_dig & 1 == 0 else 0
        return ans
