from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]]
                          , veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        ans = []
        for rest in restaurants:
            if veganFriendly == 1 and rest[2] != veganFriendly:
                continue
            if rest[3] > maxPrice:
                continue
            if rest[4] > maxDistance:
                continue
            ans.append(rest)
        ans.sort(key=lambda x: [-x[1], -x[0]])
        return [rest[0] for rest in ans]
        