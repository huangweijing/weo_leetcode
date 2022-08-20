def guess(num: int) -> int:
    data = 123124
    if data > num:
        return 1
    elif data == num:
        return 0
    else:
        return -1

class Solution:

    def guessNumber(self, n: int) -> int:
        low = 0
        high = n + 1
        mid = (low + high) >> 1
        while low < high:
            r = guess(mid)
            if r == 0:
                return mid
            elif r < 0:
                high = mid
            elif r > 0:
                low = mid
            mid = (low + high) >> 1

