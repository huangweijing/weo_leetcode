from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_rest = dict[str, int]()
        common_set = set[str]()
        rank_dict = dict[int, list]()
        for i, rest in enumerate(list1):
            common_rest[rest] = i
        for i, rest in enumerate(list2):
            if rest in common_rest:
                common_rest[rest] += i
                common_set.add(rest)
        for rest in common_set:
            val = common_rest[rest]
            if val not in rank_dict:
                rank_dict[val] = list[str]()
            rank_dict[val].append(rest)

        rank_list = list(rank_dict.keys())
        rank_list.sort()
        return rank_dict[rank_list[0]]
