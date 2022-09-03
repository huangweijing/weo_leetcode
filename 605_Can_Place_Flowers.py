from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                if i > 0:
                    flowerbed[i - 1] = 2
                if i < len(flowerbed) - 1:
                    flowerbed[i + 1] = 2

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
                if i > 0:
                    flowerbed[i - 1] = 2
                if i < len(flowerbed) - 1:
                    flowerbed[i + 1] = 2
            if n == 0:
                return True
        return False
