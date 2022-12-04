class Solution:
    def countHousePlacements(self, n: int) -> int:
        np = [1] * 2
        for i in range(1, n):
            np[0], np[1] = (np[1] + np[0]) % (10 ** 9 + 7), np[0]
        return (np[0] + np[1]) ** 2 % (10 ** 9 + 7)
