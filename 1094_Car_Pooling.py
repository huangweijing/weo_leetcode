from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: [x[1], x[2]])
        way = [0] * 1002
        for trip in trips:
            way[trip[1]] += trip[0]
            way[trip[2]] -= trip[0]
        people_cnt = 0
        # print(way)
        for pick_people in way:
            people_cnt += pick_people
            # print(people_cnt)
            if people_cnt > capacity:
                return False
        return True

data = [
    [[2,1,5],[3,5,7]]
    , 3
]
r = Solution().carPooling(* data)
print(r)