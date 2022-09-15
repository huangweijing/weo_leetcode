from typing import List

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        property_group = dict[int, list[int]]()
        property_max = dict[int, int]()
        for prop in properties:
            if prop[0] not in property_group:
                property_group[prop[0]] = list[int]()
            property_group[prop[0]].append(prop[1])
            property_max[prop[0]] = max(property_max.get(prop[0], 0), prop[1])

        key_list = list(property_group.keys())
        key_list.sort()
        stack_max = []
        stack_key = []

        result = 0
        for key in key_list:
            while len(stack_max) > 0 and stack_max[-1] < property_max[key]:
                stack_max.pop()
                popped_key = stack_key.pop()
                result += len(property_group[popped_key])
                # del property_group[popped_key]
                # del property_max[popped_key]

            stack_max.append(property_max[key])
            stack_key.append(key)

        for i in range(1, len(stack_key)):
            prev_prop = property_group[stack_key[i - 1]]
            cur_max = property_max[stack_key[i]]
            for prop in prev_prop:
                if prop < cur_max:
                    result += 1
        return result

data_properties = [[2,4],[3,3],[3,4],[3,8],[4,3],[4,9],[5,1],[5,7]]
r = Solution().numberOfWeakCharacters(data_properties)
print(r)





