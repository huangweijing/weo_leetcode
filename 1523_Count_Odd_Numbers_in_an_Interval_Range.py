class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low & 1 == 1:
            return ((high - low) >> 1) + 1
        else:
            if (high - low) & 1 == 0:
                return (high - low) >> 1
            else:
                return ((high - low) >> 1) + 1

