from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for item in asteroids:
            if item > 0:
                stk.append(item)
            elif item < 0:
                while len(stk) > 0 and 0 < stk[-1] < -item:
                    stk.pop()
                if len(stk) == 0:
                    stk.append(item)
                elif len(stk) > 0:
                    if stk[-1] < 0:
                        stk.append(item)
                    elif stk[-1] == -item:
                        stk.pop()
                    # elif stk[-1] > -item:
        return stk


data = [-10,7,-5]
r = Solution().asteroidCollision(data)
print(r)
