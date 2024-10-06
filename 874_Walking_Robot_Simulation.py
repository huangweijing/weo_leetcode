from typing import List
import bisect
from collections import defaultdict


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        xline = defaultdict(lambda: list[int]())
        yline = defaultdict(lambda: list[int]())
        for obs in obstacles:
            xline[obs[1]].append(obs[0])
            yline[obs[0]].append(obs[1])
        for val in xline.values():
            val.sort()
        for val in yline.values():
            val.sort()
        # print(xline, yline)
        pos = [0, 0]
        direct = [0, 1]
        ans = 0
        for cmd in commands:
            if cmd == -1:
                direct = [direct[1], -direct[0]]
            elif cmd == -2:
                direct = [-direct[1], direct[0]]
            else:
                if direct == [0, 1]:
                    line = yline[pos[0]]
                    idx = bisect.bisect_right(line, pos[1])
                    if idx >= len(line) or line[idx] > pos[1] + cmd:
                        pos = [pos[0], pos[1] + cmd]
                    else:
                        pos = [pos[0], line[idx] - 1]
                elif direct == [0, -1]:
                    line = yline[pos[0]]
                    idx = bisect.bisect_right(line, pos[1] - cmd - 1)
                    if idx >= len(line) or line[idx] >= pos[1]:
                        pos = [pos[0], pos[1] - cmd]
                    else:
                        pos = [pos[0], line[idx] + 1]
                elif direct == [1, 0]:
                    line = xline[pos[1]]
                    idx = bisect.bisect_right(line, pos[0])
                    if idx >= len(line) or line[idx] > pos[0] + cmd:
                        pos = [pos[0] + cmd, pos[1]]
                    else:
                        pos = [line[idx] - 1, pos[1]]
                elif direct == [-1, 0]:
                    line = xline[pos[1]]
                    idx = bisect.bisect_right(line, pos[0] - cmd - 1)
                    if idx >= len(line) or line[idx] >= pos[0]:
                        pos = [pos[0] - cmd, pos[1]]
                    else:
                        pos = [line[idx] + 1, pos[1]]
            print(pos, direct)
            ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans
    


data = [
    [-2,-1,-2,3,7]
    , [[1,-3],[2,-3],[4,0],[-2,5],[-5,2],[0,0],[4,-4],[-2,-5],[-1,-2],[0,2]]
]
r = Solution().robotSim(*data)
print(r)
                
