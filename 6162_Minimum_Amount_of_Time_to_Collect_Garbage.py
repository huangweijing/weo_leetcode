from typing import List
from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        last_station = dict[str, int]()
        garbage_cnt = dict[str, int]()
        garbage_cnt["M"] = 0
        garbage_cnt["P"] = 0
        garbage_cnt["G"] = 0
        for i, g in enumerate(garbage):
            gc = Counter(g)
            # print(gc)
            if gc["M"] != 0:
                last_station["M"] = i
            if gc["P"] != 0:
                last_station["P"] = i
            if gc["G"] != 0:
                last_station["G"] = i
            garbage_cnt["M"] += gc["M"]
            garbage_cnt["P"] += gc["P"]
            garbage_cnt["G"] += gc["G"]

        sum_travel = 0
        sum_travel_arr = []
        for t in travel:
            sum_travel += t
            sum_travel_arr.append(sum_travel)

        # print(garbage_cnt)
        # print(last_station)
        # print(sum_travel_arr)
        result = 0
        for assortment in ["M", "P", "G"]:
            if garbage_cnt[assortment] != 0:
                if last_station[assortment] == 0:
                    result += garbage_cnt[assortment]
                else:
                    result += sum_travel_arr[last_station[assortment] - 1] + garbage_cnt[assortment]
            # print(assortment, result)
        return result

data_garbage = ["MMM","PGM","GP"]
data_travel = [3, 10]
r = Solution().garbageCollection(data_garbage, data_travel)
print(r)
