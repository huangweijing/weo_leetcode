from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        result = list[str]()
        global_dict = dict[str, int]()
        for word in words2:
            local_dict = dict[str, int]()
            for ch in word:
                if ch not in local_dict:
                    local_dict[ch] = 0
                local_dict[ch] += 1

            for key in local_dict.keys():
                if key not in global_dict:
                    global_dict[key] = local_dict[key]
                else:
                    if global_dict[key] < local_dict[key]:
                        global_dict[key] = local_dict[key]

        for word in words1:
            local_dict = dict[str, int]()
            for ch in word:
                if ch not in local_dict:
                    local_dict[ch] = 0
                local_dict[ch] += 1
            should_pick = True
            for key in global_dict.keys():
                if key not in local_dict:
                    should_pick = False
                    break
                if global_dict[key] > local_dict[key]:
                    should_pick = False
                    break
            if should_pick:
                result.append(word)

        return result

sol = Solution()
r = sol.wordSubsets(
    ["amazon","apple","facebook","google","leetcode"]
    ,["e","o"]
)
print(r)