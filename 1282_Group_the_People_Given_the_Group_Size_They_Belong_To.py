from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = dict[int, list[list[int]]]()
        for i, group_size in enumerate(groupSizes):
            if group_size not in group_dict:
                group_dict[group_size] = list[list[int]]()
            group_list = group_dict[group_size]
            if len(group_list) == 0 or len(group_list[-1]) == group_size:
                new_list = list[int]()
                new_list.append(i)
                group_list.append(new_list)
            else:
                group_list[-1].append(i)

        result = []
        for groups in group_dict.values():
            for group in groups:
                result.append(group)
        return result
