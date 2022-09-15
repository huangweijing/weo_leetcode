from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key=lambda x: x[0])
        slope = [coordinates[1][0] - coordinates[0][0], coordinates[1][1] - coordinates[0][1]]
        for i in range(1, len(coordinates)):
            # print((coordinates[i][0] - coordinates[i - 1][0]))
            # print((coordinates[i][1] - coordinates[i - 1][1]))
            if (coordinates[i][0] - coordinates[i - 1][0]) * slope[1] != \
                    (coordinates[i][1] - coordinates[i - 1][1]) * slope[0]:
                return False
        return True

data_coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
r = Solution().checkStraightLine(data_coordinates)
print(r)