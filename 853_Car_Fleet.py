from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(sorted(zip(position, speed), key=lambda x: x[0], reverse=True))
        max_time = 0
        ans = 0
        for car in cars:
            time = (target - car[0]) / car[1]
            # print(time)
            if time > max_time:
                ans += 1
                max_time = time
                # print(max_time)
        return ans

data = [
12
    , [10,8,0,5,3]
    , [2,4,1,1,3]
]
r = Solution().carFleet(* data)
print(r)