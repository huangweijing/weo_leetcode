from typing import List

class Solution:
    def move(self, pos: list[int], n: int,cmd: str) -> bool:
        if cmd == "L":
            if pos[1] == 0:
                return False
            else:
                pos[1] -= 1
        elif cmd == "R":
            if pos[1] == n - 1:
                return False
            else:
                pos[1] += 1
        elif cmd == "U":
            if pos[0] == 0:
                return False
            else:
                pos[0] -= 1
        elif cmd == "D":
            if pos[0] == n - 1:
                return False
            else:
                pos[0] += 1
        return True

    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        result = []
        for i in range(len(s)):
            cur_pos = startPos.copy()
            steps = 0
            for ch in s[i:]:
                print(cur_pos)
                if self.move(cur_pos, n, ch):
                    steps += 1
                else:
                    break
            result.append(steps)
        return result


data = [10
        ,[9,6]
        ,"UDDDUDDURRLLDRDDRRUU"
        ]
r = Solution().executeInstructions(* data)
print(r)