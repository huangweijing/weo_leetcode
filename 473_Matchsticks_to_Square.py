from typing import List

class Solution:
    def __init__(self):
        self.avg_len = 0

    def validate(self, matchsticks: List[int]):
        sum_all = sum(matchsticks)
        if sum_all % 4 != 0:
            return False
        self.avg_len = sum_all // 4
        for match in matchsticks:
            if match > self.avg_len:
                return False
        return True


    def makesquare(self, matchsticks: List[int]) -> bool:


r = Solution().makesquare([4,13,1,1,14,15,1,3,13,1,3,5,2,8,12])
print(r)

# s1 = {1, 2, 3}
# s2 = {3, 4, 5}
# s1.union(s2)
# print(s1)