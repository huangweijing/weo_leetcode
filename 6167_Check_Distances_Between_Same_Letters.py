from typing import List

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        my_distance = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord("a")
            if my_distance[idx] == -1:
                my_distance[idx] = i
            else:
                print(ch, i - my_distance[idx] - 1)
                if distance[idx] != i - my_distance[idx] - 1:
                    return False
        return True

data_s = "zbaazb"
data_distance = [0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3]
r = Solution().checkDistances(data_s, data_distance)
print(r)