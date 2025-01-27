from typing import List
from collections import defaultdict

class Solution:

    def __init__(self) -> None:
        self.pt_dict = defaultdict(lambda: list[int]())
        self.found = False

    def next_step(self, pyramid: list[list[str]]):
        # print(pyramid)
        if len(pyramid[-1]) == 1 and len(pyramid[0]) == len(pyramid):
            self.found = True
        if self.found:
            return
        if len(pyramid) == 1 or len(pyramid[-1]) + 1 == len(pyramid[-2]):
            new_layer = list[int]()
            key = pyramid[-1][0] + pyramid[-1][1]
            if key not in self.pt_dict:
                return
            else:
                for pt in self.pt_dict[key]:
                    new_layer.append(pt)
                    pyramid.append(new_layer)
                    self.next_step(pyramid)
                    new_layer.pop()
                    pyramid.pop()
        else:
            # print(pyramid[-2], len(pyramid[-1]) + 1)
            key = pyramid[-2][len(pyramid[-1])] + pyramid[-2][len(pyramid[-1]) + 1]
            if key not in self.pt_dict:
                return 
            else:
                for pt in self.pt_dict[key]:
                    pyramid[-1].append(pt)
                    self.next_step(pyramid)
                    pyramid[-1].pop()

    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        for pattern in allowed:
            self.pt_dict[pattern[:2]].append(pattern[2])
        self.next_step([list(bottom)])
        return self.found
    

data = [
    "BCD"
    , ["BCC","CDE","CEA","FFF"]
]
r = Solution().pyramidTransition(*data)
print(r)