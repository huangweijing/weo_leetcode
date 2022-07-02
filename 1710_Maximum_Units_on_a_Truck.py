from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        print(boxTypes)
        units = 0
        for boxType in boxTypes:
            if boxType[0] > truckSize:
                units += truckSize * boxType[1]
            else:
                units += boxType[0] * boxType[1]
            truckSize -= boxType[0]
            if truckSize <= 0:
                return units

        return units

r = Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
print(r)