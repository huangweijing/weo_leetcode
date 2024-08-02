from typing import List
from collections import defaultdict


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        d1 = defaultdict(lambda: list[int]())
        d2 = defaultdict(lambda: list[int]())
        d3 = defaultdict(lambda: list[int]())
        for triplet in triplets:
            d1[triplet[0]].append(triplet)
            d2[triplet[1]].append(triplet)
            d3[triplet[2]].append(triplet)
        okay_flag = False
        for triplet in d1[target[0]]:
            if triplet[1] <= target[1] and triplet[2] <= target[2]:
                okay_flag = True
                break
        if not okay_flag:
            return False
        okay_flag = False
        for triplet in d2[target[1]]:
            if triplet[0] <= target[0] and triplet[2] <= target[2]:
                okay_flag = True
                break
        if not okay_flag:
            return False
        okay_flag = False
        for triplet in d3[target[2]]:
            if triplet[1] <= target[1] and triplet[0] <= target[0]:
                okay_flag = True
                break
        return okay_flag
        

data = [[[3,5,1],[10,5,7]]
        , [3,5,7]]
r = Solution().mergeTriplets(* data)
print(r)