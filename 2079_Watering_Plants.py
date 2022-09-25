from typing import List

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        watering_can = capacity
        steps = 0
        last_pos = -1
        for i, plant in enumerate(plants):
            steps += i - last_pos
            watering_can -= plant
            if i < len(plants) - 1 and watering_can < plants[i + 1]:
                steps += i + 1
                last_pos = -1
                watering_can = capacity
            else:
                last_pos = i
        return steps

data_plants = [7,7,7,7,7,7,7]
data_k = 8
r = Solution().wateringPlants(data_plants, data_k)
print(r)
