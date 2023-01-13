from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        cap_rocks = zip(capacity, rocks)
        rock_space = [t[0] - t[1] for t in cap_rocks]
        rock_space.sort()
        ans, i = 0, 0
        while additionalRocks > 0 and i < len(rock_space):
            if additionalRocks < rock_space[i]:
                break
            additionalRocks -= rock_space[i]
            i += 1
            ans += 1
        return ans

