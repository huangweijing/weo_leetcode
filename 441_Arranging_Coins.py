class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        mid = (low + high) >> 1
        while low < high:
            k1 = (mid + 1) * mid / 2
            k2 = (mid + 2) * (mid + 1) / 2
            if k1 <= n < k2:
                return mid
            elif n == k2:
                return mid + 1
            elif n > k2:
                low = mid
            elif n < k1:
                high = mid
            mid = (low + high) >> 1

