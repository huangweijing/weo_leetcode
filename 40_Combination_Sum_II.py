from typing import List

class Solution:
    def __init__(self):
        self.cache = dict[str, List[List[int]]]()
        pass

    def get_key(self, target, candidates: List[int]):
        candidates = candidates.copy()
        candidates.sort()
        key = str(target) + "_"
        for i in candidates:
            if i < 10:
                key += "0"
            key += str(i)
        return key

    def add_to_cache(self, target: int, candidates: List[int], result: List[List[int]]):
        key = self.get_key(target, candidates)
        self.cache[key] = result
        # self.cache[key] = [ele.copy() for ele in result]

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 0:
            return []
        if target == 0:
            return [[]]
        key = self.get_key(target, candidates)
        if key in self.cache.keys():
            # print(key, self.cache[key])
            return self.cache[key]

        result: list[list[int]] = []
        cand_backup = candidates.copy()
        for cand in candidates:
            cand_backup.remove(cand)
            # print(f"cand_backup={cand_backup}, cand={cand}, target={target}")
            n_1_result: list[list[int]] = self.combinationSum2(cand_backup, target - cand)
            if n_1_result is not None:
                for ele in n_1_result:
                    ele = ele.copy()
                    ele.append(cand)
                    result.append(ele)
            cand_backup.append(cand)

        # remove duplication
        r_map = dict[str, list[int]]()
        for ele in result:
            key = self.get_key(0, ele)
            r_map[key] = ele

        key = self.get_key(target, candidates)
        result = list(r_map.values())
        self.cache[key] = result

        # print(candidates, target, result)
        return result


# print(l)


sol = Solution()
# _candidates = [10,1,2,7,6,1,5]
# _target = 8
_candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
# print(len(_candidates))
_target = 27
r = sol.combinationSum2(_candidates, _target)
print(r)
