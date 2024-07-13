from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        rl = sorted([[zip_val[0], zip_val[1], zip_val[2], i]
                     for i, zip_val in enumerate(zip(positions, healths, directions))], key=lambda x: x[0])
        stk = []
        stk_left = []
        for robot in rl:
            if robot[2] == "L":
                while len(stk) > 0:
                    stk_rb = stk.pop()
                    if stk_rb[1] < robot[1]:
                        robot[1] -= 1
                    elif stk_rb[1] > robot[1]:
                        stk_rb[1] -= 1
                        stk.append(stk_rb)
                        robot[1] = 0
                        break
                    else:
                        robot[1] = 0
                        break
                if robot[1] > 0:
                    stk_left.append(robot)
            elif robot[2] == "R":
                stk.append(robot)
        stk.extend(stk_left)
        stk.sort(key=lambda x: x[3])
        return [v[1] for v in stk]



data = [
[5,4,3,2,1]
, [2,17,9,15,10]
, "RRRRR"
]
r = Solution().survivedRobotsHealths(*data)
print(r)