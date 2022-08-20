class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = (1 << 31) - 1
        guess = (l + r) >> 1
        while True:
            square = guess ** 2
            if square == num:
                return True
            elif square > num:
                r = guess
            else:
                l = guess
            last_guess = guess
            guess = (l + r) >> 1
            if last_guess == guess:
                return False

r = Solution().isPerfectSquare(1 << 31)
print(r)

