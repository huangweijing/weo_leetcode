class Solution:
    def countDigits(self, num: int) -> int:
        ans = 0
        num_copy = num
        while num > 0:
            if num_copy % (num % 10) == 0:
                ans += 1
            num //= 10
        return ans